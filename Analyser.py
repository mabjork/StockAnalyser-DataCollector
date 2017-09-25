from Equity import Equity
import tensorflow

class AnalyserController(object):

    def __init__(self, data):
        self.data = data

    def startAnalaysing(self):
        for equity in self.data:
