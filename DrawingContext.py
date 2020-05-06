class DrawingContext(object):
    def __init__(self):
        self._canvas = None

        self._stock = None
        self._range = ""
        self._chartType = "line"

        self._df = None
        self._dfToCompare = None

    @property
    def canvas(self): 
        return self._canvas

    def setCanvas(self, canvas):
        self._canvas = canvas

    @property
    def stock(self): 
        return self._stock

    def setStock(self, stock):
        self._stock = stock

    @property
    def range(self): 
        return self._range

    def setRange(self, range):
        self._range = range

    @property
    def chartType(self): 
        return self._chartType

    def setChartType(self, chartType):
        self._chartType = chartType

    @property
    def df(self): 
        return self._df

    def setDf(self, df):
        self._df = df

    @property
    def dfToCompare(self): 
        return self._dfToCompare

    def setDfToCompare(self, dfToCompare):
        self._dfToCompare = dfToCompare

