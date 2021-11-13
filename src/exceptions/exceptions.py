from src.models.Drink import Drink


class ApiException(Exception):
    """Base Exception class"""
    def __init__(self, message="Exception!!!"):
        self.message = message


class NoIngredientsFoundException(ApiException):
    """Exception raised when no ingredients are found for a drink"""
    def __init__(self, drink: Drink = None, message="{} has no ingredients found"):
        self.message = message.format(drink.name)


class InsufficientIngredientsException(ApiException):
    """Exception raised when a drink can't be prepared due to less ingredients"""
    def __init__(self, drink: Drink = None, ingredient=None,
                 message="{} can not be prepared because {} is not sufficient"):
        self.message = message.format(drink.name, ingredient)


class UnavailableIngredientException(ApiException):
    """Exception raised when ingredient required is not available"""
    def __init__(self, drink: Drink = None, ingredient=None,
                 message="{} can not be prepared because {} is not available"):
        self.message = message.format(drink.name, ingredient)
