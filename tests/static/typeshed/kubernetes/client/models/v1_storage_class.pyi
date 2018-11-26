# Stubs for kubernetes.client.models.v1_storage_class (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Dict, List, Optional

class V1StorageClass:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    allow_volume_expansion: Any = ...
    allowed_topologies: Any = ...
    api_version: str = ...
    kind: str = ...
    metadata: Any = ...
    mount_options: Any = ...
    parameters: Any = ...
    provisioner: Any = ...
    reclaim_policy: Any = ...
    volume_binding_mode: Any = ...
    def __init__(self, allow_volume_expansion: Optional[Any] = ..., allowed_topologies: Optional[Any] = ..., api_version: Optional[Any] = ..., kind: Optional[Any] = ..., metadata: Optional[Any] = ..., mount_options: Optional[Any] = ..., parameters: Optional[Any] = ..., provisioner: Optional[Any] = ..., reclaim_policy: Optional[Any] = ..., volume_binding_mode: Optional[Any] = ...) -> None: ...
    @property
    def allow_volume_expansion(self): ...
    @allow_volume_expansion.setter
    def allow_volume_expansion(self, allow_volume_expansion: Any) -> None: ...
    @property
    def allowed_topologies(self): ...
    @allowed_topologies.setter
    def allowed_topologies(self, allowed_topologies: Any) -> None: ...
    @property
    def api_version(self) -> str: ...
    @api_version.setter
    def api_version(self, api_version: str) -> None: ...
    @property
    def kind(self) -> str: ...
    @kind.setter
    def kind(self, kind: str) -> None: ...
    @property
    def metadata(self): ...
    @metadata.setter
    def metadata(self, metadata: Any) -> None: ...
    @property
    def mount_options(self) -> Optional[List[str]]: ...
    @mount_options.setter
    def mount_options(self, mount_options: Optional[List[str]]) -> None: ...
    @property
    def parameters(self) -> Optional[Dict[str, str]]: ...
    @parameters.setter
    def parameters(self, parameters: Optional[Dict[str, str]]) -> None: ...
    @property
    def provisioner(self) -> str: ...
    @provisioner.setter
    def provisioner(self, provisioner: str) -> None: ...
    @property
    def reclaim_policy(self) -> Optional[str]: ...
    @reclaim_policy.setter
    def reclaim_policy(self, reclaim_policy: Optional[str]) -> None: ...
    @property
    def volume_binding_mode(self) -> Optional[str]: ...
    @volume_binding_mode.setter
    def volume_binding_mode(self, volume_binding_mode: Optional[str]) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
