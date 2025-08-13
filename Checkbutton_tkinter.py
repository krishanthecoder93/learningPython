from tkinter import *
def selected():
    sugar= sugar_var.get()
    ice = ice_var.get()
    cream=cream_var.get()
    if sugar:
        sugar= ("sugar")
    else:
        sugar=("no sugar")
    if ice:
        ice="ice"
    else:
        ice="no ice"
    if cream:
        cream ="cream"
    else:
        cream="no cream"
    label.config(text="options selected are : " + "\n" +sugar + "\n"+ ice + "\n"+ cream )
root =Tk()
sugar_var = BooleanVar()
ice_var = BooleanVar()
cream_var = BooleanVar()
sugar_checkbox = Checkbutton(root,text="Sugar", variable = sugar_var,command= selected)
ice_checkbox = Checkbutton(root,text="Ice",variable= ice_var,command= selected)
cream_checkbox = Checkbutton(root,text="Cream",variable = cream_var,command= selected)
sugar_checkbox.pack()
ice_checkbox.pack()
cream_checkbox.pack()
label=Label(root)
label.pack()
root.geometry("300x300")
root.mainloop()