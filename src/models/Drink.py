from src.utils.utils import formatName


class Drink:
    """
    Drink represents a beverage with a name and ingredients required.
    """
    def __init__(self, name: str, ingredients: dict):
        name = formatName(name)
        self.name = name
        self.ingredients = ingredients
