import tkinter as app
import random
from tkinter import messagebox


renkler = ['black-siyah', 'white-beyaz', 'red-kırmızı', 'green-yeşil', 'blue-mavi', 'yellow-sarı',
           'brown-kahverengi', 'orange-turuncu', 'grey-gri', 'maroon-bordo', 'purple-mor', 'pink-pembe']

global puan
puan = 0
kalanZaman = 30



def basla(event):
    if kalanZaman == 30:
        gerisayim()
    sonrakiRenk()


def sonrakiRenk():
    global puan
    if kalanZaman > 0:
        e.focus()
        if e.get().lower() == renkler[1][renkler[1].find('-')+1:].lower():
            puan += 1
        e.delete(0, app.END)
        random.shuffle(renkler)
        yazi.config(fg=str(renkler[1][:renkler[1].find('-')]), text=str(renkler[0][renkler[0].find('-')+1:]))
        puanLabel.config(text='PUAN: ' + str(puan))


def gerisayim():
    global kalanZaman
    if kalanZaman > 0:
        kalanZaman -= 1
        timeLabel.config(text='KALAN ZAMAN: ' + str(kalanZaman))
        timeLabel.after(1000, gerisayim)
    elif kalanZaman == 0:
        messagebox.showinfo("RENK OYUNU", "Üzgünüm SÜRE BİTTİ ")
        


newWindow = app.Tk()
newWindow.title('RENK OYUNU')
newWindow.geometry('400x200')


infoLabel = app.Label(newWindow, fg='red', text='YAZININ RENGİNİ YAZIN', font=('Courier', 12))
infoLabel.pack()

puanLabel = app.Label(newWindow, fg='green', text='BAŞLAMAK İÇİN ENTER"A BASINIZ', font=('Courier', 12))
puanLabel.pack()

timeLabel = app.Label(newWindow, fg='blue', text='KALAN ZAMAN : ' + str(kalanZaman), font=('Courier', 12))
timeLabel.pack()

yazi = app.Label(newWindow, font=('Helvetica', 60))
yazi.pack()


e = app.Entry(newWindow)
newWindow.bind( '<Return>', basla)
e.pack()
e.focus()


newWindow.mainloop()