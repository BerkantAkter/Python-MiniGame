from tkinter import *
from time import *
import datetime
 
app=Tk()
app.title("TARİH")

 
def history():
    text=strftime("    %d . %m . %Y ")
    label.config(text=text)
    label.after(1000,history)
 
label=Label(app,font=("ds-digital",100),bg="black",fg="purple")
label.pack(anchor="center")
labell=Label(app,text=("GÜN    AY      YIL"),bg="white",fg="black",font=("Arial",54))
labell.pack(anchor="center")
 
history()
mainloop()