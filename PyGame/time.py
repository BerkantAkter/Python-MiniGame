from tkinter import *
from time import *
import datetime
 
app=Tk()
app.title("SAAT")

def openNewGAME():
	newWindow = (app)
	newWindow.title("New Window")
	newWindow.geometry("350x400")
 
def clock():
    text=strftime("%T")
    label.config(text=text)
    label.after(1000,clock)
 
label=Label(app,font=("ds-digital",154),bg="black",fg="purple")
label.pack(anchor="center")
labell=Label(app,text=("SAAT DAKİKA SANİYE"),bg="white",fg="black",font=("Arial",40))
labell.pack(anchor="center")
 
clock()
mainloop()