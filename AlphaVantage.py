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

    def readSymbolsFromFile(self,filename,clean_method = lambda x : x, column = 0):
        if(filename == None or filename == ""):
            raise ValueError("Filename must not be empty")
        
        with open(filename) as f:
            content = f.readlines()
        
        symbols = []

        for symbol in content:
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


            


        
        



"""
    def getSymbols(self):
        counter = 1
        equities = []
        files = glob.glob("./Companies/*.csv")
        for fileName in files:
            with open(fileName) as f:
                content = f.readlines()
                for line in content:
                    parts = line.split(",")
                    parts[0] = parts[0].replace('"','')
                    parts[1] = parts[1].replace('"','')
                    parts[6] = parts[6].replace('"','')
                    parts[7] = parts[7].replace('"','')
                    equity = Equity(counter,parts[1],parts[0],parts[6],parts[7])
                    equities.append(equity)
                    counter += 1


        physicalCounter = 1
        pcurrenciesList = []
        with open("./Currencies/physical_currency_list.csv") as f:
            content = f.readlines()
            for line in content:
                parts = line.split(",")
                currency = Currency(physicalCounter,parts[0],parts[1],"Physical")
                pcurrenciesList.append(currency)
                physicalCounter += 1


        digitalCounter = 1
        dcurrenciesList = []
        with open("./Currencies/digital_currency_list.csv") as f:
            content = f.readlines()
            for line in content:
                parts = line.split(",")
                currency = Currency(digitalCounter,parts[0],parts[1],"Digital")
                dcurrenciesList.append(currency)
                digitalCounter += 1

        self.physicalcurrencies = pcurrenciesList
        self.digitalcurrencies = dcurrenciesList
        self.equities = equities
"""
"""
    def getSectorData(self):
        sp = SectorPerformances(self.key)
        data, meta_data , _ = sp.get_sectorsector()
        print data

    def saveToDB(self):
        controller = DatabaseController()
        for equity in self.equities:
            datalist = []
            data = {}
            data["name"] = equity.name
            data["symbol"] = equity.symbol
            data["sector"] = equity.sector
            data["stock_id"] = equity.stock_id
            datalist.append(data)
            controller.saveToDB(datalist)
        for pc in self.physicalcurrencies:
            datalist = []
            data = {}
            data["name"] = pc.name
            data["symbol"] = pc.symbol
            data["id"] = pc.currency_id
            datalist.append(data)
            controller.savePCurrencyToDB(datalist)
        for pc in self.digitalcurrencies:
            datalist = []
            data = {}
            data["name"] = pc.name
            data["symbol"] = pc.symbol
            data["id"] = pc.currency_id
            datalist.append(data)
            controller.saveDCurrencyToDB(datalist)
    """