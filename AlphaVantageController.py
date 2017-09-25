import requests
from os import listdir
from os.path import isfile, join
import glob
from Equity import Equity
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.sectorperformance import SectorPerformances
from DatabaseController import DatabaseController
class AlphaVantage(object):

    def __init__(self, key):
        self.key = key

    def startTimeSeriesCollection(self):
        dataDictionary = {}
        apikey = self.key
        equities = self.equities
        for equity in equities:
            endpoint = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=" + str(equity.symbol) + "&" + "apikey=" + apikey
            response = requests.get(endpoint)
            equity.data = response.json()

    def getSectorData(self):
        sp = SectorPerformances(self.key)
        data, meta_data = sp.get_sector()
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


    def getSymbols(self):
        counter = 2
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
        self.equities = equities
