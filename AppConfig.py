import json

class AppConfig(object):
    def __init__(self):
        with open('config/watchlist.json') as f:
            watchlistJson = json.load(f)
        self._watchList = watchlistJson["watchlist"]

    @property
    def watchList(self): 
        return self._watchList

    def getStock(self, code):
        for stock in self._watchList:
            if stock["code"] == code:
                return stock
