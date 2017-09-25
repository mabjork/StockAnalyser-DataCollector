import time

from TwitterAPI import TwitterAPI
consumer_key='zBZvvlVi7prqyJ6MbuQSIH0S2'
consumer_secret='79BdDfHYqjeT6eU2GWKZ0y8Qkl1BufuzA2UndVBdStb5rBz8ia'
access_token_key='873900949898756096-BiXsfUzbHP4OPNvk85Cmdx9CNi3GLHK'
access_token_secret='Mq3jhRWszSVj25w3XsnGKwvNM8La72FUakbmyqGzZN9WZ'
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

collection = {}
counter = 0
with open("tags.txt") as f:
    content= f.readlines()
    for line in content:
        tags = line.split(" ")
        for tag in tags:
            t = tag.replace("#","")
            r = api.request('search/tweets', {'q':t})
            liste = []
            for item in r:
                print item["text"]
                liste.append(item["text"])
                print " "
            collection[t] = liste
            print counter
            counter+=1
            time.sleep(1)

print collection

#for item in r:
#print(item["text"]
