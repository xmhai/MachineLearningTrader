import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from StockService import StockService

class PlotService:
    def __init__(self, drawingContext):
        self._drawingContext = drawingContext
        self._canvas = None
        self._ax = None
        self._frame = None

    def resetPlot(self):
        # reset containter frame
        if self._frame is None:
            self._frame = tk.Frame(self._drawingContext.canvas)
            self._frame.pack(fill=tk.BOTH, expand=1)
        else:
            try:
                for widget in self._frame.winfo_children():
                    widget.destroy()            
            except:
                None
            #plt.gcf() get current figure, plt.gca() to get current axis
            plt.clf()

    def plot(self):
        self.resetPlot()

        #load data
        code = self._drawingContext.stock["code"]
        dateRange = self._drawingContext.range
        df = StockService().loadData(code)
        if df is None:
            tk.messagebox.showinfo(title="Error", message="Failed to load data!")
            return

        #draw in matplot
        self._ax = df[['Date','Adj Close']].plot()
        self._ax.set_xlabel("Date")
        self._ax.set_ylabel("Price")

        #output to main window
        self._canvas = FigureCanvasTkAgg(plt.gcf(), master=self._frame)  # A tk.DrawingArea.
        self._canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self._canvas.draw()

        #show toolbar
        #toolbar = NavigationToolbar2Tk(canvas, chartCanvas)
        #toolbar.update()
        #canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

