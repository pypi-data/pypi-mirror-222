"""
Internal package providing a Python CRUD interface to MLflow experiments and runs.
This is a lower level API than the :py:mod:`mlflow.tracking.fluent` module, and is
exposed in the :py:mod:`mlflow.tracking` module.
"""

import os
import time
import typing
import uuid
from collections import OrderedDict

from mlflow.entities import (
    SENTINEL,
    Artifact,
    ArtifactType,
    ArtifactVersion,
    CustomMetric,
    ExperimentTag,
    Feature,
    FileInfo,
    Metric,
    Model,
    ModelSchema,
    ModelVersion,
    MultiPartUpload,
    Param,
    Run,
    RunLog,
    RunStatus,
    RunTag,
    SignedURL,
    ViewType,
    ArtifactVersionStatus,
)
from mlflow.exceptions import MlflowException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE, ErrorCode
from mlflow.store.artifact.artifact_repository_registry import get_artifact_repository
from mlflow.store.entities import PagedList
from mlflow.store.tracking import _SEARCH_MAX_RESULTS_DEFAULT
from mlflow.store.tracking.abstract_store import AbstractStore
from mlflow.tracking._tracking_service import utils
from mlflow.utils.mlflow_tags import MLFLOW_USER
from mlflow.utils.string_utils import is_string_type
from mlflow.utils.uri import add_databricks_profile_info_to_artifact_uri
from mlflow.utils.validation import (
    PARAM_VALIDATION_MSG,
    _validate_experiment_artifact_location,
    _validate_experiment_name,
    _validate_metric,
    _validate_param_keys_unique,
    _validate_param_name,
    _validate_run_id,
    _validate_tag_name,
)

TrackingStore = typing.TypeVar("TrackingStore", bound=AbstractStore)


