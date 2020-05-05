import pandas as pd
import urllib.request
import shutil
from pathlib import Path

import tkinter as tk
from tkinter import messagebox

class StockService:
    def loadData(self, code):
        csvFilename = "data/"+code+".csv"
        if not Path(csvFilename).is_file():
            # file not exists
            result = messagebox.askyesno(title="Load Data", message="Data file does not exist, do you want to download it?")
            if result == True:
                stockService = StockService()
                stockService.downloadData(code)

        try:
            df = pd.read_csv(csvFilename)
            return df
        except:
            return None

    # Download the file from `url` and save it locally under `file_name`:
    def downloadData(self, code):
        url = "https://query1.finance.yahoo.com/v7/finance/download/"+code+"?period1=1&period2=2588636800&interval=1d&events=history"
        filename = "data/"+code+".csv"
        with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

if __name__ == "__main__":
    stockService = StockService()
    df = stockService.loadData("D05.SI")
    print("{} rows loaded".format(len(df)))
