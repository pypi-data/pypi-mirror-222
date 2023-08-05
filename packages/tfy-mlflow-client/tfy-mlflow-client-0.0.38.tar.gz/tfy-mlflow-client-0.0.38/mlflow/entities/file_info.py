from mlflow.entities._mlflow_object import _MLflowObject
from mlflow.protos.service_pb2 import FileInfo as ProtoFileInfo


class FileInfo(_MLflowObject):
    """
    Metadata about a file or directory.
    """

    def __init__(self, path, is_dir, file_size, signed_url=None):
        self._path = path
        self._is_dir = is_dir
        self._bytes = file_size
        self._signed_url = signed_url

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    @property
    def path(self):
        """String path of the file or directory."""
        return self._path

    @property
    def is_dir(self):
        """Whether the FileInfo corresponds to a directory."""
        return self._is_dir

    @property
    def file_size(self):
        """Size of the file or directory. If the FileInfo is a directory, returns None."""
        return self._bytes

    @property
    def signed_url(self):
        """Signed url to read the file. If the FileInfo is a directory or comes from non s3 store, returns None"""
        return self._signed_url

    def to_proto(self):
        proto = ProtoFileInfo()
        proto.path = self.path
        proto.is_dir = self.is_dir
        if self.file_size:
            proto.file_size = self.file_size
        if self.signed_url:
            proto.signed_url = self.signed_url
        return proto

    @classmethod
    def from_proto(cls, proto):
        signed_url = proto.signed_url if proto.HasField("signed_url") else None
        return cls(proto.path, proto.is_dir, proto.file_size, signed_url=signed_url)
