from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

import app.controllers.recipe as recipe_controller
import app.models.api as api_models

API_RESPONSES = {
    status.HTTP_400_BAD_REQUEST: {"model": api_models.Error},
    status.HTTP_403_FORBIDDEN: {"model": api_models.Error},
    status.HTTP_422_UNPROCESSABLE_ENTITY: {"description": "n/a"},
    status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": api_models.Error},
}

fastapi_app = FastAPI(
    title="Local Recipe API",
    description="API to find local recipes for unknown ingredients",
    responses=API_RESPONSES,
    openapi_url="/local/openapi.json",
)

fastapi_app.include_router(recipe_controller.router, tags=["Recipes"])


# Used to generate openapi
@fastapi_app.get("/openapi.json", include_in_schema=False)
def get_openapi():
    return fastapi_app.openapi()


@fastapi_app.exception_handler(RequestValidationError)
def request_validation_exception_handler(request, e):
    return JSONResponse({"message": str(e)}, status_code=status.HTTP_400_BAD_REQUEST)


@fastapi_app.exception_handler(Exception)
def exception_handler(request, e):
    return JSONResponse(
        {"message": str(e).splitlines()},
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
