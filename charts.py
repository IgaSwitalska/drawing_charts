import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from numpy import abs, pi, sqrt, pi, e, log, log2, log10, sin, cos, tan, arcsin, arccos, arctan, exp, sign, floor, linspace
import tkinter as tk
import warnings

warnings.simplefilter('error', UserWarning)

def draw():
    """
    The function that draws graphs of the function given by the user 
    and displays them on the canvas.
    The function generates also labels, a chart title and a legend.
    """
    
    try:
        # destroying the old chart before adding a new one
        for widget in frame.winfo_children():
            widget.destroy()
            
        # ranges
        x1 = float(entry_range_x.get().split(",")[0])
        x2 = float(entry_range_x.get().split(",")[1])

        y1 = float(entry_range_y.get().split(",")[0])
        y2 = float(entry_range_y.get().split(",")[1])
        
        # creating a figure and then a chart
        x = linspace(x1,x2,1000)
        f = Figure(figsize=(6,4))
        a = f.add_subplot(111)

        lista = formula.get().split("; ")
        for function in lista:
            a.plot(x,(eval("lambda x:" + function)(x)))
        
        a.set_xlim(x1,x2)
        a.set_ylim(y1,y2)
        a.set_title(entry_title.get())
        a.set_xlabel(entry_x.get())
        a.set_ylabel(entry_y.get())

        if item.get() == 1:
            a.legend(lista)
            
        canvas = FigureCanvasTkAgg(f, frame)

        function = canvas.get_tk_widget()
        function.pack()

        label.set("")
        
    except ValueError:
        label.set("No appropriate data!")

    except NameError:
        label.set("The variable must be marked as x")

    except IndexError:
        label.set("Wrong range has been given!")

    except SyntaxError:
        label.set("Function formulas must be separated by a semicolon and a space!")
    except TypeError:
        label.set("Function formulas must be separated by a semicolon and a space!")

    except UserWarning:
        label.set("Wrong range has been given!")

def insert(text):
    """
    The function is called when pressing one of the formula-building buttons. 
    It inserts appropriate symbol or elementary function 
    in the place for entering the function formula.
    """
    formula.insert(len(formula.get()),text)


# creating a window  
root = tk.Tk()
root.title("Drawing charts")
root.geometry('650x650')

# creating a space, where the chart will appear
frame = tk.Frame(root)
frame.place(x=25, y=230)

# formula
tk.Label(root, text="Formula: ").grid(row=0, column=0, padx=3, pady=5)

formula = tk.Entry(root)
formula.grid(row=0, column=1, padx=10, pady=5)

# chart title
tk.Label(root, text="Chart title: ").grid(row=1, column=0, padx=3, pady=5)

entry_title = tk.Entry(root)
entry_title.grid(row=1, column=1, padx=10, pady=5)

# X axis range
tk.Label(root, text="X axis range:").grid(row=2, column=0, padx=3, pady=2)

entry_range_x = tk.Entry(root)
entry_range_x.grid(row=3, column=0, padx=3, pady=2)

# Y axis range
tk.Label(root, text="Y axis range:").grid(row=2, column=1, padx=10, pady=2)

entry_range_y = tk.Entry(root)
entry_range_y.grid(row=3, column=1, padx=10, pady=2)

# X axis label
tk.Label(root, text="X axis label:").grid(row=4, column=0, padx=3, pady=2)

entry_x = tk.Entry(root)
entry_x.grid(row=5, column=0, padx=3, pady=2)

# Y axis label
tk.Label(root, text="Y axis label:").grid(row=4, column=1, padx=10, pady=2)

entry_y = tk.Entry(root)
entry_y.grid(row=5, column=1, padx=10, pady=2)

# legend
item = tk.IntVar()
tk.Checkbutton(root, text="legend", variable=item, onvalue=1, offvalue=0).grid(row=6)

# draw  and close button
tk.Button(root, text="Draw", command=draw).place(x=200,y=190)

tk.Button(root, text="Close", command=quit).place(x=300,y=190)

# Other buttons
tk.Label(root, text="Buttons to build a formula:").grid(row=0, columnspan=4, column=3)

b1 = ["(", ")", "+", "-", "*", "/"]
b2 = [ "**2", "**3", "sqrt()", "abs()", "pi", "e"]
b3 = ["sin()", "cos()", "tan()", "arcsin()", "arccos()", "arctan()"]
b4 = ["log()", "log2()", "log10()", "exp()", "sign()", "floor()"]
buttons = [b1, b2, b3, b4]

for k in range(len(buttons)): 
    for i in range(len(buttons[k])):
        tk.Button(root, text=buttons[k][i], command=lambda x=buttons[k][i]:insert(x)).grid(row=1+k, column=3+i, sticky="EW")

# reating a space, where the error message will appear
label = tk.StringVar()
tk.Label(root, textvariable=label).grid(row=5, columnspan=6, column=3)

root.mainloop()

