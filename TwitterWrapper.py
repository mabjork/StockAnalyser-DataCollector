import time
from TwitterAPI import TwitterAPI
import json


class TwitterController(object):
    
    def __init__(self):
        consumer_key = 'zBZvvlVi7prqyJ6MbuQSIH0S2'
        consumer_secret='79BdDfHYqjeT6eU2GWKZ0y8Qkl1BufuzA2UndVBdStb5rBz8ia'
        access_token_key='873900949898756096-BiXsfUzbHP4OPNvk85Cmdx9CNi3GLHK'
        access_token_secret='Mq3jhRWszSVj25w3XsnGKwvNM8La72FUakbmyqGzZN9WZ'
        self.api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

    def makeRequests(self,tags):
        if(not isinstance(tags,list)):
            raise ValueError("Tags must be instanceof list")
        response_collection = []
        for tag in tags:
            response = self.api.request('search/tweets', {'q':tag})
            response_collection.append(response.text)
        return response_collection

    def makeSingleRequest(self,tag):
        if(tag == None or tag ==""):
            raise ValueError("Must supply a tag")
        response = self.api.request('search/tweets', {'q':tag})
        return response.text


    def makeTagsFromSymbols(self,symbols,tag = "#"):
        if(not isinstance(symbols,list)):
            raise ValueError("Symbols must be a list")
        return map(lambda x : tag + x , symbols)
    
    def readTagsFromFile(self,filename, column = -1, separator = " "):
        if(filename == None or filename == ""):
            raise ValueError("Filename can not be empty")

        with open(filename) as file:
            content = file.readlines()

        if(column < -1):
            raise ValueError("Selected column must be -1 for all or larger")
        
        tags = []

        for line in content:
            items = line.split(separator)
            if(column == -1):
                items = map(lambda x : x.replace("\n",""),items)
                tags.extend(items)
            else:
                if(column >= len(items)):
                    raise ValueError("Column is beyond array bounds")
                item = items[column].replace("\n","")
                tags.append(items[column])
        
        return tags
    
    def extractTwitText(self,data):
        serialized_data = json.loads(data)

        statuses = serialized_data["statuses"]

        texts = []

        for status in statuses:
            text = status["text"]
            texts.append(text)

        return texts
            

        



    
                
    






