class Currency(object):
    def __init__(self,currency_id,symbol,name,ctype):
        self.currency_id = currency_id
        self.symbol = symbol
        self.name = name
        self.type = ctype

    def __str__(self):
        return self.symbol
