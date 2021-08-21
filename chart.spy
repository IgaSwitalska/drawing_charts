import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from numpy import abs, pi, sqrt, pi, e, log, log2, log10, sin, cos, tan, arcsin, arccos, arctan, exp, sign, floor, linspace
import tkinter as tk
import warnings

warnings.simplefilter('error', UserWarning)

def draw():
    """
    Funkcja rysuje wykresy podanych przez użytkownika funkcji
    i wyświtla je na wyznaczonym płótnie.
    Genruje również podpisy pod osiami, tytuł wykresu i legendę.
    """
    
    try:
        #niszczenie starego wykresu przed dodaniem nowego
        for widget in frame.winfo_children():
            widget.destroy()
            
        #zakresy
        x1 = float(entry_range_x.get().split(",")[0])
        x2 = float(entry_range_x.get().split(",")[1])

        y1 = float(entry_range_y.get().split(",")[0])
        y2 = float(entry_range_y.get().split(",")[1])
        
        #tworzenie wykresu
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
        label.set("Brak odpowiednich danych!")

    except NameError:
        label.set("Zmienna musi oznaczona jako x!")

    except IndexError:
        label.set("Podano zły przedział!")

    except SyntaxError:
        label.set("Wzory funkcji muszą być oddzielone średnikiem i spacją!")

    except TypeError:
        label.set("Wzory funkcji muszą być oddzielone średnikiem i spacją!")

    except UserWarning:
        label.set("Podano zły przedział!")

def insert(text):
    """
    Funkcja jest wywoływana po naciśnięciu jednego z przycisków do budowania wykresu funkcji,
    wpisuje odpowiedni symbol lub funkcję elementarną
    w miejsce przeznacozne do wpisywania wzoru funkcji
    """
    formula.insert(len(formula.get()),text)


#stworzenie okienka    
root = tk.Tk()
root.title("Rysowanie wykresów")
root.geometry('650x650')

#stworzenie pola, na którym będzie się wyświetlać wykres
frame = tk.Frame(root)
frame.place(x=25, y=230)

#wzór funkcji
tk.Label(root, text="Wzór funkcji: ").grid(row=0, column=0, padx=3, pady=5)

formula = tk.Entry(root)
formula.grid(row=0, column=1, padx=10, pady=5)

#tytuł funkcji
tk.Label(root, text="Tytuł rysunku: ").grid(row=1, column=0, padx=3, pady=5)

entry_title = tk.Entry(root)
entry_title.grid(row=1, column=1, padx=10, pady=5)

#zakres osi x
tk.Label(root, text="Zakres osi x").grid(row=2, column=0, padx=3, pady=2)

entry_range_x = tk.Entry(root)
entry_range_x.grid(row=3, column=0, padx=3, pady=2)

#zakres osi y
tk.Label(root, text="Zakres osi y").grid(row=2, column=1, padx=10, pady=2)

entry_range_y = tk.Entry(root)
entry_range_y.grid(row=3, column=1, padx=10, pady=2)

#etykieta osi x
tk.Label(root, text="Etykieta osi x").grid(row=4, column=0, padx=3, pady=2)

entry_x = tk.Entry(root)
entry_x.grid(row=5, column=0, padx=3, pady=2)

#etykieta osi y
tk.Label(root, text="Etykieta osi y").grid(row=4, column=1, padx=10, pady=2)

entry_y = tk.Entry(root)
entry_y.grid(row=5, column=1, padx=10, pady=2)

#legenda
item = tk.IntVar()
tk.Checkbutton(root, text="legenda", variable=item, onvalue=1, offvalue=0).grid(row=6)

#przycisk rozpoczynający progarm
tk.Button(root, text="Narysuj", command=draw).place(x=200,y=190)

tk.Button(root, text="Koniec", command=quit).place(x=300,y=190)

#przyciski
tk.Label(root, text="Przyciski do budowania wzoru funkcji:").grid(row=0, columnspan=4, column=3)

b1 = ["(", ")", "+", "-", "*", "/"]
b2 = [ "**2", "**3", "sqrt()", "abs()", "pi", "e"]
b3 = ["sin()", "cos()", "tan()", "arcsin()", "arccos()", "arctan()"]
b4 = ["log()", "log2()", "log10()", "exp()", "sign()", "floor()"]
buttons = [b1, b2, b3, b4]

for k in range(len(buttons)): 
    for i in range(len(buttons[k])):
        tk.Button(root, text=buttons[k][i], command=lambda x=buttons[k][i]:insert(x)).grid(row=1+k, column=3+i, sticky="EW")

#storzenie pola, gdzie będzie się wyświetlać wynik w razie błędu
label = tk.StringVar()
tk.Label(root, textvariable=label).grid(row=5, columnspan=6, column=3)

root.mainloop()

