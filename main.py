import tkinter as tk
import tkinter.ttk as ttk
from tkinter import simpledialog

from AppConfig import AppConfig
from DrawingContext import DrawingContext
from PlotService import PlotService
from StockService import StockService

_config = AppConfig()
_drawingContext = DrawingContext()
_plotService = PlotService(_drawingContext)

# program start here
root = tk.Tk()

#menu
def NewStock():
    print("New Stock!")
def About():
    tk.messagebox.showinfo(title='About', message='Machine Learning Trader\n\nCoauthor: Lin Hai, Lin Bohan')

menu = tk.Menu(root)
root.config(menu=menu)

filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New Stock...", command=NewStock)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

#watchlist
lblWatchlist = tk.Label(root, text="My Watchlist")
lblWatchlist.place(x=20, y=20)

def onStockSelect(event):
    code = event.widget.get(int(event.widget.curselection()[0]))
    _drawingContext.setStock(_config.getStock(code))
    _drawingContext.setDf(StockService().loadData(code))
    _plotService.plot()

lbStocks = tk.Listbox(root, height=30)
for stock in _config.watchList:
    lbStocks.insert(tk.END, stock["code"])
lbStocks.place(x=20, y=40, width=150)
lbStocks.bind('<<ListboxSelect>>', onStockSelect)

#stock basic information

#chart control panel
chartControlFrame = tk.LabelFrame(master=root, borderwidth=0, highlightthickness=0)
chartControlFrame.place(x=200, y=10)

def onRangeClick(event):
    dateRange = event.widget.cget("text")
    _drawingContext.setRange(dateRange)
    _plotService.plot()
    
ranges = ("5D", "1M", "3M", "6M", "1Y", "2Y", "5Y", "Max", "Compare")
col = 0
for i, range in enumerate(ranges):
    label=tk.Label(chartControlFrame, text=range)
    label.grid(row=0, column=i, padx=10)
    col = col + 1
    label.bind("<Button-1>", onRangeClick)

def onCompareClick(event):
    #ask for stock code
    codesToCompare = simpledialog.askstring(title="Stock Comparison", prompt="Enter the stock codes, seperated by comma")
    if codesToCompare is not None:
        #load adj close data for the list (normalize to base stock)
        _plotService.plot()

label=tk.Label(chartControlFrame, text="Compare")
label.grid(row=0, column=i, padx=10)
col = col + 1
label.bind("<Button-1>", onCompareClick)

def onChartTypeClick(*args):
    chartType = chartTypeVar.get()
    print(chartType)
    _drawingContext.setChartType(chartType)
    _plotService.plot()

chartTypeVar = tk.StringVar(root)
chartTypeVar.set('Line') # set the default option
chartTypeVar.trace("w", onChartTypeClick)
choices = {'Line','Candle'} # Dictionary with options
chartTypeMenu = tk.OptionMenu(chartControlFrame, chartTypeVar, *choices)
chartTypeMenu.grid(row=0, column=col, padx=10, pady=5)
col = col + 1

#chart canvas
chartCanvas = tk.Canvas(root, width=800, height=400)
chartCanvas.place(x=200, y=40)
_drawingContext.setCanvas(chartCanvas)

#analysis

#show application windows
def on_closing():
    root.destroy()
    root.quit()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.title('Machine Learning Trader')
root.geometry("900x550+10+10")

root.mainloop()

print("Exit application")
