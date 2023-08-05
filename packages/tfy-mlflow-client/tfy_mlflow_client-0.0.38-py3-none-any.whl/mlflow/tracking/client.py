"""
Internal package providing a Python CRUD interface to MLflow experiments, runs, registered models,
and model versions. This is a lower level API than the :py:mod:`mlflow.tracking.fluent` module,
and is exposed in the :py:mod:`mlflow.tracking` module.
"""
import contextlib
import json
import logging
import os
import posixpath
import sys
import tempfile
import uuid
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Sequence, Union

import yaml

from mlflow.entities import (
    SENTINEL,
    Artifact,
    ArtifactType,
    ArtifactVersion,
    ArtifactVersionStatus,
    CustomMetric,
    Experiment,
    Feature,
    FileInfo,
    Metric,
    Model,
    ModelSchema,
    ModelVersion,
    MultiPartUpload,
    Param,
    Run,
    RunInfo,
    RunLog,
    RunTag,
    SignedURL,
    ViewType,
)
from mlflow.store.entities.paged_list import PagedList
from mlflow.store.tracking import _SEARCH_MAX_RESULTS_DEFAULT
from mlflow.tracking._tracking_service import utils
from mlflow.tracking._tracking_service.client import TrackingServiceClient

if TYPE_CHECKING:
    import matplotlib  # pylint: disable=unused-import
    import numpy  # pylint: disable=unused-import
    import PIL  # pylint: disable=unused-import
    import plotly  # pylint: disable=unused-import

_logger = logging.getLogger(__name__)


