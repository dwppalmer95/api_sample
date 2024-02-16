from app1.models import Column
from app1.resource.base import BaseResource
from app1.resource.resource_registry import COLUMN_RESOURCE, register_resource
from app1.resource.versioning import ApiVersion


@register_resource(resource_name=COLUMN_RESOURCE, version_number=ApiVersion.V2)
class ColumnV2(BaseResource[Column]):
    height: float
    width: float

    @classmethod
    def from_model(cls, column: Column) -> "ColumnV2":
        return ColumnV2(version_number=ApiVersion.V2, height=column.height, width=column.width)

