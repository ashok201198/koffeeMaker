import json
from src.models.Cafe import CafeMachine
from concurrent.futures import ThreadPoolExecutor
from src.models.Drink import Drink
from src.utils.utils import array_on_duplicate_keys


class CafeMachineServer:
    instance = None

    def __init__(self, instructionsFile):
        with open(instructionsFile, "r") as file:
            instructionJson = json.loads(file.read(), object_pairs_hook=array_on_duplicate_keys)
        machine = instructionJson['machine']
        outlet_counter = machine['outlets']['count_n']
        self.cafe = CafeMachine(outlet_counter, machine['total_items_quantity'], machine['beverages'])
        self.executor = ThreadPoolExecutor(outlet_counter)

    @staticmethod
    def getInstance(instructionsFile=None):
        if CafeMachineServer.instance is None:
            CafeMachineServer.instance = CafeMachineServer(instructionsFile)
        return CafeMachineServer.instance

    def process(self):
        self.cafe.setupInventory()
        for order_name, ingredients in self.cafe.drinks.items():
            if isinstance(ingredients, list):
                for order in ingredients:
                    drink = Drink(order_name, order)
                    self.serveDrink(drink)
            else:
                drink = Drink(order_name, ingredients)
                self.serveDrink(drink)

    def serveDrink(self, drink):
        thread = self.executor.submit(self.cafe.serveDrink, drink)
        if thread.done() and thread.result():
            print("{} is prepared".format(drink.name))
