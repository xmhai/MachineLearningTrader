import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk

class PlotService:
    def __init__(self, drawingContext):
        self._drawingContext = drawingContext

    def plot(self):
        df = self.loadData()
        if df is None:
            return

        #draw in matplot
        ax = df[['Date','Adj Close']].plot()
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")

        #output to main window
        #plt.gcf() get current figure, plt.gca() to get current axis
        canvas = FigureCanvasTkAgg(plt.gcf(), master=self._drawingContext.canvas)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        #show toolbar
        #toolbar = NavigationToolbar2Tk(canvas, chartCanvas)
        #toolbar.update()
        #canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def loadData(self):
        try:
            csvFilename = "data/"+self._drawingContext.stock["code"]+".csv"
            df = pd.read_csv(csvFilename)
            return df
        except:
            tk.messagebox.showinfo(title="Error", message="Failed to load data from "+csvFilename)
