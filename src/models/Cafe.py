from src.models.Inventory import Inventory


class CafeMachine:

    def __init__(self, outlets, inventoryDetails, drinks):
        self.outlets = outlets
        self.inventoryDetails = inventoryDetails
        self.drinks = drinks
        self.inventory = None

    def setupInventory(self):
        if self.inventory is None:
            self.inventory = Inventory.getInstance(self.inventoryDetails)

    def serveDrink(self, drink):
        return self.inventory.prepareDrink(drink)
