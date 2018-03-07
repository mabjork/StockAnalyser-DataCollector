import numpy as np
import json
from pandas.io.json import json_normalize
import pandas as pd
import scipy
import sklearn
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances

class StockTrainingModelController:

    def __init__(self):
        self.data_set = []
    
    def createDataSetFromResponse(self,data_collection,format):
        if(format == "json"):
            data = json.loads(data_collection)
            self.data_set = json_normalize(data)
            return self.data_set
        
    def loadDataSet(self):
        None

    def createDataSetFromFile(self,filename):
        dataframe = pd.read_csv(filename)
        return dataframe
    
    def analyseData(self):
        None

    def createTensorFlowModel(self):
        None

    def createSentimentModel(self):
        None
    
    def kmeans(self,datapoints,k,maxiter,seed = None):
        if(seed != None):
            np.random.seed(seed)
        
        rand_indices = np.random.randint(len(datapoints),size=k)
        centroids = np.array(datapoints[rand_indices])

        centroids_histroy = []

        for itr in range(maxiter):
            ### Assignment step ###
            distance_matrix = pairwise_distances(datapoints,centroids,metric='sqeuclidian')

            cluster_assignment = np.argmin(distance_matrix,axis=1)
            ### Update step ###
            new_centroids = np.empty([k,2])

            for i in range(k):
                new_centroids[i] = (np.mean(datapoints[cluster_assignment == i],axis=0))

            ### Stop condition ###
            if(np.array_equal(centroids,new_centroids)):
                break
            
            centroids = new_centroids
        
        return centroids,cluster_assignment



    def svm(self):
        None



