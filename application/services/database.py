from deta import Deta
import os

DETA_PROJECT_KEY = os.environ["DETA_PROJECT_KEY"]

def fetch_recipes(ingredient_name: str):
    deta = Deta(DETA_PROJECT_KEY)
    db = deta.Base("recipes")
    query = [{
        "title?contains": ingredient_name,
        "ingredients?contains": ingredient_name
    }]
    response = db.fetch(query)
    recipes = response.items
    return [
        {   
            "title": recipe["title"].capitalize(),
            "ingredients": [item.capitalize() for item in recipe["ingredients"].split("-INGREDIENT-")],
            "steps": [item.capitalize() for item in recipe["steps"].split("-STEP-")],
            "image": recipe["image"]
        }
        for recipe in recipes
    ]