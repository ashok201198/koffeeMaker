from src.services.CafeMachineServer import CafeMachineServer
from src.utils.utils import loadFile

"""
base process to setup and process and tear the application
"""


def base_tester(file):
    instructionsJson = loadFile(file)
    cafeMachineServer = CafeMachineServer()
    cafeMachineServer.start(instructionsJson)
    cafeMachineServer.process()
    success = cafeMachineServer.success_counter
    cafeMachineServer.reset()
    return success


def test_base_case():
    assert base_tester("testdata_sample.json") == 2


def test_no_ingredient_drink():
    assert base_tester("test_no_ingredient_drink.json") == 1


def test_single_outlet():
    assert base_tester("test_single_outlet.json") == 4


def test_no_inventory():
    assert base_tester("test_no_inventory.json") == 0


def test_repetitive_drinks():
    assert base_tester("test_repetitive_drinks.json") == 2


def test_all_cases():
    test_map = dict()
    test_map["test_no_inventory.json"] = 0
    test_map["test_single_outlet.json"] = 4
    test_map["test_no_ingredient_drink.json"] = 1
    test_map["testdata_sample.json"] = 2
    test_map["test_repetitive_drinks.json"] = 2
    for k, v in test_map.items():
        assert base_tester(k) == v
