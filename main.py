import tkinter as tk
import tkinter.ttk as ttk
import json

from PlotService import PlotService

#class definition
class Config(object):
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

_config = Config()

class DrawingContext(object):
    def __init__(self):
        self._stock = None
        self._canvas = None
        self._range = ""

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

#def onExchangeSelected(event):
#    lbStocks.delete(0, tk.END)
#    exchange = cbExchanges.get()
#    for stock in _config.watchList.get(exchange):
#        lbStocks.insert(tk.END, stock["code"])

#cbExchanges = ttk.Combobox(root, values=_config.exchangeList)
#cbExchanges.place(x=20, y=40, width=150)
#cbExchanges.current(0)
#cbExchanges.bind("<<ComboboxSelected>>", onExchangeSelected)

def onStockSelect(event):
    # Note here that Tkinter passes an event object to onselect()
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    _drawingContext.setStock(_config.getStock(value))
    _plotService.plot()

lbStocks = tk.Listbox(root, height=30)
for stock in _config.watchList:
    lbStocks.insert(tk.END, stock["code"])
lbStocks.place(x=20, y=40, width=150)
lbStocks.bind('<<ListboxSelect>>', onStockSelect)

#stock basic information

#chart control panel
ranges = ("5D", "1M", "3M", "6M", "1Y", "2Y", "5Y", "Max", "Compare")
def showChart(event):
    _drawingContext.setRange(event.widget.cget("text"))
    _plotService.plot()
    
chartControlFrame = tk.LabelFrame(master=root, borderwidth=0, highlightthickness=0)
chartControlFrame.place(x=200, y=20)
for i, range in enumerate(ranges):
    label=tk.Label(chartControlFrame, text=range)
    label.grid(row=0, column=i)
    label.bind("<Button-1>", showChart)

#chart
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

exit()