class TrackingServiceClient:
    """
    Client of an MLflow Tracking Server that creates and manages experiments and runs.
    """

    _artifact_repos_cache = OrderedDict()

    def __init__(self, tracking_uri):
        """
        :param tracking_uri: Address of local or remote tracking server.
        """
        self.tracking_uri = tracking_uri
        self._store = utils._get_store(self.tracking_uri)

    @property
    def store(self) -> TrackingStore:
        return self._store

    def get_run(self, run_id):
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
        """
        _validate_run_id(run_id)
        return self.store.get_run(run_id)

    def get_metric_history(self, run_id, key):
        """
        Return a list of metric objects corresponding to all values logged for a given metric.

        :param run_id: Unique identifier for run
        :param key: Metric name within the run

        :return: A list of :py:class:`mlflow.entities.Metric` entities if logged, else empty list
        """
        return self.store.get_metric_history(run_id=run_id, metric_key=key)

    def create_run(self, experiment_id, start_time=None, tags=None, name="", description=None):
        """
        Create a :py:class:`mlflow.entities.Run` object that can be associated with
        metrics, parameters, artifacts, etc.
        Unlike :py:func:`mlflow.projects.run`, creates objects but does not run code.
        Unlike :py:func:`mlflow.start_run`, does not change the "active run" used by
        :py:func:`mlflow.log_param`.

        :param experiment_id: The ID of then experiment to create a run in.
        :param start_time: If not provided, use the current timestamp.
        :param tags: A dictionary of key-value pairs that are converted into
                     :py:class:`mlflow.entities.RunTag` objects.
        :return: :py:class:`mlflow.entities.Run` that was created.
        """

        tags = tags if tags else {}

        # Extract user from tags
        # This logic is temporary; the user_id attribute of runs is deprecated and will be removed
        # in a later release.
        user_id = tags.get(MLFLOW_USER, "unknown")

        return self.store.create_run(
            experiment_id=experiment_id,
            user_id=user_id,
            start_time=start_time or int(time.time() * 1000),
            tags=[RunTag(key, value) for (key, value) in tags.items()],
            name=name,
            description=description,
        )

    def list_run_infos(
        self,
        experiment_id,
        run_view_type=ViewType.ACTIVE_ONLY,
        max_results=_SEARCH_MAX_RESULTS_DEFAULT,
        order_by=None,
        page_token=None,
    ):
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
        """
        return self.store.list_run_infos(
            experiment_id, run_view_type, max_results, order_by, page_token
        )

    def list_experiments(self, view_type=ViewType.ACTIVE_ONLY, max_results=None, page_token=None):
        """
        :param view_type: Qualify requested type of experiments.
        :param max_results: If passed, specifies the maximum number of experiments desired.
                            If not passed, all experiments will be returned for the File and
                            SQLAlchemy backends. For the REST backend, the server will determine
                            an appropriate number of experiments to return.
        :param page_token: Token specifying the next page of results. It should be obtained from
                            a ``list_experiments`` call.
        :return: A :py:class:`PagedList <mlflow.store.entities.PagedList>` of
                 :py:class:`Experiment <mlflow.entities.Experiment>` objects. The pagination token
                 for the next page can be obtained via the ``token`` attribute of the object.
        """
        return self.store.list_experiments(
            view_type=view_type, max_results=max_results, page_token=page_token
        )

    def get_experiment(self, experiment_id):
        """
        :param experiment_id: The experiment ID returned from ``create_experiment``.
        :return: :py:class:`mlflow.entities.Experiment`
        """
        return self.store.get_experiment(experiment_id)

    def get_experiment_by_name(self, name):
        """
        :param name: The experiment name.
        :return: :py:class:`mlflow.entities.Experiment`
        """
        return self.store.get_experiment_by_name(name)

    def create_experiment(self, name, tags=None, description=None, storage_integration_fqn=None):
        """Create an experiment.

        :param name: The experiment name. Must be unique.
        :param description: A description of the experiment.
        :param storage_integration_id: The storage integration ID to use for the experiment for saving artifacts.
        :param tags: A dictionary of key-value pairs that are converted into
                                  :py:class:`mlflow.entities.ExperimentTag` objects.
        :return: Integer ID of the created experiment.
        """
        _validate_experiment_name(name)

        return self.store.create_experiment(
            name=name,
            tags=[ExperimentTag(key, value) for (key, value) in tags.items()] if tags else [],
            description=description,
            storage_integration_fqn=storage_integration_fqn,
        )

    def delete_experiment(self, experiment_id):
        """
        Delete an experiment from the backend store.

        :param experiment_id: The experiment ID returned from ``create_experiment``.
        """
        self.store.delete_experiment(experiment_id)

    def restore_experiment(self, experiment_id):
        """
        Restore a deleted experiment unless permanently deleted.

        :param experiment_id: The experiment ID returned from ``create_experiment``.
        """
        self.store.restore_experiment(experiment_id)

    def rename_experiment(self, experiment_id, new_name):
        """
        Update an experiment's name. The new name must be unique.

        :param experiment_id: The experiment ID returned from ``create_experiment``.
        """
        self.store.rename_experiment(experiment_id, new_name)

    def update_experiment(self, experiment_id, description):
        self.store.update_experiment(experiment_id, description)

    def log_metric(self, run_id, key, value, timestamp=None, step=None):
        """
        Log a metric against the run ID.

        :param run_id: The run id to which the metric should be logged.
        :param key: Metric name (string). This string may only contain alphanumerics,
                    underscores (_), dashes (-), periods (.), spaces ( ), and slashes (/).
                    All backend stores will support keys up to length 250, but some may
                    support larger keys.
        :param value: Metric value (float). Note that some special values such
                      as +/- Infinity may be replaced by other values depending on the store. For
                      example, the SQLAlchemy store replaces +/- Inf with max / min float values.
                      All backend stores will support values up to length 5000, but some
                      may support larger values.
        :param timestamp: Time when this metric was calculated. Defaults to the current system time.
        :param step: Training step (iteration) at which was the metric calculated. Defaults to 0.
        """
        timestamp = timestamp if timestamp is not None else int(time.time() * 1000)
        step = step if step is not None else 0
        _validate_metric(key, value, timestamp, step)
        metric = Metric(key, value, timestamp, step)
        self.store.log_metric(run_id, metric)

    def log_param(self, run_id, key, value):
        """
        Log a parameter against the run ID. Value is converted to a string.
        """
        _validate_param_name(key)
        param = Param(key, str(value))
        try:
            self.store.log_param(run_id, param)
        except MlflowException as e:
            if e.error_code == ErrorCode.Name(INVALID_PARAMETER_VALUE):
                msg = f"{e.message}{PARAM_VALIDATION_MSG}'"
                raise MlflowException(msg, INVALID_PARAMETER_VALUE)
            else:
                raise e

    def set_experiment_tag(self, experiment_id, key, value):
        """
        Set a tag on the experiment with the specified ID. Value is converted to a string.

        :param experiment_id: String ID of the experiment.
        :param key: Name of the tag.
        :param value: Tag value (converted to a string).
        """
        _validate_tag_name(key)
        tag = ExperimentTag(key, str(value))
        self.store.set_experiment_tag(experiment_id, tag)

    def set_tag(self, run_id, key, value):
        """
        Set a tag on the run with the specified ID. Value is converted to a string.

        :param run_id: String ID of the run.
        :param key: Tag name (string). This string may only contain alphanumerics, underscores
                    (_), dashes (-), periods (.), spaces ( ), and slashes (/).
                    All backend stores will support keys up to length 250, but some may
                    support larger keys.
        :param value: Tag value (string, but will be string-ified if not).
                      All backend stores will support values up to length 5000, but some
                      may support larger values.
        """
        _validate_tag_name(key)
        tag = RunTag(key, str(value))
        self.store.set_tag(run_id, tag)

    def delete_tag(self, run_id, key):
        """
        Delete a tag from a run. This is irreversible.

        :param run_id: String ID of the run
        :param key: Name of the tag
        """
        self.store.delete_tag(run_id, key)

    def log_batch(self, run_id, metrics=(), params=(), tags=()):
        """
        Log multiple metrics, params, and/or tags.

        :param run_id: String ID of the run
        :param metrics: If provided, List of Metric(key, value, timestamp) instances.
        :param params: If provided, List of Param(key, value) instances.
        :param tags: If provided, List of RunTag(key, value) instances.

        Raises an MlflowException if any errors occur.
        :return: None
        """
        if len(metrics) == 0 and len(params) == 0 and len(tags) == 0:
            return
        if len(params) > 1:
            _validate_param_keys_unique(params)
        for metric in metrics:
            _validate_metric(metric.key, metric.value, metric.timestamp, metric.step)
        for param in params:
            _validate_param_name(param.key)
        for tag in tags:
            _validate_tag_name(tag.key)
        self.store.log_batch(run_id=run_id, metrics=metrics, params=params, tags=tags)

    def _record_logged_model(self, run_id, mlflow_model):
        from mlflow.models import Model

        if not isinstance(mlflow_model, Model):
            raise TypeError(
                "Argument 'mlflow_model' should be of type mlflow.models.Model but was "
                "{}".format(type(mlflow_model))
            )
        self.store.record_logged_model(run_id, mlflow_model)

    def _get_artifact_repo(self, run_id):
        # Attempt to fetch the artifact repo from a local cache
        cached_repo = TrackingServiceClient._artifact_repos_cache.get(run_id)
        if cached_repo is not None:
            return cached_repo
        else:
            run = self.get_run(run_id)
            artifact_uri = add_databricks_profile_info_to_artifact_uri(
                run.info.artifact_uri, self.tracking_uri
            )
            artifact_repo = get_artifact_repository(artifact_uri)
            # Cache the artifact repo to avoid a future network call, removing the oldest
            # entry in the cache if there are too many elements
            if len(TrackingServiceClient._artifact_repos_cache) > 1024:
                TrackingServiceClient._artifact_repos_cache.popitem(last=False)
            TrackingServiceClient._artifact_repos_cache[run_id] = artifact_repo
            return artifact_repo

    def log_artifact(self, run_id, local_path, artifact_path=None):
        """
        Write a local file or directory to the remote ``artifact_uri``.

        :param local_path: Path to the file or directory to write.
        :param artifact_path: If provided, the directory in ``artifact_uri`` to write to.
        """
        artifact_repo = self._get_artifact_repo(run_id)
        if os.path.isdir(local_path):
            dir_name = os.path.basename(os.path.normpath(local_path))
            path_name = (
                os.path.join(artifact_path, dir_name) if artifact_path is not None else dir_name
            )
            artifact_repo.log_artifacts(local_path, path_name)
        else:
            artifact_repo.log_artifact(local_path, artifact_path)

    def log_artifacts(self, run_id, local_dir, artifact_path=None):
        """
        Write a directory of files to the remote ``artifact_uri``.

        :param local_dir: Path to the directory of files to write.
        :param artifact_path: If provided, the directory in ``artifact_uri`` to write to.
        """
        self._get_artifact_repo(run_id).log_artifacts(local_dir, artifact_path)

    def list_artifacts_(
        self,
        ml_repo_id: str,
        name: str,
        artifact_type: typing.Optional[ArtifactType] = ArtifactType.ARTIFACT,
        max_results: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        run_id: typing.Optional[str] = None
    ):
        return self.store.list_artifacts(
            experiment_id=ml_repo_id, 
            name=name, 
            artifact_types=[artifact_type],
            max_results=max_results,
            page_token=page_token,
            offset=offset,
            run_id=run_id
        )

    def list_artifacts(self, run_id, path=None):
        """
        List the artifacts for a run.

        :param run_id: The run to list artifacts from.
        :param path: The run's relative artifact path to list from. By default it is set to None
                     or the root artifact path.
        :return: List of :py:class:`mlflow.entities.FileInfo`
        """
        return self._get_artifact_repo(run_id).list_artifacts(path)

    def download_artifacts(self, run_id, path, dst_path=None):
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
        """
        return self._get_artifact_repo(run_id).download_artifacts(path, dst_path)

    def set_terminated(self, run_id, status=None, end_time=None):
        """Set a run's status to terminated.

        :param status: A string value of :py:class:`mlflow.entities.RunStatus`.
                       Defaults to "FINISHED".
        :param end_time: If not provided, defaults to the current time."""
        end_time = end_time if end_time else int(time.time() * 1000)
        status = status if status else RunStatus.to_string(RunStatus.FINISHED)
        self.store.update_run_info(
            run_id,
            run_status=RunStatus.from_string(status),
            end_time=end_time,
        )

    def update_run(self, run_id: str, description: str):
        self.store.update_run_info(run_id, description=description)

    def delete_run(self, run_id):
        """
        Deletes a run with the given ID.
        """
        self.store.delete_run(run_id)

    def hard_delete_run(self, run_id):
        """
        Hard delete a run along with its artifacts, metrics, params and tags.
        """
        self.store.hard_delete_run(run_id)

    def restore_run(self, run_id):
        """
        Restores a deleted run with the given ID.
        """
        self.store.restore_run(run_id)

    def search_runs(
        self,
        experiment_ids,
        filter_string="",
        run_view_type=ViewType.ACTIVE_ONLY,
        max_results=_SEARCH_MAX_RESULTS_DEFAULT,
        order_by=None,
        page_token=None,
    ):
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
        """
        if isinstance(experiment_ids, int) or is_string_type(experiment_ids):
            experiment_ids = [experiment_ids]
        return self.store.search_runs(
            experiment_ids=experiment_ids,
            filter_string=filter_string,
            run_view_type=run_view_type,
            max_results=max_results,
            order_by=order_by,
            page_token=page_token,
        )

    def insert_run_logs(self, run_uuid: str, run_logs: typing.List[RunLog]):
        self.store.insert_run_logs(run_uuid=run_uuid, run_logs=run_logs)

    def get_latest_run_log(self, run_uuid: str, key: str, log_type: str) -> RunLog:
        return self.store.get_latest_run_log(run_uuid=run_uuid, key=key, log_type=log_type)

    def list_run_logs(
        self,
        run_uuid: str,
        key: typing.Optional[str] = None,
        log_type: typing.Optional[str] = None,
        steps: typing.Optional[typing.List[int]] = None,
    ) -> typing.List[RunLog]:
        return self.store.list_run_logs(run_uuid=run_uuid, key=key, log_type=log_type, steps=steps)

    def get_run_by_fqn(self, fqn: str) -> Run:
        return self.store.get_run_by_fqn(fqn=fqn)

    def get_run_by_name(
        self,
        run_name:str,
        experiment_id: typing.Optional[str] = None,
        experiment_name: typing.Optional[str] = None,
    ) -> Run:
        return self.store.get_run_by_name(experiment_id=experiment_id, run_name=run_name, experiment_name=experiment_name)

    # Mlfoundry Artifacts methods
    # TODO (chiragjn): consider moving these to another mlfoundry_artifacts_service/client.py
    # TODO (chiragjn): implement list apis for artifacts and models

    def create_artifact_version(
        self,
        experiment_id: typing.Union[int, str],
        artifact_type: ArtifactType,
        name: str,
    ) -> uuid.UUID:
        return self.store.create_artifact_version(
            experiment_id=experiment_id, artifact_type=artifact_type, name=name
        )

    def create_artifact(
        self,
        experiment_id: typing.Union[int, str],
        artifact_type: ArtifactType,
        name: str,
    ) -> uuid.UUID:
        return self.store.create_artifact(
            experiment_id=experiment_id, artifact_type=artifact_type, name=name
        )

    def get_artifact_by_id(self, artifact_id: uuid.UUID) -> Artifact:
        return self.store.get_artifact_by_id(artifact_id=artifact_id)

    def get_artifact_by_fqn(self, fqn: str) -> Artifact:
        return self.store.get_artifact_by_fqn(fqn=fqn)

    def notify_failure_for_artifact_version(self, version_id: uuid.UUID):
        return self.store.notify_failure_for_artifact_version(version_id=version_id)

    def list_files_for_artifact_version(
        self, version_id: uuid.UUID, path: typing.Optional[str] = None
    ) -> typing.List[FileInfo]:
        return self.store.list_files_for_artifact_version(version_id=version_id, path=path)

    def get_signed_urls_for_artifact_version_read(
        self, version_id: uuid.UUID, paths: typing.List[str]
    ) -> typing.List[SignedURL]:
        return self.store.get_signed_urls_for_artifact_version_read(
            version_id=version_id, paths=paths
        )

    def get_signed_urls_for_artifact_version_write(
        self, version_id: uuid.UUID, paths: typing.List[str]
    ) -> typing.List[SignedURL]:
        return self.store.get_signed_urls_for_artifact_version_write(
            version_id=version_id, paths=paths
        )

    def finalize_artifact_version(
        self,
        version_id: uuid.UUID,
        run_uuid: str,
        description: typing.Optional[str] = None,
        # this is only `Optional` because argument default should be {}
        artifact_metadata: typing.Optional[typing.Dict[str, typing.Any]] = None,
        data_path: typing.Optional[str] = None,
        step: int = 0,
        artifact_size: typing.Optional[int] = None,
    ) -> ArtifactVersion:
        return self.store.finalize_artifact_version(
            version_id=version_id,
            run_uuid=run_uuid,
            description=description,
            artifact_metadata=artifact_metadata,
            data_path=data_path,
            step=step,
            artifact_size=artifact_size,
        )

    def get_artifact_version_by_id(self, version_id: uuid.UUID) -> ArtifactVersion:
        return self.store.get_artifact_version_by_id(version_id=version_id)
    
    def get_artifact_version(self, experiment_id: int, artifact_name: str, version: typing.Optional[int], artifact_type: ArtifactType) -> ArtifactVersion:
        return self.store.get_artifact_version(
            experiment_id=experiment_id,
            artifact_name=artifact_name,
            version=version,
            artifact_type=artifact_type,
        )

    def get_artifact_version_by_fqn(self, fqn: str) -> ArtifactVersion:
        return self.store.get_artifact_version_by_fqn(fqn=fqn)

    def update_artifact_version(
        self,
        version_id: uuid.UUID,
        description: typing.Optional[str] = SENTINEL,
        artifact_metadata: typing.Dict[str, typing.Any] = SENTINEL,
    ) -> ArtifactVersion:
        return self.store.update_artifact_version(
            version_id=version_id, description=description, artifact_metadata=artifact_metadata
        )

    def delete_artifact_version(self, version_id: uuid.UUID):
        return self.store.delete_artifact_version(version_id=version_id)

    def get_model_by_id(self, model_id: uuid.UUID) -> Model:
        return self.store.get_model_by_id(model_id=model_id)

    def get_model_by_fqn(self, fqn: str) -> Model:
        return self.store.get_model_by_fqn(fqn=fqn)

    def get_model_by_name(self, experiment_id: int, name: str) -> Model:
        return self.store.get_model_by_name(experiment_id=experiment_id, name=name)

    def create_model_version(
        self,
        artifact_version_id: uuid.UUID,
        description: typing.Optional[str] = SENTINEL,
        artifact_metadata: typing.Dict[str, typing.Any] = SENTINEL,
        internal_metadata: typing.Dict[str, typing.Any] = SENTINEL,
        data_path: typing.Optional[str] = SENTINEL,
        step: typing.Optional[int] = SENTINEL,
    ) -> ModelVersion:
        return self.store.create_model_version(
            artifact_version_id=artifact_version_id,
            description=description,
            artifact_metadata=artifact_metadata,
            internal_metadata=internal_metadata,
            data_path=data_path,
            step=step,
        )

    def get_model_version_by_id(self, version_id: uuid.UUID) -> ModelVersion:
        return self.store.get_model_version_by_id(version_id=version_id)
    
    def get_model_version(self, experiment_id: int, model_name: str, version: typing.Optional[int]) -> ModelVersion:
        return self.store.get_model_version(
            experiment_id=experiment_id,
            model_name=model_name,
            version=version
        )

    def get_model_version_by_fqn(self, fqn: str) -> ModelVersion:
        return self.store.get_model_version_by_fqn(fqn=fqn)

    def update_model_version(
        self,
        version_id: uuid.UUID,
        description: typing.Optional[str] = SENTINEL,
        artifact_metadata: typing.Dict[str, typing.Any] = SENTINEL,
        model_schema: ModelSchema = SENTINEL,
        model_framework: typing.Optional[str] = None,
    ) -> ModelVersion:
        return self.store.update_model_version(
            version_id=version_id,
            description=description,
            artifact_metadata=artifact_metadata,
            model_schema=model_schema,
            model_framework=model_framework,
        )

    def add_features_to_model_version(
        self, version_id: uuid.UUID, features: typing.List[Feature]
    ) -> ModelVersion:
        return self.store.add_features_to_model_version(version_id=version_id, features=features)

    def add_custom_metrics_to_model_version(
        self,
        version_id: uuid.UUID,
        custom_metrics: typing.List[CustomMetric],
    ) -> ModelVersion:
        return self.store.add_custom_metrics_to_model_version(
            version_id=version_id, custom_metrics=custom_metrics
        )

    def list_artifact_versions(
        self,
        artifact_id: typing.Optional[uuid.UUID] = None,
        max_results: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        artifact_types: typing.Optional[ArtifactType] = None,
        run_ids: typing.Optional[typing.List[str]] = None,
        run_steps: typing.Optional[typing.List[str]] = None,
        include_internal_metadata: typing.Optional[bool] = False,
        offset: typing.Optional[int] = None,
        statuses: typing.Optional[ArtifactVersionStatus] = None,
    ) -> PagedList[ArtifactVersion]:
        return self.store.list_artifact_versions(
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
        max_results: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        monitoring_enabled_only: typing.Optional[bool] = False,
    ):
        return self.store.list_models(
            experiment_id=ml_repo_id,
            name=name,
            max_results=max_results,
            page_token=page_token,
            offset=offset,
            monitoring_enabled_only=monitoring_enabled_only,
        )

    def list_model_versions(
        self,
        model_id: typing.Optional[uuid.UUID] = None,
        max_results: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        statuses: typing.Optional[ArtifactVersionStatus] = None,
        offset: typing.Optional[int] = None,
        run_ids: typing.Optional[typing.List[str]]=None,
    ) -> PagedList[ModelVersion]:
        return self.store.list_model_versions(
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
        return self.store.create_multipart_upload(
            artifact_version_id=artifact_version_id,
            path=path,
            num_parts=num_parts,
        )

    def authorize_user_for_model(
        self, 
        model_id: uuid.UUID,
        role: str,
    ):
        return self.store.authorize_user_for_model(
            model_id=model_id, 
            role=role
        )

    def authorize_user_for_model_version(
        self, 
        version_id: uuid.UUID,
        role: str,
    ):
        return self.store.authorize_user_for_model_version(
            version_id=version_id, 
            role=role
        )