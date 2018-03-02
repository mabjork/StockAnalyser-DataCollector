class Equity(object):
    data = ""
    def __init__(self,stock_id,name,symbol,sector,industry):
        self.stock_id = stock_id
        self.name = name
        self.symbol = symbol
        self.sector = sector
        self.industry = industry

    def __str__(self):
        return self.symbol
