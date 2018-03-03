import pandas
import numpy
import json
from pandas.io.json import json_normalize
import pandas as pd
#import tensorflow

class StockTrainingModelController:

    def __init__(self):
        self.data_set = []
    
    def createDataSetFromResponse(self,data_collection,format):
        if(format == "json"):
            data = json.loads(data_collection)
            self.data_set = json_normalize(data)
            return self.data_set

    def createDataSetFromFile(self,filename):
        dataframe = pd.read_csv(filename)
        return dataframe
    
    def analyseData(self):
        None

    def createTensorFlowModel():
        None

    def createSentimentModel():
        None
    
    def kmeans(self):
        None

    def svm():
        None



