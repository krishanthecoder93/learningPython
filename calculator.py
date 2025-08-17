from tkinter import *
import ast


i=0
def get_number(num):
    global i
    display.insert(i,num)
    i+=1

def get_operation(operator):
    global i
    length= len(operator)
    display.insert(i,operator)
    i+=length

def clear_all():
    display.delete(0,END)

def calculate():
    entire_string = display.get()
    try:
        node= ast.parse(entire_string,mode="eval")
        result= eval(compile(node,'<string>','eval'))
        clear_all()
        display.insert(0,result)
    except Exception :
        clear_all()
        display.insert(0,"Error")

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string=entire_string[ :-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,'')
root =Tk()
display= Entry(root)
display.grid(row=1,columnspan=6,sticky=W+E)

# adding buttons form 1 to 9
numbers=[9,8,7,6,5,4,3,2,1]
counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button= Button(root,text=button_text,width=2,height=2,command=lambda text=button_text:get_number(text))
        button.grid(row=x+2,column=y)
        counter+=1

# adding button "0"
button= Button(root,text="0",width=2,height=2,command=lambda:get_number(0))
button.grid(row=5,column=1)
#adding button "AC"(clear screen)
button= Button(root,text="AC",width=2,height=2,command=lambda:clear_all())
button.grid(row=5,column=0)
#adding button "="
button= Button(root,text="=",width=2,height=2,command=lambda:calculate())
button.grid(row=5,column=2)
# adding undo button(delete button)
button= Button(root,text="<-",width=2,height=2,command=lambda:undo())
button.grid(row=5,column=5)


# now column 3 is empty,let fill up with operations
count=0
operations =['+','-','*','/','*3.14','%','(','**',')','**2','**0.5']
for x in range(4):
    for y in range(3):
        if count<len(operations):
            button= Button(root,text=operations[count],width=2,height=2,command=lambda text=operations[count]: get_operation(text))
            count += 1
            button.grid(row=x+2,column=y+3)

root.mainloop()

