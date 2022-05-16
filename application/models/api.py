from typing import List, Optional

from pydantic import BaseModel


class Error(BaseModel):
    message: str


class Recipe(BaseModel):
    title: str
    ingredients: List[str]
    steps: List[str]
    image: str


class Recipes(BaseModel):
    ingredient_name: str
    recipes: Optional[List[Recipe]]
