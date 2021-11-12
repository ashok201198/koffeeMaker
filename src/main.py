from services.CafeMachineServer import CafeMachineServer


def start(instructionsFile):
    instance = CafeMachineServer.getInstance(instructionsFile)
    instance.process()


if __name__ == '__main__':
    instructions = input()
    start(instructions)
