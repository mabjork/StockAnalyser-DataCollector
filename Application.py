from AlphaVantage import AlphaVantageController
from StockTrainingModel import StockTrainingModelController
from Database import DatabaseController
from TwitterWrapper import TwitterController
import glob
import json


def main():
    alphaVantageController = AlphaVantageController("UM5EE9UP44J2R9SE")
    stockTrainingModelController = StockTrainingModelController()
    databaseController = DatabaseController()
    twitterController = TwitterController()

    files = getCompaniesFiles()

    clean_function = lambda x : x.replace('"',"").strip()
    symbols = alphaVantageController.readSymbolsFromMultipleFiles(files,clean_function,startline = 1)

    company_dataframe = stockTrainingModelController.createDataSetFromFile(files[0])

    tags = twitterController.makeTagsFromSymbols(symbols,tag="$")

    data = twitterController.makeSingleRequest(tags[0])

    texts = twitterController.extractTwitText(data)

    
    
    

def getCurrencyFiles():
    files = glob.glob("./Currencies/*.csv")
    return files

def getCompaniesFiles():
    files = glob.glob("./Companies/*.csv")
    return files

def getTwitterTagsFiles():
    files = glob.glob("./TwitterTags/*.txt")
    return files



main()
