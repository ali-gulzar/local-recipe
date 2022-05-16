import json

from fastapi.openapi.utils import get_openapi

from main import fastapi_app

print(
    json.dumps(
        get_openapi(
            title=fastapi_app.title,
            version=fastapi_app.version,
            openapi_version=fastapi_app.openapi_version,
            description=fastapi_app.description,
            routes=fastapi_app.routes,
        ),
        indent=4,
    )
)
