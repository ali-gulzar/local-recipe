from fastapi import APIRouter, UploadFile

import application.models.api as api_model
import application.services.clarifai as clarifai_service
import application.services.database as database_service


router = APIRouter()


@router.post("/", response_model=api_model.Recipes)
async def get_reciepes(image: UploadFile):
    image_bytes = await image.read()
    ingredient_name = clarifai_service.get_ingredient_name(image_bytes)
    recipes = [api_model.Recipe.parse_obj(recipe) for recipe in database_service.fetch_recipes(ingredient_name)]
    return api_model.Recipes(ingredient_name=ingredient_name, recipes=recipes)
