from AlphaVantage import AlphaVantageController
from StockTrainingModel import StockTrainingModelController
from Database import DatabaseController
import glob


def main():
    alphaVantageController = AlphaVantageController("UM5EE9UP44J2R9SE")
    stockTrainingModelController = StockTrainingModelController()
    databaseController = DatabaseController()

    files = getCompaniesFiles()
    symbols = alphaVantageController.readSymbolsFromMultipleFiles(files,lambda x : x.replace('"',"").strip(),startline = 1)

    dataframe = stockTrainingModelController.createDataSetFromFile(files[0])
    
    data = alphaVantageController.makeTimeSeriesRequest("TIME_SERIES_INTRADAY",symbols[0],"60min","compact")
    print data

def getCurrencyFiles():
    files = glob.glob("./Currencies/*.csv")
    return files

def getCompaniesFiles():
    files = glob.glob("./Companies/*.csv")
    return files

def getTwitterTagsFiles():
    files = glob.glob("./TwitterTags/*.txt")


main()
