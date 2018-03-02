import requests
from os import listdir
from os.path import isfile, join
import glob
from Equity import Equity
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.sectorperformance import SectorPerformances
from DatabaseController import DatabaseController
from Currency import Currency
import json

class AlphaVantageController(object):

    def __init__(self, key):
        self.key = key
        self.endpointfactory = AlphaVantageEndpointFactory(key)

    def makeTimeSeriesRequest(self,function,symbol,interval,outputsize):
        options = {"symbol":symbol,"interval":interval,"outputsize":outputsize}
        endpoint = factory.makeEndpoint(function,options)
        response = requests.get(endpoint)
        data = json.loads(response)
        return data

    def makeCryptoRequest(self):
        None

    def readSymbolsFromFile(self,filename,clean_method = lambda x : x, column = 0, separator = ","):
        if(filename == None or filename == ""):
            raise ValueError("Filename must not be empty")
        
        with open(filename) as f:
            content = f.readlines()
        
        symbols = []

        for line in content:
            symbol = line.split(separator)[column]
            cleaned_symbol = clean_method(symbol)
            symbols.append(cleaned_symbol)

        return symbols


    def readSymbolsFromMultipleFiles(self,filenames,clean_method = lambda x : x,column = 0):
        if(filenames == None or len(filenames) == 0):
            raise ValueError("Filenames cant be None or empty")
            
        all_symbols = []

        for filename in filenames:
            symbols = self.readSymbolsFromFile(filename,clean_method,column)
            all_symbols.extend(symbols)
        
        return all_symbols


class AlphaVantageEndpointFactory(object):
    base = "https://www.alphavantage.co/query?"
    intervals = ["1min","5min","15min","30min","60min"]
    outputsizes = ["compact","full"]
    outputsize_default = "compact"
    requirements_file = "alpha_vantage_api_requirements.txt"

    def __init__(self,apikey):
        self.apikey = apikey
        self.requirements = self.readRequirements()
    
    def makeEndpoint(self,function,options):
        keys = options.keys()
        reqs = self.requirements

        #Checks if the function is valid and supported
        if(function == "" or function == none or function not in reqs.keys()):
            raise ValueError("Not a valid function")
        
        function_requirements = reqs[function]
        required_options = filter(lambda a,b: b == "required", function_requirements)


        #Check if some of required option are not present
        for option in required_options:
            if(option not in keys):
                raise ValueError("Not all required fields are present. Missing " + option)
        
        url = base

        #Check if the options provided are supported
        for key in keys:
            if(function_requirements[key] == "none"):
                raise ValueError("This option " + key + " is not supported by function " + function)

        #Build the url
        url += "function=" + function
        for option,param in options:
            url += "&"
            url += option + "=" + param

        return url



    def readRequirements(self):
        requirements = {}

        with open(self.requirements_file) as f:
            content = f.readlines()
        
        params = content[0].split(";")
        for i in range(1, len(params)):
            line = content[i]
            options = line.split(";")
            function_name = options[0]
            options_dict = {}

            for j in range(1,len(options)):
                param = params[j]
                option = options[j]
                options_dict[param] = option
            
            requirements[function_name] = options_dict

        return requirements


