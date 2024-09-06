import tkinter as tk
import random


window=tk.Tk()
window.title("CALCULATOR")

label_a=tk.Label(window,text="Enter a number(a): ")
label_a.pack()
entry_a=tk.Entry(window)
entry_a.pack()

label_b=tk.Label(window,text="Enter a number(b): ")
label_b.pack()
entry_b = tk.Entry(window)
entry_b.pack()


result_label=tk.Label(window,text="",bg="Blue")
result_label.pack()
def calc():

    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        add = a + b
        diff = a - b
        prod = a * b
        divi = a / b if b != 0 else 'Infinity'

        result_label.config(text=f"a={a}  b={b}\na+b={add}\na-b={diff}\na*b={prod}\na/b={divi}")
    except ValueError:
        result_label.config(text="Please Enter valid numbers ",bg ="Red")


button = tk.Button(window,text="Calculate",bg="Red",command=calc)
button.pack()

window.mainloop()