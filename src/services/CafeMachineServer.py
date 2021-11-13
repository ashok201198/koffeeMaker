from concurrent.futures import ThreadPoolExecutor

from src.exceptions.exceptions import ApiException
from src.models.Cafe import CafeMachine
from src.models.Drink import Drink


class CafeMachineServer:
    """
    Creates a singleton instance of the cafe machine server (serves on cafe machine model)
    uses a threadpoolexecutor to handle threads(outlets)
    success_counter & failure_counters just to assert results for tests
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CafeMachineServer, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.cafe = None
        self.executor = None
        self.success_counter = 0
        self.failure_counter = 0

    def start(self, instructionsJson):
        machine = instructionsJson['machine']
        outlet_counter = machine['outlets']['count_n']
        self.cafe = CafeMachine(outlet_counter, machine['total_items_quantity'], machine['beverages'])
        self.executor = ThreadPoolExecutor(outlet_counter)

    def reset(self):
        self.executor.shutdown(wait=False)
        self.cafe.reset()
        self.__setattr__('instance', None)

    # @staticmethod
    # def getInstance(instructionsJson=None):
    #     if CafeMachineServer.instance is None:
    #         CafeMachineServer.instance = CafeMachineServer(instructionsJson)
    #     return CafeMachineServer.instance

    def process(self):
        self.cafe.setupInventory()
        for order_name, ingredients in self.cafe.drinks.items():
            drink = Drink(order_name, ingredients)
            self.serveDrink(drink)

    def serveDrink(self, drink):
        try:
            thread = self.executor.submit(self.cafe.serveDrink, drink)
            if thread.result():
                self.success_counter += 1
                print("{} is prepared".format(drink.name))
        except ApiException as ex:
            print(ex.message)
            self.failure_counter += 1
        except Exception as ignored:
            self.failure_counter += 1
            print(ignored.__repr__())
            print("error preparing {}".format(drink.name))
