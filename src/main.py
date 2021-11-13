from services.CafeMachineServer import CafeMachineServer
from src.utils.utils import loadFile


def start(instructionsFile):
    instructionJson = loadFile(instructionsFile)
    instance = CafeMachineServer()
    instance.start(instructionJson)
    instance.process()
    # instance.reset()


"""
Main class to start the application
params:
Instructions: input -> provide the file path 
"""
if __name__ == '__main__':
    instructions = input()
    start(instructions)