class MlflowClient:
    """
    Client of an MLflow Tracking Server that creates and manages experiments and runs, and of an
    MLflow Registry Server that creates and manages registered models and model versions. It's a
    thin wrapper around TrackingServiceClient and RegistryClient so there is a unified API but we
    can keep the implementation of the tracking and registry clients independent from each other.
    """

    def __init__(self, tracking_uri: Optional[str] = None, registry_uri: Optional[str] = None):
        """
        :param tracking_uri: Address of local or remote tracking server. If not provided, defaults
                             to the service set by ``mlflow.tracking.set_tracking_uri``. See
                             `Where Runs Get Recorded <../tracking.html#where-runs-get-recorded>`_
                             for more info.
        :param registry_uri: Address of local or remote model registry server. If not provided,
                             defaults to the service set by ``mlflow.tracking.set_registry_uri``. If
                             no such service was set, defaults to the tracking uri of the client.
        """
        final_tracking_uri = utils._resolve_tracking_uri(tracking_uri)
        self._tracking_client = TrackingServiceClient(final_tracking_uri)

    # Tracking API

    def get_run(self, run_id: str) -> Run:
        """
        Fetch the run from backend store. The resulting :py:class:`Run <mlflow.entities.Run>`
        contains a collection of run metadata -- :py:class:`RunInfo <mlflow.entities.RunInfo>`,
        as well as a collection of run parameters, tags, and metrics --
        :py:class:`RunData <mlflow.entities.RunData>`. In the case where multiple metrics with the
        same key are logged for the run, the :py:class:`RunData <mlflow.entities.RunData>` contains
        the most recently logged value at the largest step for each metric.

        :param run_id: Unique identifier for the run.

        :return: A single :py:class:`mlflow.entities.Run` object, if the run exists. Otherwise,
                 raises an exception.

        .. code-block:: python
            :caption: Example

            import mlflow
            from mlflow.tracking import MlflowClient

            with mlflow.start_run() as run:
                mlflow.log_param("p", 0)

            # The run has finished since we have exited the with block
            # Fetch the run
            client = MlflowClient()
            run = client.get_run(run.info.run_id)
            print("run_id: {}".format(run.info.run_id))
            print("params: {}".format(run.data.params))
            print("status: {}".format(run.info.status))

        .. code-block:: text
            :caption: Output

            run_id: e36b42c587a1413ead7c3b6764120618
            params: {'p': '0'}
            status: FINISHED
        """
        return self._tracking_client.get_run(run_id)

    def get_metric_history(self, run_id: str, key: str) -> List[Metric]:
        """
        Return a list of metric objects corresponding to all values logged for a given metric.

        :param run_id: Unique identifier for run
        :param key: Metric name within the run

        :return: A list of :py:class:`mlflow.entities.Metric` entities if logged, else empty list

        .. code-block:: python
            :caption: Example

            from mlflow.tracking import MlflowClient

            def print_metric_info(history):
                for m in history:
                    print("name: {}".format(m.key))
                    print("value: {}".format(m.value))
                    print("step: {}".format(m.step))
                    print("timestamp: {}".format(m.timestamp))
                    print("--")

            # Create a run under the default experiment (whose id is "0"). Since this is low-level
            # CRUD operation, the method will create a run. To end the run, you'll have
            # to explicitly end it.
            client = MlflowClient()
            experiment_id = "0"
            run = client.create_run(experiment_id)
            print("run_id: {}".format(run.info.run_id))
            print("--")

            # Log couple of metrics, update their initial value, and fetch each
            # logged metrics' history.
            for k, v in [("m1", 1.5), ("m2", 2.5)]:
                client.log_metric(run.info.run_id, k, v, step=0)
                client.log_metric(run.info.run_id, k, v + 1, step=1)
                print_metric_info(client.get_metric_history(run.info.run_id, k))
            client.set_terminated(run.info.run_id)

        .. code-block:: text
            :caption: Output

            run_id: c360d15714994c388b504fe09ea3c234
            --
            name: m1
            value: 1.5
            step: 0
            timestamp: 1603423788607
            --
            name: m1
            value: 2.5
            step: 1
            timestamp: 1603423788608
            --
            name: m2
            value: 2.5
            step: 0
            timestamp: 1603423788609
            --
            name: m2
            value: 3.5
            step: 1
            timestamp: 1603423788610
            --
        """
        return self._tracking_client.get_metric_history(run_id, key)

    def create_run(
        self,
        experiment_id: str,
        start_time: Optional[int] = None,
        tags: Optional[Dict[str, Any]] = None,
        name: str = "",
        description: Optional[str] = None,
    ) -> Run:
        """
        Create a :py:class:`mlflow.entities.Run` object that can be associated with
        metrics, parameters, artifacts, etc.
        Unlike :py:func:`mlflow.projects.run`, creates objects but does not run code.
        Unlike :py:func:`mlflow.start_run`, does not change the "active run" used by
        :py:func:`mlflow.log_param`.

        :param experiment_id: The string ID of the experiment to create a run in.
        :param start_time: If not provided, use the current timestamp.
        :param tags: A dictionary of key-value pairs that are converted into
                     :py:class:`mlflow.entities.RunTag` objects.
        :return: :py:class:`mlflow.entities.Run` that was created.

        .. code-block:: python
            :caption: Example

            from mlflow.tracking import MlflowClient

            # Create a run with a tag under the default experiment (whose id is '0').
            tags = {"engineering": "ML Platform"}
            client = MlflowClient()
            experiment_id = "0"
            run = client.create_run(experiment_id, tags=tags)

            # Show newly created run metadata info
            print("Run tags: {}".format(run.data.tags))
            print("Experiment id: {}".format(run.info.experiment_id))
            print("Run id: {}".format(run.info.run_id))
            print("lifecycle_stage: {}".format(run.info.lifecycle_stage))
            print("status: {}".format(run.info.status))

        .. code-block:: text
            :caption: Output

            Run tags: {'engineering': 'ML Platform'}
            Experiment id: 0
            Run id: 65fb9e2198764354bab398105f2e70c1
            lifecycle_stage: active
            status: RUNNING
        """
        return self._tracking_client.create_run(
            experiment_id, start_time, tags, name=name, description=description
        )

    def list_run_infos(
        self,
        experiment_id: str,
        run_view_type: int = ViewType.ACTIVE_ONLY,
        max_results: int = _SEARCH_MAX_RESULTS_DEFAULT,
        order_by: Optional[List[str]] = None,
        page_token: Optional[str] = None,
    ) -> PagedList[RunInfo]:
        """
        Return run information for runs which belong to the experiment_id.

        :param experiment_id: The experiment id which to search
        :param run_view_type: ACTIVE_ONLY, DELETED_ONLY, or ALL runs
        :param max_results: Maximum number of results desired.
        :param order_by: List of order_by clauses. Currently supported values are
            are ``metric.key``, ``parameter.key``, ``tag.key``, ``attribute.key``.
            For example, ``order_by=["tag.release ASC", "metric.click_rate DESC"]``.

        :return: A :py:class:`PagedList <mlflow.store.entities.PagedList>` of
            :py:class:`RunInfo <mlflow.entities.RunInfo>` objects that satisfy the search
            expressions. If the underlying tracking store supports pagination, the token for the
            next page may be obtained via the ``token`` attribute of the returned object.

        .. code-block:: python
            :caption: Example

            import mlflow
            from mlflow.tracking import MlflowClient
            from mlflow.entities import ViewType

            def print_run_infos(run_infos):
                for r in run_infos:
                    print("- run_id: {}, lifecycle_stage: {}".format(r.run_id, r.lifecycle_stage))

            # Create two runs
            with mlflow.start_run() as run1:
                mlflow.log_metric("click_rate", 1.55)

            with mlflow.start_run() as run2:
                mlflow.log_metric("click_rate", 2.50)

            # Delete the last run
            client = MlflowClient()
            client.delete_run(run2.info.run_id)

            # Get all runs under the default experiment (whose id is 0)
            print("Active runs:")
            print_run_infos(mlflow.list_run_infos("0", run_view_type=ViewType.ACTIVE_ONLY))

            print("Deleted runs:")
            print_run_infos(mlflow.list_run_infos("0", run_view_type=ViewType.DELETED_ONLY))

            print("All runs:")
            print_run_infos(mlflow.list_run_infos("0", run_view_type=ViewType.ALL,
                            order_by=["metric.click_rate DESC"]))

        .. code-block:: text
            :caption: Output

            Active runs:
            - run_id: 47b11b33f9364ee2b148c41375a30a68, lifecycle_stage: active
            Deleted runs:
            - run_id: bc4803439bdd4a059103811267b6b2f4, lifecycle_stage: deleted
            All runs:
            - run_id: bc4803439bdd4a059103811267b6b2f4, lifecycle_stage: deleted
            - run_id: 47b11b33f9364ee2b148c41375a30a68, lifecycle_stage: active
        """
        return self._tracking_client.list_run_infos(
            experiment_id, run_view_type, max_results, order_by, page_token
        )

    def list_experiments(
        self,
        view_type: int = ViewType.ACTIVE_ONLY,
        max_results: Optional[int] = None,
        page_token: Optional[str] = None,
    ) -> PagedList[Experiment]:
        """
        :param view_type: Qualify requested type of experiments.
        :param max_results: If passed, specifies the maximum number of experiments desired. If not
                            passed, all experiments will be returned for the File and SQL backends.
                            For the REST backend, the server will pick a maximum number of results
                            to return.
        :param page_token: Token specifying the next page of results. It should be obtained from
                            a ``list_experiments`` call.
        :return: A :py:class:`PagedList <mlflow.store.entities.PagedList>` of
                 :py:class:`Experiment <mlflow.entities.Experiment>` objects. The pagination token
                 for the next page can be obtained via the ``token`` attribute of the object.

        .. code-block:: python
            :caption: Example

            from mlflow.tracking import MlflowClient
            from mlflow.entities import ViewType

            def print_experiment_info(experiments):
                for e in experiments:
                    print("- experiment_id: {}, name: {}, lifecycle_stage: {}"
                          .format(e.experiment_id, e.name, e.lifecycle_stage))

            client = MlflowClient()
            for name in ["Experiment 1", "Experiment 2"]:
                exp_id = client.create_experiment(name)

            # Delete the last experiment
            client.delete_experiment(exp_id)

            # Fetch experiments by view type
            print("Active experiments:")
            print_experiment_info(client.list_experiments(view_type=ViewType.ACTIVE_ONLY))
            print("Deleted experiments:")
            print_experiment_info(client.list_experiments(view_type=ViewType.DELETED_ONLY))
            print("All experiments:")
            print_experiment_info(client.list_experiments(view_type=ViewType.ALL))

        .. code-block:: text
            :caption: Output

            Active experiments:
            - experiment_id: 0, name: Default, lifecycle_stage: active
            - experiment_id: 1, name: Experiment 1, lifecycle_stage: active
            Deleted experiments:
            - experiment_id: 2, name: Experiment 2, lifecycle_stage: deleted
            All experiments:
            - experiment_id: 0, name: Default, lifecycle_stage: active
            - experiment_id: 1, name: Experiment 1, lifecycle_stage: active
            - experiment_id: 2, name: Experiment 2, lifecycle_stage: deleted
        """
        return self._tracking_client.list_experiments(
            view_type=view_type, max_results=max_results, page_token=page_token
        )

    def get_experiment(self, experiment_id: str) -> Experiment:
        """
        Retrieve an experiment by experiment_id from the backend store

        :param experiment_id: The experiment ID returned from ``create_experiment``.
        :return: :py:class:`mlflow.entities.Experiment`

        .. code-block:: python
            :caption: Example

            from mlflow.tracking import MlflowClient

            client = MlflowClient()
            exp_id = client.create_experiment("Experiment")
            experiment = client.get_experiment(exp_id)

            # Show experiment info
            print("Name: {}".format(experiment.name))
            print("Experiment ID: {}".format(experiment.experiment_id))
            print("Artifact Location: {}".format(experiment.artifact_location))
            print("Lifecycle_stage: {}".format(experiment.lifecycle_stage))

        .. code-block:: text
            :caption: Output

            Name: Experiment
            Experiment ID: 1
            Artifact Location: file:///.../mlruns/1
            Lifecycle_stage: active
        """
        return self._tracking_client.get_experiment(experiment_id)

    def get_experiment_by_name(self, name: str) -> Optional[Experiment]:
        """
        Retrieve an experiment by experiment name from the backend store

        :param name: The experiment name, which is case sensitive.
        :return: An instance of :py:class:`mlflow.entities.Experiment`
                 if an experiment with the specified name exists, otherwise None.

        .. code-block:: python
            :caption: Example

            from mlflow.tracking import MlflowClient

            # Case-sensitive name
            client = MlflowClient()
            experiment = client.get_experiment_by_name("Default")

            # Show experiment info
            print("Name: {}".format(experiment.name))
            print("Experiment ID: {}".format(experiment.experiment_id))
            print("Artifact Location: {}".format(experiment.artifact_location))
            print("Lifecycle_stage: {}".format(experiment.lifecycle_stage))

        .. code-block:: text
            :caption: Output

            Name: Default
            Experiment ID: 0
            Artifact Location: file:///.../mlruns/0
            Lifecycle_stage: active
        """
        return self._tracking_client.get_experiment_by_name(name)

    def create_experiment(
        self,
        name: str,
        tags: Optional[Dict[str, Any]] = None,
        description: Optional[str] = None,
        storage_integration_fqn: Optional[str] = None,
    ) -> str:
        """Create an experiment.

        :param name: The experiment name. Must be unique.
        :param storage_integration_fqn: The storage integration FQN to use for the experiment for saving artifacts.
        :param tags: A dictionary of key-value pairs that are converted into
                                :py:class:`mlflow.entities.ExperimentTag` objects, set as
                                experiment tags upon experiment creation.
        :return: String as an integer ID of the created experiment.

        .. code-block:: python
            :caption: Example

            from mlflow.tracking import MlflowClient

            # Create an experiment with a name that is unique and case sensitive.
            client = MlflowClient()
            experiment_id = client.create_experiment("Social NLP Experiments")
            client.set_experiment_tag(experiment_id, "nlp.framework", "Spark NLP")

            # Fetch experiment metadata information
            experiment = client.get_experiment(experiment_id)
            print("Name: {}".format(experiment.name))
            print("Experiment_id: {}".format(experiment.experiment_id))
            print("Artifact Location: {}".format(experiment.artifact_location))
            print("Tags: {}".format(experiment.tags))
            print("Lifecycle_stage: {}".format(experiment.lifecycle_stage))

        .. code-block:: text
            :caption: Output

            Name: Social NLP Experiments
            Experiment_id: 1
            Artifact Location: file:///.../mlruns/1
            Tags: {'nlp.framework': 'Spark NLP'}
            Lifecycle_stage: active
        """
        return self._tracking_client.create_experiment(
            name=name,
            tags=tags,
            description=description,
            storage_integration_fqn=storage_integration_fqn,
        )

    def delete_experiment(self, experiment_id: str) -> None:
        """
        Delete an experiment from the backend store.

        :param experiment_id: The experiment ID returned from ``create_experiment``.

        .. code-block:: python
            :caption: Example

            from mlflow.tracking import MlflowClient

            # Create an experiment with a name that is unique and case sensitive
            client = MlflowClient()
            experiment_id = client.create_experiment("New Experiment")
            client.delete_experiment(experiment_id)

            # Examine the deleted experiment details.
            experiment = client.get_experiment(experiment_id)
            print("Name: {}".format(experiment.name))
            print("Artifact Location: {}".format(experiment.artifact_location))
            print("Lifecycle_stage: {}".format(experiment.lifecycle_stage))

        .. code-block:: text
            :caption: Output

            Name: New Experiment
            Artifact Location: file:///.../mlruns/1
            Lifecycle_stage: deleted
        """
        self._tracking_client.delete_experiment(experiment_id)

    def restore_experiment(self, experiment_id: str) -> None:
        """
        Restore a deleted experiment unless permanently deleted.

        :param experiment_id: The experiment ID returned from ``create_experiment``.

        .. code-block:: python
            :caption: Example

            from mlflow.tracking import MlflowClient

            def print_experiment_info(experiment):
                print("Name: {}".format(experiment.name))
                print("Experiment Id: {}".format(experiment.experiment_id))
                print("Lifecycle_stage: {}".format(experiment.lifecycle_stage))

            # Create and delete an experiment
            client = MlflowClient()
            experiment_id = client.create_experiment("New Experiment")
            client.delete_experiment(experiment_id)

            # Examine the deleted experiment details.
            experiment = client.get_experiment(experiment_id)
            print_experiment_info(experiment)
            print("--")

            # Restore the experiment and fetch its info
            client.restore_experiment(experiment_id)
            experiment = client.get_experiment(experiment_id)
            print_experiment_info(experiment)

        .. code-block:: text
            :caption: Output

            Name: New Experiment
            Experiment Id: 1
            Lifecycle_stage: deleted
            --
            Name: New Experiment
            Experiment Id: 1
            Lifecycle_stage: active
        """
        self._tracking_client.restore_experiment(experiment_id)

    def rename_experiment(self, experiment_id: str, new_name: str) -> None:
        """
        Update an experiment's name. The new name must be unique.

        :param experiment_id: The experiment ID returned from ``create_experiment``.

        .. code-block:: python
            :caption: Example

            from mlflow.tracking import MlflowClient

            def print_experiment_info(experiment):
                print("Name: {}".format(experiment.name))
                print("Experiment_id: {}".format(experiment.experiment_id))
                print("Lifecycle_stage: {}".format(experiment.lifecycle_stage))

            # Create an experiment with a name that is unique and case sensitive
            client = MlflowClient()
            experiment_id = client.create_experiment("Social NLP Experiments")

            # Fetch experiment metadata information
            experiment = client.get_experiment(experiment_id)
            print_experiment_info(experiment)
            print("--")

            # Rename and fetch experiment metadata information
            client.rename_experiment(experiment_id, "Social Media NLP Experiments")
            experiment = client.get_experiment(experiment_id)
            print_experiment_info(experiment)

        .. code-block:: text
            :caption: Output

            Name: Social NLP Experiments
            Experiment_id: 1
            Lifecycle_stage: active
            --
            Name: Social Media NLP Experiments
            Experiment_id: 1
            Lifecycle_stage: active
        """
        self._tracking_client.rename_experiment(experiment_id, new_name)

    def update_experiment(self, experiment_id: str, description) -> None:
        self._tracking_client.update_experiment(experiment_id, description)

    def log_metric(
        self,
        run_id: str,
        key: str,
        value: float,
        timestamp: Optional[int] = None,
        step: Optional[int] = None,
    ) -> None:
        """
        Log a metric against the run ID.

        :param run_id: The run id to which the metric should be logged.
        :param key: Metric name (string). This string may only contain alphanumerics, underscores
                    (_), dashes (-), periods (.), spaces ( ), and slashes (/).
                    All backend stores will support keys up to length 250, but some may
                    support larger keys.
        :param value: Metric value (float). Note that some special values such
                      as +/- Infinity may be replaced by other values depending on the store. For
                      example, the SQLAlchemy store replaces +/- Inf with max / min float values.
                      All backend stores will support values up to length 5000, but some
                      may support larger values.
        :param timestamp: Time when this metric was calculated. Defaults to the current system time.
        :param step: Integer training step (iteration) at which was the metric calculated.
                     Defaults to 0.

        .. code-block:: python
            :caption: Example

            from mlflow.tracking import MlflowClient

            def print_run_info(r):
                print("run_id: {}".format(r.info.run_id))
                print("metrics: {}".format(r.data.metrics))
                print("status: {}".format(r.info.status))

            # Create a run under the default experiment (whose id is '0').
            # Since these are low-level CRUD operations, this method will create a run.
            # To end the run, you'll have to explicitly end it.
            client = MlflowClient()
            experiment_id = "0"
            run = client.create_run(experiment_id)
            print_run_info(run)
            print("--")

            # Log the metric. Unlike mlflow.log_metric this method
            # does not start a run if one does not exist. It will log
            # the metric for the run id in the backend store.
            client.log_metric(run.info.run_id, "m", 1.5)
            client.set_terminated(run.info.run_id)
            run = client.get_run(run.info.run_id)
            print_run_info(run)

        .. code-block:: text
            :caption: Output

            run_id: 95e79843cb2c463187043d9065185e24
            metrics: {}
            status: RUNNING
            --
            run_id: 95e79843cb2c463187043d9065185e24
            metrics: {'m': 1.5}
            status: FINISHED
        """
        self._tracking_client.log_metric(run_id, key, value, timestamp, step)

    def log_param(self, run_id: str, key: str, value: Any) -> None:
        """
        Log a parameter against the run ID.

        :param run_id: The run id to which the param should be logged.
        :param key: Parameter name (string). This string may only contain alphanumerics, underscores
                    (_), dashes (-), periods (.), spaces ( ), and slashes (/).
                    All backend stores will support keys up to length 250, but some may
                    support larger keys.
        :param value: Parameter value (string, but will be string-ified if not).
                      All backend stores will support values up to length 5000, but some
                      may support larger values.

        .. code-block:: python
            :caption: Example

            from mlflow.tracking import MlflowClient

            def print_run_info(r):
                print("run_id: {}".format(r.info.run_id))
                print("params: {}".format(r.data.params))
                print("status: {}".format(r.info.status))

            # Create a run under the default experiment (whose id is '0').
            # Since these are low-level CRUD operations, this method will create a run.
            # To end the run, you'll have to explicitly end it.
            client = MlflowClient()
            experiment_id = "0"
            run = client.create_run(experiment_id)
            print_run_info(run)
            print("--")

            # Log the parameter. Unlike mlflow.log_param this method
            # does not start a run if one does not exist. It will log
            # the parameter in the backend store
            client.log_param(run.info.run_id, "p", 1)
            client.set_terminated(run.info.run_id)
            run = client.get_run(run.info.run_id)
            print_run_info(run)

        .. code-block:: text
            :caption: Output

            run_id: e649e49c7b504be48ee3ae33c0e76c93
            params: {}
            status: RUNNING
            --
            run_id: e649e49c7b504be48ee3ae33c0e76c93
            params: {'p': '1'}
            status: FINISHED
        """
        self._tracking_client.log_param(run_id, key, value)

    def set_experiment_tag(self, experiment_id: str, key: str, value: Any) -> None:
        """
        Set a tag on the experiment with the specified ID. Value is converted to a string.

        :param experiment_id: String ID of the experiment.
        :param key: Name of the tag.
        :param value: Tag value (converted to a string).

        .. code-block:: python
            :caption: Example

            from mlflow.tracking import MlflowClient

            # Create an experiment and set its tag
            client = MlflowClient()
            experiment_id = client.create_experiment("Social Media NLP Experiments")
            client.set_experiment_tag(experiment_id, "nlp.framework", "Spark NLP")

            # Fetch experiment metadata information
            experiment = client.get_experiment(experiment_id)
            print("Name: {}".format(experiment.name))
            print("Tags: {}".format(experiment.tags))

        .. code-block:: text
            :caption: Output

            Name: Social Media NLP Experiments
            Tags: {'nlp.framework': 'Spark NLP'}
        """
        self._tracking_client.set_experiment_tag(experiment_id, key, value)

    def set_tag(self, run_id: str, key: str, value: Any) -> None:
        """
        Set a tag on the run with the specified ID. Value is converted to a string.

        :param run_id: String ID of the run.
        :param key: Tag name (string). This string may only contain alphanumerics,
                    underscores (_), dashes (-), periods (.), spaces ( ), and slashes (/).
                    All backend stores will support keys up to length 250, but some may
                    support larger keys.
        :param value: Tag value (string, but will be string-ified if not).
                      All backend stores will support values up to length 5000, but some
                      may support larger values.

        .. code-block:: python
            :caption: Example

            from mlflow.tracking import MlflowClient

            def print_run_info(run):
                print("run_id: {}".format(run.info.run_id))
                print("Tags: {}".format(run.data.tags))

            # Create a run under the default experiment (whose id is '0').
            client = MlflowClient()
            experiment_id = "0"
            run = client.create_run(experiment_id)
            print_run_info(run)
            print("--")

            # Set a tag and fetch updated run info
            client.set_tag(run.info.run_id, "nlp.framework", "Spark NLP")
            run = client.get_run(run.info.run_id)
            print_run_info(run)

        .. code-block:: text
            :caption: Output

            run_id: 4f226eb5758145e9b28f78514b59a03b
            Tags: {}
            --
            run_id: 4f226eb5758145e9b28f78514b59a03b
            Tags: {'nlp.framework': 'Spark NLP'}
        """
        self._tracking_client.set_tag(run_id, key, value)

    def delete_tag(self, run_id: str, key: str) -> None:
        """
        Delete a tag from a run. This is irreversible.

        :param run_id: String ID of the run
        :param key: Name of the tag

        .. code-block:: python
            :caption: Example

            from mlflow.tracking import MlflowClient

            def print_run_info(run):
                print("run_id: {}".format(run.info.run_id))
                print("Tags: {}".format(run.data.tags))

            # Create a run under the default experiment (whose id is '0').
            client = MlflowClient()
            tags = {"t1": 1, "t2": 2}
            experiment_id = "0"
            run = client.create_run(experiment_id, tags=tags)
            print_run_info(run)
            print("--")

            # Delete tag and fetch updated info
            client.delete_tag(run.info.run_id, "t1")
            run = client.get_run(run.info.run_id)
            print_run_info(run)

        .. code-block:: text
            :caption: Output

            run_id: b7077267a59a45d78cd9be0de4bc41f5
            Tags: {'t2': '2', 't1': '1'}
            --
            run_id: b7077267a59a45d78cd9be0de4bc41f5
            Tags: {'t2': '2'}
        """
        self._tracking_client.delete_tag(run_id, key)

    def log_batch(
        self,
        run_id: str,
        metrics: Sequence[Metric] = (),
        params: Sequence[Param] = (),
        tags: Sequence[RunTag] = (),
    ) -> None:
        """
        Log multiple metrics, params, and/or tags.

        :param run_id: String ID of the run
        :param metrics: If provided, List of Metric(key, value, timestamp) instances.
        :param params: If provided, List of Param(key, value) instances.
        :param tags: If provided, List of RunTag(key, value) instances.

        Raises an MlflowException if any errors occur.
        :return: None

        .. code-block:: python
            :caption: Example

            import time

            from mlflow.tracking import MlflowClient
            from mlflow.entities import Metric, Param, RunTag

            def print_run_info(r):
                print("run_id: {}".format(r.info.run_id))
                print("params: {}".format(r.data.params))
                print("metrics: {}".format(r.data.metrics))
                print("tags: {}".format(r.data.tags))
                print("status: {}".format(r.info.status))

            # Create MLflow entities and a run under the default experiment (whose id is '0').
            timestamp = int(time.time() * 1000)
            metrics = [Metric('m', 1.5, timestamp, 1)]
            params = [Param("p", 'p')]
            tags = [RunTag("t", "t")]
            experiment_id = "0"
            client = MlflowClient()
            run = client.create_run(experiment_id)

            # Log entities, terminate the run, and fetch run status
            client.log_batch(run.info.run_id, metrics=metrics, params=params, tags=tags)
            client.set_terminated(run.info.run_id)
            run = client.get_run(run.info.run_id)
            print_run_info(run)

        .. code-block:: text
            :caption: Output

            run_id: ef0247fa3205410595acc0f30f620871
            params: {'p': 'p'}
            metrics: {'m': 1.5}
            tags: {'t': 't'}
            status: FINISHED
        """
        self._tracking_client.log_batch(run_id, metrics, params, tags)

    def log_artifact(self, run_id, local_path, artifact_path=None) -> None:
        """
        Write a local file or directory to the remote ``artifact_uri``.

        :param local_path: Path to the file or directory to write.
        :param artifact_path: If provided, the directory in ``artifact_uri`` to write to.

        .. code-block:: python
            :caption: Example

            from mlflow.tracking import MlflowClient

            features = "rooms, zipcode, median_price, school_rating, transport"
            with open("features.txt", 'w') as f:
                f.write(features)

            # Create a run under the default experiment (whose id is '0').
            client = MlflowClient()
            experiment_id = "0"
            run = client.create_run(experiment_id)

            # log and fetch the artifact
            client.log_artifact(run.info.run_id, "features.txt")
            artifacts = client.list_artifacts(run.info.run_id)
            for artifact in artifacts:
                print("artifact: {}".format(artifact.path))
                print("is_dir: {}".format(artifact.is_dir))
            client.set_terminated(run.info.run_id)

        .. code-block:: text
            :caption: Output

            artifact: features.txt
            is_dir: False
        """
        self._tracking_client.log_artifact(run_id, local_path, artifact_path)

    def log_artifacts(
        self, run_id: str, local_dir: str, artifact_path: Optional[str] = None
    ) -> None:
        """
        Write a directory of files to the remote ``artifact_uri``.

        :param local_dir: Path to the directory of files to write.
        :param artifact_path: If provided, the directory in ``artifact_uri`` to write to.

        .. code-block:: python
            :caption: Example

            import os
            import json

            # Create some artifacts data to preserve
            features = "rooms, zipcode, median_price, school_rating, transport"
            data = {"state": "TX", "Available": 25, "Type": "Detached"}

            # Create couple of artifact files under the local directory "data"
            os.makedirs("data", exist_ok=True)
            with open("data/data.json", 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            with open("data/features.txt", 'w') as f:
                f.write(features)

            # Create a run under the default experiment (whose id is '0'), and log
            # all files in "data" to root artifact_uri/states
            client = MlflowClient()
            experiment_id = "0"
            run = client.create_run(experiment_id)
            client.log_artifacts(run.info.run_id, "data", artifact_path="states")
            artifacts = client.list_artifacts(run.info.run_id)
            for artifact in artifacts:
                print("artifact: {}".format(artifact.path))
                print("is_dir: {}".format(artifact.is_dir))
            client.set_terminated(run.info.run_id)

        .. code-block:: text
            :caption: Output

            artifact: states
            is_dir: True
        """
        self._tracking_client.log_artifacts(run_id, local_dir, artifact_path)

    @contextlib.contextmanager
    def _log_artifact_helper(self, run_id, artifact_file):
        """
        Yields a temporary path to store a file, and then calls `log_artifact` against that path.

        :param run_id: String ID of the run.
        :param artifact_file: The run-relative artifact file path in posixpath format.
        :return: Temporary path to store a file.
        """
        norm_path = posixpath.normpath(artifact_file)
        filename = posixpath.basename(norm_path)
        artifact_dir = posixpath.dirname(norm_path)
        artifact_dir = None if artifact_dir == "" else artifact_dir

        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = os.path.join(tmp_dir, filename)
            yield tmp_path
            self.log_artifact(run_id, tmp_path, artifact_dir)

    def log_text(self, run_id: str, text: str, artifact_file: str) -> None:
        """
        Log text as an artifact.

        :param run_id: String ID of the run.
        :param text: String containing text to log.
        :param artifact_file: The run-relative artifact file path in posixpath format to which
                              the text is saved (e.g. "dir/file.txt").

        .. code-block:: python
            :caption: Example

            from mlflow.tracking import MlflowClient

            client = MlflowClient()
            run = client.create_run(experiment_id="0")

            # Log text to a file under the run's root artifact directory
            client.log_text(run.info.run_id, "text1", "file1.txt")

            # Log text in a subdirectory of the run's root artifact directory
            client.log_text(run.info.run_id, "text2", "dir/file2.txt")

            # Log HTML text
            client.log_text(run.info.run_id, "<h1>header</h1>", "index.html")
        """
        with self._log_artifact_helper(run_id, artifact_file) as tmp_path:
            with open(tmp_path, "w") as f:
                f.write(text)

    def log_dict(self, run_id: str, dictionary: Any, artifact_file: str) -> None:
        """
        Log a JSON/YAML-serializable object (e.g. `dict`) as an artifact. The serialization
        format (JSON or YAML) is automatically inferred from the extension of `artifact_file`.
        If the file extension doesn't exist or match any of [".json", ".yml", ".yaml"],
        JSON format is used.

        :param run_id: String ID of the run.
        :param dictionary: Dictionary to log.
        :param artifact_file: The run-relative artifact file path in posixpath format to which
                              the dictionary is saved (e.g. "dir/data.json").

        .. code-block:: python
            :caption: Example

            from mlflow.tracking import MlflowClient

            client = MlflowClient()
            run = client.create_run(experiment_id="0")
            run_id = run.info.run_id

            dictionary = {"k": "v"}

            # Log a dictionary as a JSON file under the run's root artifact directory
            client.log_dict(run_id, dictionary, "data.json")

            # Log a dictionary as a YAML file in a subdirectory of the run's root artifact directory
            client.log_dict(run_id, dictionary, "dir/data.yml")

            # If the file extension doesn't exist or match any of [".json", ".yaml", ".yml"],
            # JSON format is used.
            mlflow.log_dict(run_id, dictionary, "data")
            mlflow.log_dict(run_id, dictionary, "data.txt")
        """
        extension = os.path.splitext(artifact_file)[1]

        with self._log_artifact_helper(run_id, artifact_file) as tmp_path:
            with open(tmp_path, "w") as f:
                # Specify `indent` to prettify the output
                if extension in [".yml", ".yaml"]:
                    yaml.dump(dictionary, f, indent=2, default_flow_style=False)
                else:
                    json.dump(dictionary, f, indent=2)

    def log_figure(
        self,
        run_id: str,
        figure: Union["matplotlib.figure.Figure", "plotly.graph_objects.Figure"],
        artifact_file: str,
    ) -> None:
        """
        Log a figure as an artifact. The following figure objects are supported:

        - `matplotlib.figure.Figure`_
        - `plotly.graph_objects.Figure`_

        .. _matplotlib.figure.Figure:
            https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html

        .. _plotly.graph_objects.Figure:
            https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html

        :param run_id: String ID of the run.
        :param figure: Figure to log.
        :param artifact_file: The run-relative artifact file path in posixpath format to which
                              the figure is saved (e.g. "dir/file.png").

        .. code-block:: python
            :caption: Matplotlib Example

            import mlflow
            import matplotlib.pyplot as plt

            fig, ax = plt.subplots()
            ax.plot([0, 1], [2, 3])

            run = client.create_run(experiment_id="0")
            client.log_figure(run.info.run_id, fig, "figure.png")

        .. code-block:: python
            :caption: Plotly Example

            import mlflow
            from plotly import graph_objects as go

            fig = go.Figure(go.Scatter(x=[0, 1], y=[2, 3]))

            run = client.create_run(experiment_id="0")
            client.log_figure(run.info.run_id, fig, "figure.html")
        """

        def _is_matplotlib_figure(fig):
            import matplotlib

            return isinstance(fig, matplotlib.figure.Figure)

        def _is_plotly_figure(fig):
            import plotly

            return isinstance(fig, plotly.graph_objects.Figure)

        with self._log_artifact_helper(run_id, artifact_file) as tmp_path:
            # `is_matplotlib_figure` is executed only when `matplotlib` is found in `sys.modules`.
            # This allows logging a `plotly` figure in an environment where `matplotlib` is not
            # installed.
            if "matplotlib" in sys.modules and _is_matplotlib_figure(figure):
                figure.savefig(tmp_path)
            elif "plotly" in sys.modules and _is_plotly_figure(figure):
                figure.write_html(tmp_path, include_plotlyjs="cdn", auto_open=False)
            else:
                raise TypeError("Unsupported figure object type: '{}'".format(type(figure)))

    def log_image(
        self, run_id: str, image: Union["numpy.ndarray", "PIL.Image.Image"], artifact_file: str
    ) -> None:
        """
        Log an image as an artifact. The following image objects are supported:

        - `numpy.ndarray`_
        - `PIL.Image.Image`_

        .. _numpy.ndarray:
            https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html

        .. _PIL.Image.Image:
            https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image

        Numpy array support
            - data type (( ) represents a valid value range):

                - bool
                - integer (0 ~ 255)
                - unsigned integer (0 ~ 255)
                - float (0.0 ~ 1.0)

                .. warning::

                    - Out-of-range integer values will be **clipped** to [0, 255].
                    - Out-of-range float values will be **clipped** to [0, 1].

            - shape (H: height, W: width):

                - H x W (Grayscale)
                - H x W x 1 (Grayscale)
                - H x W x 3 (an RGB channel order is assumed)
                - H x W x 4 (an RGBA channel order is assumed)

        :param run_id: String ID of the run.
        :param image: Image to log.
        :param artifact_file: The run-relative artifact file path in posixpath format to which
                              the image is saved (e.g. "dir/image.png").

        .. code-block:: python
            :caption: Numpy Example

            import mlflow
            import numpy as np

            image = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)

            run = client.create_run(experiment_id="0")
            client.log_image(run.info.run_id, image, "image.png")

        .. code-block:: python
            :caption: Pillow Example

            import mlflow
            from PIL import Image

            image = Image.new("RGB", (100, 100))

            run = client.create_run(experiment_id="0")
            client.log_image(run.info.run_id, image, "image.png")
        """

        def _is_pillow_image(image):
            from PIL.Image import Image

            return isinstance(image, Image)

        def _is_numpy_array(image):
            import numpy as np

            return isinstance(image, np.ndarray)

        def _normalize_to_uint8(x):
            # Based on: https://github.com/matplotlib/matplotlib/blob/06567e021f21be046b6d6dcf00380c1cb9adaf3c/lib/matplotlib/image.py#L684

            is_int = np.issubdtype(x.dtype, np.integer)
            low = 0
            high = 255 if is_int else 1
            if x.min() < low or x.max() > high:
                msg = (
                    "Out-of-range values are detected. "
                    "Clipping array (dtype: '{}') to [{}, {}]".format(x.dtype, low, high)
                )
                _logger.warning(msg)
                x = np.clip(x, low, high)

            # float or bool
            if not is_int:
                x = x * 255

            return x.astype(np.uint8)

        with self._log_artifact_helper(run_id, artifact_file) as tmp_path:
            if "PIL" in sys.modules and _is_pillow_image(image):
                image.save(tmp_path)
            elif "numpy" in sys.modules and _is_numpy_array(image):
                import numpy as np

                try:
                    from PIL import Image
                except ImportError as exc:
                    raise ImportError(
                        "`log_image` requires Pillow to serialize a numpy array as an image."
                        "Please install it via: pip install Pillow"
                    ) from exc

                # Ref.: https://numpy.org/doc/stable/reference/generated/numpy.dtype.kind.html#numpy-dtype-kind
                valid_data_types = {
                    "b": "bool",
                    "i": "signed integer",
                    "u": "unsigned integer",
                    "f": "floating",
                }

                if image.dtype.kind not in valid_data_types.keys():
                    raise TypeError(
                        "Invalid array data type: '{}'. Must be one of {}".format(
                            image.dtype, list(valid_data_types.values())
                        )
                    )

                if image.ndim not in [2, 3]:
                    raise ValueError(
                        "`image` must be a 2D or 3D array but got a {}D array".format(image.ndim)
                    )

                if (image.ndim == 3) and (image.shape[2] not in [1, 3, 4]):
                    raise ValueError(
                        "Invalid channel length: {}. Must be one of [1, 3, 4]".format(
                            image.shape[2]
                        )
                    )

                # squeeze a 3D grayscale image since `Image.fromarray` doesn't accept it.
                if image.ndim == 3 and image.shape[2] == 1:
                    image = image[:, :, 0]

                image = _normalize_to_uint8(image)

                Image.fromarray(image).save(tmp_path)

            else:
                raise TypeError("Unsupported image object type: '{}'".format(type(image)))

    def _record_logged_model(self, run_id, mlflow_model):
        """
        Record logged model info with the tracking server.

        :param run_id: run_id under which the model has been logged.
        :param mlflow_model: Model info to be recorded.
        """
        self._tracking_client._record_logged_model(run_id, mlflow_model)

    def list_artifacts_(
        self,
        ml_repo_id: str,
        name: str,
        artifact_type: Optional[ArtifactType] = ArtifactType.ARTIFACT,
        max_results: Optional[int] = None,
        page_token: Optional[str] = None,
        offset: Optional[int] = None,
        run_id: Optional[str] = None
    ) -> List[Artifact]:
        return self._tracking_client.list_artifacts_(
            ml_repo_id=ml_repo_id,
            name=name,
            artifact_type=artifact_type,
            max_results=max_results,
            page_token=page_token,
            offset=offset,
            run_id=run_id
        )

    def list_artifacts(self, run_id: str, path=None) -> List[FileInfo]:
        """
        List the artifacts for a run.

        :param run_id: The run to list artifacts from.
        :param path: The run's relative artifact path to list from. By default it is set to None
                     or the root artifact path.
        :return: List of :py:class:`mlflow.entities.FileInfo`

        .. code-block:: python
            :caption: Example

            from mlflow.tracking import MlflowClient

             def print_artifact_info(artifact):
                print("artifact: {}".format(artifact.path))
                print("is_dir: {}".format(artifact.is_dir))
                print("size: {}".format(artifact.file_size))

            features = "rooms zipcode, median_price, school_rating, transport"
            labels = "price"

            # Create a run under the default experiment (whose id is '0').
            client = MlflowClient()
            experiment_id = "0"
            run = client.create_run(experiment_id)

            # Create some artifacts and log under the above run
            for file, content in [("features", features), ("labels", labels)]:
                with open("{}.txt".format(file), 'w') as f:
                    f.write(content)
                client.log_artifact(run.info.run_id, "{}.txt".format(file))

            # Fetch the logged artifacts
            artifacts = client.list_artifacts(run.info.run_id)
            for artifact in artifacts:
                print_artifact_info(artifact)
            client.set_terminated(run.info.run_id)

        .. code-block:: text
            :caption: Output

            artifact: features.txt
            is_dir: False
            size: 53
            artifact: labels.txt
            is_dir: False
            size: 5
        """
        return self._tracking_client.list_artifacts(run_id, path)

    def download_artifacts(self, run_id: str, path: str, dst_path: Optional[str] = None) -> str:
        """
        Download an artifact file or directory from a run to a local directory if applicable,
        and return a local path for it.

        :param run_id: The run to download artifacts from.
        :param path: Relative source path to the desired artifact.
        :param dst_path: Absolute path of the local filesystem destination directory to which to
                         download the specified artifacts. This directory must already exist.
                         If unspecified, the artifacts will either be downloaded to a new
                         uniquely-named directory on the local filesystem or will be returned
                         directly in the case of the LocalArtifactRepository.
        :return: Local path of desired artifact.

        .. code-block:: python
            :caption: Example

            import os
            import mlflow
            from mlflow.tracking import MlflowClient

            features = "rooms, zipcode, median_price, school_rating, transport"
            with open("features.txt", 'w') as f:
                f.write(features)

            # Log artifacts
            with mlflow.start_run() as run:
                mlflow.log_artifact("features.txt", artifact_path="features")

            # Download artifacts
            client = MlflowClient()
            local_dir = "/tmp/artifact_downloads"
            if not os.path.exists(local_dir):
                os.mkdir(local_dir)
            local_path = client.download_artifacts(run.info.run_id, "features", local_dir)
            print("Artifacts downloaded in: {}".format(local_path))
            print("Artifacts: {}".format(os.listdir(local_path)))

        .. code-block:: text
            :caption: Output

            Artifacts downloaded in: /tmp/artifact_downloads/features
            Artifacts: ['features.txt']
        """
        return self._tracking_client.download_artifacts(run_id, path, dst_path)

    def set_terminated(
        self, run_id: str, status: Optional[str] = None, end_time: Optional[int] = None
    ) -> None:
        """Set a run's status to terminated.

        :param status: A string value of :py:class:`mlflow.entities.RunStatus`.
                       Defaults to "FINISHED".
        :param end_time: If not provided, defaults to the current time.

        .. code-block:: python
            :caption: Example

            from mlflow.tracking import MlflowClient

            def print_run_info(r):
                print("run_id: {}".format(r.info.run_id))
                print("status: {}".format(r.info.status))

            # Create a run under the default experiment (whose id is '0').
            # Since this is low-level CRUD operation, this method will create a run.
            # To end the run, you'll have to explicitly terminate it.
            client = MlflowClient()
            experiment_id = "0"
            run = client.create_run(experiment_id)
            print_run_info(run)
            print("--")

            # Terminate the run and fetch updated status. By default,
            # the status is set to "FINISHED". Other values you can
            # set are "KILLED", "FAILED", "RUNNING", or "SCHEDULED".
            client.set_terminated(run.info.run_id, status="KILLED")
            run = client.get_run(run.info.run_id)
            print_run_info(run)

        .. code-block:: text
            :caption: Output

            run_id: 575fb62af83f469e84806aee24945973
            status: RUNNING
            --
            run_id: 575fb62af83f469e84806aee24945973
            status: KILLED
        """
        self._tracking_client.set_terminated(run_id, status, end_time)

    def update_run(self, run_id: str, description: str):
        self._tracking_client.update_run(run_id, description)

    def delete_run(self, run_id: str) -> None:
        """Deletes a run with the given ID.

        :param run_id: The unique run id to delete.

        .. code-block:: python
            :caption: Example

            from mlflow.tracking import MlflowClient

            # Create a run under the default experiment (whose id is '0').
            client = MlflowClient()
            experiment_id = "0"
            run = client.create_run(experiment_id)
            run_id = run.info.run_id
            print("run_id: {}; lifecycle_stage: {}".format(run_id, run.info.lifecycle_stage))
            print("--")
            client.delete_run(run_id)
            del_run = client.get_run(run_id)
            print("run_id: {}; lifecycle_stage: {}".format(run_id, del_run.info.lifecycle_stage))

        .. code-block:: text
            :caption: Output

            run_id: a61c7a1851324f7094e8d5014c58c8c8; lifecycle_stage: active
            run_id: a61c7a1851324f7094e8d5014c58c8c8; lifecycle_stage: deleted
        """
        self._tracking_client.delete_run(run_id)

    def hard_delete_run(self, run_id: str) -> None:
        """
        Hard delete a run along with its artifacts, metrics, params and tags.
        """
        self._tracking_client.hard_delete_run(run_id)

    def restore_run(self, run_id: str) -> None:
        """
        Restores a deleted run with the given ID.

        :param run_id: The unique run id to restore.

        .. code-block:: python
            :caption: Example

            from mlflow.tracking import MlflowClient

            # Create a run under the default experiment (whose id is '0').
            client = MlflowClient()
            experiment_id = "0"
            run = client.create_run(experiment_id)
            run_id = run.info.run_id
            print("run_id: {}; lifecycle_stage: {}".format(run_id, run.info.lifecycle_stage))
            client.delete_run(run_id)
            del_run = client.get_run(run_id)
            print("run_id: {}; lifecycle_stage: {}".format(run_id, del_run.info.lifecycle_stage))
            client.restore_run(run_id)
            rest_run = client.get_run(run_id)
            print("run_id: {}; lifecycle_stage: {}".format(run_id, res_run.info.lifecycle_stage))

        .. code-block:: text
            :caption: Output

            run_id: 7bc59754d7e74534a7917d62f2873ac0; lifecycle_stage: active
            run_id: 7bc59754d7e74534a7917d62f2873ac0; lifecycle_stage: deleted
            run_id: 7bc59754d7e74534a7917d62f2873ac0; lifecycle_stage: active
        """
        self._tracking_client.restore_run(run_id)

    def search_runs(
        self,
        experiment_ids: List[str],
        filter_string: str = "",
        run_view_type: int = ViewType.ACTIVE_ONLY,
        max_results: int = _SEARCH_MAX_RESULTS_DEFAULT,
        order_by: Optional[List[str]] = None,
        page_token: Optional[str] = None,
    ) -> PagedList[Run]:
        """
        Search experiments that fit the search criteria.

        :param experiment_ids: List of experiment IDs, or a single int or string id.
        :param filter_string: Filter query string, defaults to searching all runs.
        :param run_view_type: one of enum values ACTIVE_ONLY, DELETED_ONLY, or ALL runs
                              defined in :py:class:`mlflow.entities.ViewType`.
        :param max_results: Maximum number of runs desired.
        :param order_by: List of columns to order by (e.g., "metrics.rmse"). The ``order_by`` column
                     can contain an optional ``DESC`` or ``ASC`` value. The default is ``ASC``.
                     The default ordering is to sort by ``start_time DESC``, then ``run_id``.
        :param page_token: Token specifying the next page of results. It should be obtained from
            a ``search_runs`` call.

        :return: A :py:class:`PagedList <mlflow.store.entities.PagedList>` of
            :py:class:`Run <mlflow.entities.Run>` objects that satisfy the search expressions.
            If the underlying tracking store supports pagination, the token for the next page may
            be obtained via the ``token`` attribute of the returned object.

        .. code-block:: python
            :caption: Example

            import mlflow
            from mlflow.tracking import MlflowClient
            from mlflow.entities import ViewType

            def print_run_info(runs):
                for r in runs:
                    print("run_id: {}".format(r.info.run_id))
                    print("lifecycle_stage: {}".format(r.info.lifecycle_stage))
                    print("metrics: {}".format(r.data.metrics))

                    # Exclude mlflow system tags
                    tags = {k: v for k, v in r.data.tags.items() if not k.startswith("mlflow.")}
                    print("tags: {}".format(tags))

            # Create an experiment and log two runs with metrics and tags under the experiment
            experiment_id = mlflow.create_experiment("Social NLP Experiments")
            with mlflow.start_run(experiment_id=experiment_id) as run:
                mlflow.log_metric("m", 1.55)
                mlflow.set_tag("s.release", "1.1.0-RC")
            with mlflow.start_run(experiment_id=experiment_id):
                mlflow.log_metric("m", 2.50)
                mlflow.set_tag("s.release", "1.2.0-GA")

            # Search all runs under experiment id and order them by
            # descending value of the metric 'm'
            client = MlflowClient()
            runs = client.search_runs(experiment_id, order_by=["metrics.m DESC"])
            print_run_info(runs)
            print("--")

            # Delete the first run
            client.delete_run(run_id=run.info.run_id)

            # Search only deleted runs under the experiment id and use a case insensitive pattern
            # in the filter_string for the tag.
            filter_string = "tags.s.release ILIKE '%rc%'"
            runs = client.search_runs(experiment_id, run_view_type=ViewType.DELETED_ONLY,
                                        filter_string=filter_string)
            print_run_info(runs)

        .. code-block:: text
            :caption: Output

            run_id: 0efb2a68833d4ee7860a964fad31cb3f
            lifecycle_stage: active
            metrics: {'m': 2.5}
            tags: {'s.release': '1.2.0-GA'}
            run_id: 7ab027fd72ee4527a5ec5eafebb923b8
            lifecycle_stage: active
            metrics: {'m': 1.55}
            tags: {'s.release': '1.1.0-RC'}
            --
            run_id: 7ab027fd72ee4527a5ec5eafebb923b8
            lifecycle_stage: deleted
            metrics: {'m': 1.55}
            tags: {'s.release': '1.1.0-RC'}
        """
        return self._tracking_client.search_runs(
            experiment_ids, filter_string, run_view_type, max_results, order_by, page_token
        )

    def insert_run_logs(self, run_uuid: str, run_logs: List[RunLog]):
        self._tracking_client.insert_run_logs(run_uuid=run_uuid, run_logs=run_logs)

    def get_latest_run_log(self, run_uuid: str, key: str, log_type: str) -> RunLog:
        return self._tracking_client.get_latest_run_log(
            run_uuid=run_uuid, key=key, log_type=log_type
        )

    def list_run_logs(
        self,
        run_uuid: str,
        key: Optional[str] = None,
        log_type: Optional[str] = None,
        steps: Optional[List[int]] = None,
    ) -> List[RunLog]:
        return self._tracking_client.list_run_logs(
            run_uuid=run_uuid, key=key, log_type=log_type, steps=steps
        )

    def get_run_by_fqn(self, fqn: str) -> Run:
        return self._tracking_client.get_run_by_fqn(fqn=fqn)

    def get_run_by_name(
        self,
        run_name:str,
        experiment_id: Optional[str] = None,
        experiment_name: Optional[str] = None,
    ) -> Run:
        return self._tracking_client.get_run_by_name(experiment_id=experiment_id, run_name=run_name, experiment_name=experiment_name)

    # Registry API

    # Registered Model Methods

    def _get_latest_versions(self, name: str, stages: List[str] = None):
        """
        Latest version models for each requests stage. If no ``stages`` provided, returns the
        latest version for each stage.

        :param name: Name of the registered model from which to get the latest versions.
        :param stages: List of desired stages. If input list is None, return latest versions for
                       for ALL_STAGES.
        :return: List of :py:class:`mlflow.entities.model_registry.ModelVersion` objects.

        .. code-block:: python
            :caption: Example

            import mlflow.sklearn
            from mlflow.tracking import MlflowClient
            from sklearn.ensemble import RandomForestRegressor

            def print_models_info(mv):
                for m in mv:
                    print("name: {}".format(m.name))
                    print("latest version: {}".format(m.version))
                    print("run_id: {}".format(m.run_id))
                    print("current_stage: {}".format(m.current_stage))

            mlflow.set_tracking_uri("sqlite:///mlruns.db")

            # Create two runs Log MLflow entities
            with mlflow.start_run() as run1:
                params = {"n_estimators": 3, "random_state": 42}
                rfr = RandomForestRegressor(**params).fit([[0, 1]], [1])
                mlflow.log_params(params)
                mlflow.sklearn.log_model(rfr, artifact_path="sklearn-model")

            with mlflow.start_run() as run2:
                params = {"n_estimators": 6, "random_state": 42}
                rfr = RandomForestRegressor(**params).fit([[0, 1]], [1])
                mlflow.log_params(params)
                mlflow.sklearn.log_model(rfr, artifact_path="sklearn-model")

            # Register model name in the model registry
            name = "RandomForestRegression"
            client = MlflowClient()
            client.create_registered_model(name)

            # Create a two versions of the rfr model under the registered model name
            for run_id in [run1.info.run_id, run2.info.run_id]:
                model_uri = "runs:/{}/sklearn-model".format(run_id)
                mv = client.create_model_version(name, model_uri, run_id)
                print("model version {} created".format(mv.version))

            # Fetch latest version; this will be version 2
            print("--")
            print_models_info(client.get_latest_versions(name, stages=["None"]))

        .. code-block:: text
            :caption: Output

            model version 1 created
            model version 2 created
            --
            name: RandomForestRegression
            latest version: 2
            run_id: 31165664be034dc698c52a4bdeb71663
            current_stage: None
        """
        raise NotImplementedError(
            "This method was deleted intentionally. Please refer to git history to restore it"
        )

    # Model Version Methods

    def _get_model_version_download_uri(self, name: str, version: str) -> str:
        """
        Get the download location in Model Registry for this model version.

        :param name: Name of the containing registered model.
        :param version: Version number as an integer of the model version.
        :return: A single URI location that allows reads for downloading.

        .. code-block:: python
            :caption: Example

            import mlflow.sklearn
            from mlflow.tracking import MlflowClient
            from sklearn.ensemble import RandomForestRegressor

            mlflow.set_tracking_uri("sqlite:///mlruns.db")
            params = {"n_estimators": 3, "random_state": 42}
            name = "RandomForestRegression"
            rfr = RandomForestRegressor(**params).fit([[0, 1]], [1])

            # Log MLflow entities
            with mlflow.start_run() as run:
                mlflow.log_params(params)
                mlflow.sklearn.log_model(rfr, artifact_path="models/sklearn-model")

            # Register model name in the model registry
            client = MlflowClient()
            client.create_registered_model(name)

            # Create a new version of the rfr model under the registered model name
            model_uri = "runs:/{}/models/sklearn-model".format(run.info.run_id)
            mv = client.create_model_version(name, model_uri, run.info.run_id)
            artifact_uri = client.get_model_version_download_uri(name, mv.version)
            print("Download URI: {}".format(artifact_uri))

        .. code-block:: text
            :caption: Output

            Download URI: runs:/44e04097ac364cd895f2039eaccca9ac/models/sklearn-model
        """
        raise NotImplementedError(
            "This method was deleted intentionally. Please refer to git history to restore it"
        )

    # MLFoundry Artifacts Methods

    # TODO (chiragjn): implement list apis for artifacts and models

    def create_artifact_version(
        self,
        experiment_id: Union[int, str],
        artifact_type: ArtifactType,
        name: str,
    ) -> uuid.UUID:
        return self._tracking_client.create_artifact_version(
            experiment_id=experiment_id, artifact_type=artifact_type, name=name
        )

    def create_artifact(
        self,
        experiment_id: Union[int, str],
        artifact_type: ArtifactType,
        name: str,
    ) -> uuid.UUID:
        return self._tracking_client.create_artifact(
            experiment_id=experiment_id, artifact_type=artifact_type, name=name
        )

    def get_artifact_by_id(self, artifact_id: uuid.UUID) -> Artifact:
        return self._tracking_client.get_artifact_by_id(artifact_id=artifact_id)

    def get_artifact_by_fqn(self, fqn: str) -> Artifact:
        return self._tracking_client.get_artifact_by_fqn(fqn=fqn)

    def notify_failure_for_artifact_version(self, version_id: uuid.UUID):
        return self._tracking_client.notify_failure_for_artifact_version(version_id=version_id)

    def list_files_for_artifact_version(
        self, version_id: uuid.UUID, path: Optional[str] = None
    ) -> List[FileInfo]:
        return self._tracking_client.list_files_for_artifact_version(
            version_id=version_id, path=path
        )

    def get_signed_urls_for_artifact_version_read(
        self, version_id: uuid.UUID, paths: List[str]
    ) -> List[SignedURL]:
        return self._tracking_client.get_signed_urls_for_artifact_version_read(
            version_id=version_id, paths=paths
        )

    def get_signed_urls_for_artifact_version_write(
        self, version_id: uuid.UUID, paths: List[str]
    ) -> List[SignedURL]:
        return self._tracking_client.get_signed_urls_for_artifact_version_write(
            version_id=version_id, paths=paths
        )

    def finalize_artifact_version(
        self,
        version_id: uuid.UUID,
        run_uuid: str = None,
        description: Optional[str] = None,
        # this is only `Optional` because argument default should be {}
        artifact_metadata: Optional[Dict[str, Any]] = None,
        data_path: Optional[str] = None,
        step: int = 0,
        artifact_size: Optional[int] = None,
    ) -> ArtifactVersion:
        return self._tracking_client.finalize_artifact_version(
            version_id=version_id,
            run_uuid=run_uuid,
            description=description,
            artifact_metadata=artifact_metadata,
            data_path=data_path,
            step=step,
            artifact_size=artifact_size,
        )

    def get_artifact_version_by_id(self, version_id: uuid.UUID) -> ArtifactVersion:
        return self._tracking_client.get_artifact_version_by_id(version_id=version_id)
    
    def get_artifact_version(self, experiment_id: int, artifact_name: str, version: Optional[int], artifact_type: ArtifactType) -> ArtifactVersion:
        return self._tracking_client.get_artifact_version(
            experiment_id=experiment_id,
            artifact_name=artifact_name,
            version=version,
            artifact_type=artifact_type,
        )

    def get_artifact_version_by_fqn(self, fqn: str) -> ArtifactVersion:
        return self._tracking_client.get_artifact_version_by_fqn(fqn=fqn)

    def update_artifact_version(
        self,
        version_id: uuid.UUID,
        description: Optional[str] = SENTINEL,
        artifact_metadata: Dict[str, Any] = SENTINEL,
    ) -> ArtifactVersion:
        return self._tracking_client.update_artifact_version(
            version_id=version_id, description=description, artifact_metadata=artifact_metadata
        )

    def delete_artifact_version(self, version_id: uuid.UUID):
        return self._tracking_client.delete_artifact_version(version_id=version_id)

    def get_model_by_id(self, model_id: uuid.UUID) -> Model:
        return self._tracking_client.get_model_by_id(model_id=model_id)

    def get_model_by_fqn(self, fqn: str) -> Model:
        return self._tracking_client.get_model_by_fqn(fqn=fqn)

    def get_model_by_name(self, experiment_id: int, name: str) -> Model:
        return self._tracking_client.get_model_by_name(experiment_id=experiment_id, name=name)

    def create_model_version(
        self,
        artifact_version_id: uuid.UUID,
        description: Optional[str] = SENTINEL,
        artifact_metadata: Dict[str, Any] = SENTINEL,
        internal_metadata: Dict[str, Any] = SENTINEL,
        data_path: Optional[str] = SENTINEL,
        step: Optional[int] = SENTINEL,
    ) -> ModelVersion:
        return self._tracking_client.create_model_version(
            artifact_version_id=artifact_version_id,
            description=description,
            artifact_metadata=artifact_metadata,
            internal_metadata=internal_metadata,
            data_path=data_path,
            step=step,
        )

    def get_model_version_by_id(self, version_id: uuid.UUID) -> ModelVersion:
        return self._tracking_client.get_model_version_by_id(version_id=version_id)
    
    def get_model_version(self, experiment_id: int, model_name: str, version: Optional[int]) -> ModelVersion:
        return self._tracking_client.get_model_version(
            experiment_id=experiment_id,
            model_name=model_name,
            version=version
        )

    def get_model_version_by_fqn(self, fqn: str) -> ModelVersion:
        return self._tracking_client.get_model_version_by_fqn(fqn=fqn)

    def update_model_version(
        self,
        version_id: uuid.UUID,
        description: Optional[str] = SENTINEL,
        artifact_metadata: Dict[str, Any] = SENTINEL,
        model_schema: ModelSchema = SENTINEL,
        model_framework: Optional[str] = None,
    ) -> ModelVersion:
        return self._tracking_client.update_model_version(
            version_id=version_id,
            description=description,
            artifact_metadata=artifact_metadata,
            model_schema=model_schema,
            model_framework=model_framework,
        )

    def add_features_to_model_version(
        self, version_id: uuid.UUID, features: List[Feature]
    ) -> ModelVersion:
        return self._tracking_client.add_features_to_model_version(
            version_id=version_id, features=features
        )

    def add_custom_metrics_to_model_version(
        self,
        version_id: uuid.UUID,
        custom_metrics: List[CustomMetric],
    ) -> ModelVersion:
        return self._tracking_client.add_custom_metrics_to_model_version(
            version_id=version_id, custom_metrics=custom_metrics
        )

    def list_artifact_versions(
        self,
        artifact_id: Optional[uuid.UUID] = None,
        max_results: Optional[int] = None,
        page_token: Optional[str] = None,
        artifact_types: Optional[ArtifactType] = None,
        run_ids: Optional[List[str]] = None,
        run_steps: Optional[List[str]] = None,
        include_internal_metadata: Optional[bool] = False,
        offset: Optional[int] = None,
        statuses: Optional[ArtifactVersionStatus] = None,
    ) -> PagedList[ArtifactVersion]:
        return self._tracking_client.list_artifact_versions(
            artifact_id=artifact_id,
            max_results=max_results,
            page_token=page_token,
            artifact_types=artifact_types,
            run_ids=run_ids,
            run_steps=run_steps,
            include_internal_metadata=include_internal_metadata,
            offset=offset,
            statuses=statuses,
        )

    def list_models(
        self,
        ml_repo_id: str,
        name: str,
        max_results: Optional[int] = None,
        page_token: Optional[str] = None,
        offset: Optional[int] = None,
        monitoring_enabled_only: Optional[bool] = False,
    ) -> List[FileInfo]:
        return self._tracking_client.list_models(
            ml_repo_id=ml_repo_id,
            name=name,
            max_results=max_results,
            page_token=page_token,
            offset=offset,
            monitoring_enabled_only=monitoring_enabled_only,
        )

    def list_model_versions(
        self,
        model_id: Optional[uuid.UUID] = None,
        max_results: Optional[int] = None,
        page_token: Optional[str] = None,
        statuses: Optional[ArtifactVersionStatus] = None,
        offset: Optional[int] = None,
        run_ids: Optional[List[str]]=None,
    ) -> PagedList[ModelVersion]:
        return self._tracking_client.list_model_versions(
            model_id=model_id,
            max_results=max_results,
            page_token=page_token,
            offset=offset,
            run_ids=run_ids,
            statuses=statuses,
        )

    def create_multipart_upload(
        self, artifact_version_id: uuid.UUID, path: str, num_parts: int
    ) -> MultiPartUpload:
        return self._tracking_client.create_multipart_upload(
            artifact_version_id=artifact_version_id,
            path=path,
            num_parts=num_parts,
        )

    def authorize_user_for_model(
        self, 
        model_id: uuid.UUID,
        role: str,
    ) -> None:
        return self._tracking_client.authorize_user_for_model(
            model_id=model_id,
            role=role,
        )

    def authorize_user_for_model_version(
        self, 
        version_id: uuid.UUID,
        role: str,
    ):
        return self._tracking_client.authorize_user_for_model_version(
            version_id=version_id, 
            role=role
        )
