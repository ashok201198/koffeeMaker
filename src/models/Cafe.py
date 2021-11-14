from src.exceptions.exceptions import ApiException
from src.models.Inventory import Inventory


class CafeMachine:
    """
    Cafe machine class represents the machine provided in the image with outlets and an inventory(more about it at inventory.py) behind.
    Takes a drink object as an input and forwards it to inventory
    """

    def __init__(self, outlets, inventoryDetails):
        self.outlets = outlets
        self.inventoryDetails = inventoryDetails
        self.inventory = None

    def setupInventory(self):
        self.inventory = Inventory()
        self.inventory.setupInventory(self.inventoryDetails)

    def serveDrink(self, drink):
        try:
            return self.inventory.prepareDrink(drink)
        except ApiException:
            raise

    def reset(self):
        self.inventory.reset()
