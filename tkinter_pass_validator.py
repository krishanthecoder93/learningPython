from tkinter import *
import bcrypt

def validate(password):
    hash = b'$2b$12$jKXOwe9CEjqrw84PocPsSOMUQvlNuGeZZVmbg9OjfhU54ID6Y2yUW'
    password = bytes(password,encoding= 'utf-8')
    if bcrypt.checkpw(password,hash):
        print("Login successful")
    else:
        print("Invalid password ")




root = Tk()
root.geometry("300x300")

password_entry = Entry(root)
password_entry.pack()

button = Button (text="validate",command = lambda: validate(password_entry.get()))
button.pack()


root.mainloop()