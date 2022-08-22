##Write a Python GUI program to create  certain number of rows and columns of a Tkinter grid? and add differt color on each column
##write a name,id,batch,feedback are columns 
##each column has differnt color 
import tkinter
root = tkinter.Tk()
root.geometry('500x500')
lst = [ "white", "red", "green", "blue", "cyan", "yellow", "magenta"]
columns = ['name','id','batch','feedback','address','village']

for i in range(6):
    tkinter.Label(root,text=columns[i],bg=lst[i]).grid(row=1,column=i)
