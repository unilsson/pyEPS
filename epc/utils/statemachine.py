import logging

assertionLogger = logging.getLogger("assertions")

class StateMachine(object):

    def __init__(self):
        self.state = None

    def changeState(self, stateClass):
        if hasattr(self.state, "__exit__"):
            self.state.__exit__()
        self.state = stateClass(self)
        if hasattr(self.state, "__enter__"):
            self.state.__enter__()

    def handleCommand(self, command):
        self.state.handleCommand(command)

    def handleIncomingMessage(self, *args):
        self.state.handleIncomingMessage(*args)


class State(object):

    def handleCommand(self, command, *args, **kwargs):
        def handleUnknownCommand(self, command, *args, **kwargs):
            assertionLogger.info("{} received unknown command: {}({}, {})".format(
                self.__class__.__name__, command, args, kwargs))
        getattr(self, command, handleUnknownCommand)(*args, **kwargs)
