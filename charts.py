from tkinter import font
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
        f = Figure(figsize=(5,3))
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

# background color and font
bg_color = "#b8f09c"
text_font = "Gothic"

# creating a window  
root = tk.Tk()
root.title("Drawing charts")
root.geometry('700x700')
root.configure(bg=bg_color)

tk.Label(root, text="Drawing charts", font=("Roman", 40), background=bg_color).grid(row=0, columnspan=5, column=1, pady=8)

# creating a space, where the chart will appear
frame = tk.Frame(root,background=bg_color)
frame.place(x=100, y=340)

# formula
tk.Label(root, text="Formula: ", font=(text_font,15), background=bg_color).grid(row=1, column=0, padx=3, pady=5)

formula = tk.Entry(root)
formula.grid(row=1, column=1, padx=10, pady=5)

# chart title
tk.Label(root, text="Chart title: ",  font=(text_font,15), background=bg_color).grid(row=2, column=0, padx=3, pady=5)

entry_title = tk.Entry(root)
entry_title.grid(row=2, column=1, padx=10, pady=5)

# X axis range
tk.Label(root, text="X axis range:", font=(text_font,12), background=bg_color).grid(row=3, column=0, padx=3, pady=2)

entry_range_x = tk.Entry(root)
entry_range_x.grid(row=4, column=0, padx=3, pady=2)

# Y axis range
tk.Label(root, text="Y axis range:", font=(text_font,12), background=bg_color).grid(row=3, column=1, padx=10, pady=2)

entry_range_y = tk.Entry(root)
entry_range_y.grid(row=4, column=1, padx=10, pady=2)

# X axis label
tk.Label(root, text="X axis label:", font=(text_font,12), background=bg_color).grid(row=5, column=0, padx=3, pady=2)

entry_x = tk.Entry(root)
entry_x.grid(row=6, column=0, padx=3, pady=2)

# Y axis label
tk.Label(root, text="Y axis label:", font=(text_font,12), background=bg_color).grid(row=5, column=1, padx=10, pady=2)

entry_y = tk.Entry(root)
entry_y.grid(row=6, column=1, padx=10, pady=2)

# legend
item = tk.IntVar()
tk.Checkbutton(root, text="legend", font=(text_font,12), background=bg_color, variable=item, onvalue=1, offvalue=0).grid(row=7, pady=5)

# draw  and close button
tk.Button(root, text="Draw", command=draw, font=(text_font,12), background="#f0e96e", activebackground="#f0eb8d", width=10, height=2).place(x=200,y=280)

tk.Button(root, text="Close", command=quit, font=(text_font,12), background="#eb6d59", activebackground="#eb998a", width=10, height=2).place(x=300,y=280)

# other buttons
tk.Label(root, text="Buttons to build a formula:", font=(text_font,12), background=bg_color).grid(row=1, columnspan=4, column=3)

b1 = ["(", ")", "+", "-", "*", "/"]
b2 = [ "**2", "**3", "sqrt()", "abs()", "pi", "e"]
b3 = ["sin()", "cos()", "tan()", "arcsin()", "arccos()", "arctan()"]
b4 = ["log()", "log2()", "log10()", "exp()", "sign()", "floor()"]
buttons = [b1, b2, b3, b4]

for k in range(len(buttons)): 
    for i in range(len(buttons[k])):
        tk.Button(root, text=buttons[k][i], font=(text_font,10), background="#edaf72", command=lambda x=buttons[k][i]:insert(x)).grid(row=2+k, column=3+i, sticky="EW")

# creating a space, where the error message will appear
label = tk.StringVar()
tk.Label(root, textvariable=label, background=bg_color, font=(text_font,10,"bold")).grid(row=6, columnspan=6, column=3)

root.mainloop()

