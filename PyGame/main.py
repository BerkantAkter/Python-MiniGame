from tkinter import *
from tkinter.ttk import *
import subprocess
import sys


def callgame1 ():	
	subprocess.run(["C:\\Users\\berkant\\Desktop\\PYHTON PROJE\\game1.py", "-c", "game1.py"],shell=True, check=True)

def callgame2 ():
	subprocess.run(["C:\\Users\\berkant\\Desktop\\PYHTON PROJE\\game2.py", "-c", "game2.py"],shell=True, check=True)

def callgame3 ():
	subprocess.run(["C:\\Users\\berkant\\Desktop\\PYHTON PROJE\\game3.py", "-c", "game3.py"],shell=True, check=True)
def callgame4 ():
	subprocess.run(["C:\\Users\\berkant\\Desktop\\PYHTON PROJE\\game4.py", "-c", "game4.py"],shell=True, check=True)

def callpiyano ():
	subprocess.run(["C:\\Users\\berkant\\Desktop\\PYHTON PROJE\\piyano\piyano.py", "-c", "piyano.py"],shell=True, check=True)

def calldate ():
	subprocess.run(["C:\\Users\\berkant\\Desktop\\PYHTON PROJE\\date.py", "-c", "date.py"],shell=True, check=True)

def calltime ():
	subprocess.run(["C:\\Users\\berkant\\Desktop\\PYHTON PROJE\\time.py", "-c", "time.py"],shell=True, check=True)

def callprepare ():
	subprocess.run(["C:\\Users\\berkant\\Desktop\\PYHTON PROJE\\pre.py", "-c", "pre.py"],shell=True, check=True)

app = Tk()
app.geometry("250x120")
app.title("MENU")


label = Label(app, text ="ANA SAYFAYA HOŞGELDİNİZ")
label.pack(pady = 10)

def openNewGAME():
	newWindowgame = Toplevel(app)
	newWindowgame.title("OYUNLAR")
	newWindowgame.geometry("350x120")

	btn1 = Button(newWindowgame ,text ="SAYI TAHMİN OYUNU", command=callgame1)
	btn1.place(x= 20, y=15)

	btn2 = Button(newWindowgame ,text ="RENK BİLME OYUNU", command=callgame2)
	btn2.place(x = 170, y=15)

	btn3 = Button(newWindowgame ,text ="HAFIZA OYUNU", command=callgame3)
	btn3.place(x= 40, y=45)

	btn4 = Button(newWindowgame ,text ="2048", command=callgame4)
	btn4.place(x= 190, y=45)

	btn5 = Button(newWindowgame ,text ="PİYANO", command=callpiyano)
	btn5.place(x= 120, y=75)

	newWindowgame.mainloop()




def openNewINFO():
	newWindowinfo = Toplevel(app)
	newWindowinfo.title("BİLGİLER")
	newWindowinfo.geometry("220x70")
	
	btn1 = Button(newWindowinfo ,text ="TARİH", command=calldate)
	btn1.place(x= 20, y=25)

	btn2 = Button(newWindowinfo ,text ="SAAT",  command=calltime)
	btn2.place(x = 120, y=25)



	newWindowinfo.mainloop()
	

btn = Button(app ,text ="OYUNLAR", command = openNewGAME)
btn.place(x= 30, y=45)



btn = Button(app ,text ="BİLGİLER", command = openNewINFO)
btn.place(x = 120, y=45)


btn = Button(app ,text ="HAZIRLAYANLAR", command = callprepare)
btn.place(x = 60, y= 85)



mainloop()
