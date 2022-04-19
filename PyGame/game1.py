import tkinter as app
import random

def kontrolEt():
    global sayac
    if tahmin.get().isdigit():
        s1 = int(tahmin.get())
        sayac = sayac + 1
        if s1 > sayi2:
            yazi2.configure(text='Daha az')
        elif s1 < sayi2:
            yazi2.configure(text='Daha fazla')
        else:
            yazi2.configure(text='{}. defada tahmin ettiniz'.format(sayac))
    tahmin.selection_range(0, app.END)

window = app.Tk()
window.title(' Sayi Tahmin Oyunu')
window.geometry('320x160')

yazi1 = app.Label(window, text='1-10 arasında sayı giriniz', font='Courier 14 bold', width=25, justify='center')
yazi1.place(x=15, y=20)

tahmin = app.Entry(window, font='Courier 14 bold', width=15, justify='center')
tahmin.place(x=70, y=50)
tahmin.focus()

kontrol = app.Button(window, text='KONTROL', font='Courier 14', width=10, command=kontrolEt)
kontrol.place(x=90, y=80)

yazi2 = app.Label(window, text='', font='Courier 16 bold', width=25, justify='center')
yazi2.place(x=0, y=120)

sayi2 = random.randint(1, 10)
sayac = 0

window.mainloop()