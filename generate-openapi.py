import json

from fastapi.openapi.utils import get_openapi

from main import app

print(
    json.dumps(
        get_openapi(
            title=app.title,
            version=app.version,
            openapi_version=app.openapi_version,
            description=app.description,
            routes=app.routes,
        ),
        indent=4,
    )
)
