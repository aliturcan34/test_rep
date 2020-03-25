#custom errors for wager

class SmallerThan5(Exception):
    def __init__(self, message):
        self.message = message

class ChipOverFlow(Exception):
    def __init__(self, message):
        self.message = message
