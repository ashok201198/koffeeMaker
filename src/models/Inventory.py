from src.models.Drink import Drink
from threading import Lock


class Inventory:
    instance = None

    def __init__(self, materials: dict):
        self.lock = Lock()
        self.materials = materials

    @staticmethod
    def getInstance(materials=None):
        if Inventory.instance is None:
            Inventory.instance = Inventory(materials)
        return Inventory.instance

    def canPrepareDrink(self, drink: Drink):
        for ingredient, quantity in drink.ingredients.items():
            if self.materials.get(ingredient, 0) == 0:
                print("{} can not be prepared because {} is not available".format(drink.name, ingredient))
                return 0
            elif self.materials.get(ingredient, 0) < quantity:
                print("{} can not be prepared because {} is not sufficient".format(drink.name, ingredient))
                return 0
        return 1

    def prepareDrink(self, drink: Drink):
        prepared = False
        with self.lock:
            if self.canPrepareDrink(drink):
                for ingredient, quantity in drink.ingredients.items():
                    self.modifyInventory(ingredient, -1 * quantity)
                prepared = True
        return prepared

    def modifyInventory(self, ingredient, quantity):
        if ingredient not in self.materials:
            self.materials[ingredient] = 0
        self.materials[ingredient] += quantity
