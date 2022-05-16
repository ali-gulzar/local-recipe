from fastapi import APIRouter, File

import app.models.api as api_model
import app.services.clarifai as clarifai_service
import app.services.database as database_service


router = APIRouter()


@router.post("/", response_model=api_model.Recipes)
def get_reciepes(image: bytes = File(default=None)):
    ingredient_name = clarifai_service.get_ingredient_name(image)
    recipes = [api_model.Recipe.parse_obj(recipe) for recipe in database_service.fetch_recipes(ingredient_name)]
    return api_model.Recipes(ingredient_name=ingredient_name, recipes=recipes)
