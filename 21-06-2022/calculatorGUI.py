##Calculator GUI 
##It is GUI based calculator used to calculate any simple mathematical equation. 
## Modules Used 
##- tkinter 
## How it works 
##- It takes the mathematical equation by the User.
##- It returns the result of the mathematical equation
import tkinter
from tkinter import *
window = Tk()
window.title("Calculator")
window.configure(bg='lightgray')
window.geometry("570x580")
equation=""
def show(num):
    global equation
    equation += num
    label.config(text=equation)

def clear():
    global equation
    equation=" "
    label.config(text=equation)

def cancel():
    global equation
    equation=" "
    label.config(text=equation)

def calculate():
    global equation
    result=" "
    if equation != "":
        result=eval(equation)
    else:
        result="error"
        equation=" "
    label.config(text=result)
label=Label(window,width=25,height=2,text=" ",font=("arial",30))
label.pack()
    
btn = Button(window, text ='C', width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="Red",command=lambda:clear()).place(x=10,y=100)
btn = Button(window, text ='Back',width=5,height=1,font=("Arial",30,"bold"),bd =1,fg="Red",command=lambda:cancel( )).place(x=150,y=100)
btn = Button(window, text ='%',width=5,height=1,font=("Arial",30,"bold"),bd =1,fg="Red",command=lambda:show("%")).place(x=290,y=100)
btn = Button(window, text ='/',width=5,height=1,font=("Arial",30,"bold"),bd =1,fg="Red",command=lambda:show("/")).place(x=430,y=100)

btn = Button(window, text ='7',width=5,height=1,font=("Arial",30,"bold"),bd =1,fg="Red",command=lambda:show("7")).place(x=10,y=190)
btn = Button(window, text ='8',width=5,height=1,font=("Arial",30,"bold"),bd =1,fg="Red",command=lambda:show("8")).place(x=150,y=190)
btn = Button(window, text ='9',width=5,height=1,font=("Arial",30,"bold"),bd =1,fg="Red",command=lambda:show("9")).place(x=290,y=190)
btn = Button(window, text ='*',width=5,height=1,font=("Arial",30,"bold"),bd =1,fg="Red",command=lambda:show("*")).place(x=430,y=190)

btn = Button(window, text ='4',width=5,height=1,font=("Arial",30,"bold"),bd =1,fg="Red",command=lambda:show("4")).place(x=10,y=280)
btn = Button(window, text ='5',width=5,height=1,font=("Arial",30,"bold"),bd =1,fg="Red",command=lambda:show("5")).place(x=150,y=280)
btn = Button(window, text ='6',width=5,height=1,font=("Arial",30,"bold"),bd =1,fg="Red",command=lambda:show("6")).place(x=290,y=280)
btn = Button(window, text ='-',width=5,height=1,font=("Arial",30,"bold"),bd =1,fg="Red",command=lambda:show("-")).place(x=430,y=280)

btn = Button(window, text ='1',width=5,height=1,font=("Arial",30,"bold"),bd =1,fg="Red",command=lambda:show("1")).place(x=10,y=370)
btn = Button(window, text ='2',width=5,height=1,font=("Arial",30,"bold"),bd =1,fg="Red",command=lambda:show("2")).place(x=150,y=370)
btn = Button(window, text ='3',width=5,height=1,font=("Arial",30,"bold"),bd =1,fg="Red",command=lambda:show("3")).place(x=290,y=370)
btn = Button(window, text ='+',width=5,height=1,font=("Arial",30,"bold"),bd =1,fg="Red",command=lambda:show("+")).place(x=430,y=370)

btn = Button(window, text ='Snc',width=5,height=1,font=("Arial",30,"bold"),bd =1,fg="Red",command=lambda:show("Snc")).place(x=10,y=470)
btn = Button(window, text ='0',width=5,height=1,font=("Arial",30,"bold"),bd =1,fg="Red",command=lambda:show("0")).place(x=150,y=470)
btn = Button(window, text ='.',width=5,height=1,font=("Arial",30,"bold"),bd =1,fg="Red",command=lambda:show(".")).place(x=290,y=470)
btn = Button(window, text ='=',width=5,height=1,font=("Arial",30,"bold"),bd =1,fg="Red",command=lambda:calculate( )).place(x=430,y=470)
window.mainloop()

