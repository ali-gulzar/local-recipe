import app.services.clarifai as clarifai_service
from fastapi import APIRouter, File

router = APIRouter()


@router.post("/")
def get_reciepes(image: bytes = File(default=None)):
    ingredient_name = clarifai_service.get_ingredient_name(image)
    print(ingredient_name)
