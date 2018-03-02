import time

from TwitterAPI import TwitterAPI


class TwitterController:
    
    def __init__(self):
        consumer_key = 'zBZvvlVi7prqyJ6MbuQSIH0S2'
        consumer_secret='79BdDfHYqjeT6eU2GWKZ0y8Qkl1BufuzA2UndVBdStb5rBz8ia'
        access_token_key='873900949898756096-BiXsfUzbHP4OPNvk85Cmdx9CNi3GLHK'
        access_token_secret='Mq3jhRWszSVj25w3XsnGKwvNM8La72FUakbmyqGzZN9WZ'
        self.api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

    def makeRequests(self,tags):
        if(tags is not list):
            raise ValueError()
        response_collection = []
        for tag in tags:
            response = self.api.request('search/tweets', {'q':tag})
            responce_collection.append(response)
        return response_collection


    def readTagsFromFile(self,filename, column = -1, separator = " "):
        if(filename == None or filename = ""):
            raise ValueError("Filename can not be empty")

        with open(filename) as file:
            content = file.readlines()

        if(column < -1):
            raise ValueError("Selected column must be -1 for all or larger")
        
        tags = []

        for line in content:
            items = line.split(separator)
            if(column == -1):
                tags.extend(items)
            else:
                if(column >= len(items)):
                    raise ValueError("Column is beyond array bounds")
                tags.append(items[column])
        
        return tags

    
                
    






