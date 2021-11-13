from src.exceptions.exceptions import NoIngredientsFoundException, InsufficientIngredientsException, \
    UnavailableIngredientException, ApiException
from src.models.Drink import Drink
from threading import Lock


class Inventory:
    """
    Inventory class creates a singleton instance to represent inventory details. Lock is used to acheive synchronization
    between threads accessing the inventory at the same time.
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Inventory, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.lock = Lock()
        self.materials = None

    def setupInventory(self, materials):
        self.materials = materials

    """
    Checks up the inventory materials and returns True if drink can be made, else raised the required Exceptions.
    """

    def canPrepareDrink(self, drink: Drink):
        if drink.ingredients is None or len(drink.ingredients) == 0:
            raise NoIngredientsFoundException(drink)
        print(self.materials)
        for ingredient, quantity in drink.ingredients.items():
            if self.materials.get(ingredient, 0) == 0:
                raise UnavailableIngredientException(drink, ingredient)
            elif self.materials.get(ingredient, 0) < quantity:
                raise InsufficientIngredientsException(drink, ingredient)
        return True

    """
    Checks & deducts the inventory materials and returns True if drink can be made, else raised the required Exceptions.
    """

    def prepareDrink(self, drink: Drink):
        with self.lock:
            try:
                if self.canPrepareDrink(drink):
                    for ingredient, quantity in drink.ingredients.items():
                        self.materials[ingredient] -= quantity
            except ApiException:
                raise
        return True

    def modifyInventory(self, ingredient, quantity):
        if ingredient not in self.materials:
            self.materials[ingredient] = 0
        self.materials[ingredient] += quantity

    """
    Just to provide a reset mechanism
    """

    def reset(self):
        self.__setattr__('instance', None)
        self.materials = None
