from AlphaVantageController import AlphaVantage


def main():
    controller = AlphaVantage("UM5EE9UP44J2R9SE")
    controller.getSymbols()
    controller.saveToDB()
    #controller.startTimeSeriesCollection()
    #controller.getSectorData()



main()
