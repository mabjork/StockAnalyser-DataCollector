import re

class TwitterAnalyserController(object):

    def __init__(self):
        None
    
    def sentimentAnalysis(self,data,sentiment_data):
        words = self.cleanData(data)

        
    def cleanData(self,data):
        regex = r'\w+'
        all_words = []

        for status in data:
            words = re.findall(regex,status)
            all_words.extend(words)

        return all_words
    
    

                



