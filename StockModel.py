import pandas
import numpy
import json
from pandas.io.json import json_normalize
import pandas as pd
import tensorflow

class StockModelController:

    def __init__(self):
        self.data_set = []
    
    def createDataSet(self,data_collection,format):
        if(format == "json"):
            data = json.loads(data_collection)
            self.data_set = json_normalize(data)
    
    def analyseData(self):
        None

    def createTensorFlowModel():
        None

    def createSentimentModel():
        None

    
            

