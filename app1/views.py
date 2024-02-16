from http import HTTPStatus
from typing import Optional, Union

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View

from app1.models import Column
from app1.resource.base import BaseResource
from app1.resource.resource_registry import get_resource, COLUMN_RESOURCE
from app1.resource.v1 import ColumnV1
from app1.resource.v2 import ColumnV2
from app1.resource.versioning import ApiVersion, VersionResource


class ExampleView(View):
    def get(self, request: HttpRequest):
        version: ApiVersion = request.GET.get("version", ApiVersion.V2)
        id: Optional[int] = request.GET.get("id", None)

        if id is None:
            return HttpResponse("Provide a column id", status=HTTPStatus.NOT_FOUND)
        column: Column = get_object_or_404(Column, id=id)

        try:
            version_resource: VersionResource = VersionResource(version=version)
        except ValueError:
            return HttpResponse("Invalid version parameter.", status=HTTPStatus.NOT_FOUND)

        resource: BaseResource = get_resource(COLUMN_RESOURCE, version_resource.version)

        return HttpResponse(content=resource.from_model(model=column).model_dump_json(),
                            content_type="application/json")

    def post(self, request: HttpRequest):
        version_resource: VersionResource = VersionResource.model_validate_json(request.body)

        column: Union[ColumnV1, ColumnV2]
        if version_resource.version == ApiVersion.V1:
            column = ColumnV1.model_validate_json(request.body)
            Column.objects.create(height=column.height)
        else:
            column = ColumnV2.model_validate_json(request.body)
            Column.objects.create(height=column.height, width=column.width)

        resource: BaseResource = get_resource(COLUMN_RESOURCE, version_resource.version)
        return HttpResponse(content=resource.from_model(model=column).model_dump_json(),
                            content_type="application/json")
