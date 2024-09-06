import tkinter as tk
import random

root=tk.Tk()
root.title("Manipulator")



label_b=tk.Label(root,text="",bg="green")
label_b.pack()
label_a=tk.Label(root,text="",bg="yellow")
label_a.pack()


result_label=tk.Label(root,text="",bg="Blue")
result_label.pack()
arr=['khush',
     'akshita',
     'rahul',
     'kriti',
     'naman',
     'siddharth',
     'tushar',
     'harsh',
     'aryank',
     'raghav'
     ]
newarr=[]
def choose():
     if arr:
         a=random.choice(arr)
         arr.remove(a)
         newarr.append(a)

         label_b.config(text=f"Current Name of List {arr}")
         label_a.config(text=f"Selected Name= {a}")

         result_label.config(text=f"Selected List: {newarr} ")
         if not arr:
             label_b.config(text=f"Current name of list is Empty ")
             button.config(state=tk.DISABLED)
     else:
         result_label.config(text="List is already Empty")


button = tk.Button(root,text="Show Name",bg="Red",command=choose)
button.pack()

root.mainloop()