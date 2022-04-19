import tkinter as app
from playsound import playsound

def do(event=None):
    b1.config(relief=app.SUNKEN)
    playsound('C:\\Users\\berkant\\Desktop\\PYHTON PROJE\\piyano\\nota-do.wav', False)
    b1.after(50, lambda: b1.config(relief=app.RAISED))
def re(event=None):
    b2.config(relief=app.SUNKEN)
    playsound('C:\\Users\\berkant\\Desktop\\PYHTON PROJE\\piyano\\nota-re.wav', False)
    b2.after(50, lambda: b2.config(relief=app.RAISED))
def mi(event=None):
    b3.config(relief=app.SUNKEN)
    playsound('C:\\Users\\berkant\\Desktop\\PYHTON PROJE\\piyano\\nota-mi.wav', False)
    b3.after(50, lambda: b3.config(relief=app.RAISED))
def fa(event=None):
    b4.config(relief=app.SUNKEN)
    playsound('C:\\Users\\berkant\\Desktop\\PYHTON PROJE\\piyano\\nota-fa.wav', False)
    b4.after(50, lambda: b4.config(relief=app.RAISED))
def sol(event=None):
    b5.config(relief=app.SUNKEN)
    playsound('C:\\Users\\berkant\\Desktop\\PYHTON PROJE\\piyano\\nota-sol.wav', False)
    b5.after(50, lambda: b5.config(relief=app.RAISED))
def la(event=None):
    b6.config(relief=app.SUNKEN)
    playsound('C:\\Users\\berkant\\Desktop\\PYHTON PROJE\\piyano\\nota-lya.wav', False)
    b6.after(50, lambda: b6.config(relief=app.RAISED))
def si(event=None):
    b7.config(relief=app.SUNKEN)
    playsound('C:\\Users\\berkant\\Desktop\\PYHTON PROJE\\piyano\\nota-sol.wav', False)
    b7.after(50, lambda: b7.config(relief=app.RAISED))
def oto():
    f = open('C:\\Users\\berkant\\Desktop\\PYHTON PROJE\\piyano\\nota.txt')
    s=f.readlines()
    def notalar(i):
        if i < len(s):
            satir=s[i].split()
            def nota(j):
                if j <len(satir):
                    if satir[j].lower() == 'do':
                        do()
                    if satir[j].lower() == 're':
                        re()
                    if satir[j].lower() == 'mi':
                        mi()
                    if satir[j].lower() == 'fa':
                        fa()
                    if satir[j].lower() == 'sol':
                        sol()
                    if satir[j].lower() == 'la':
                        la()
                    if satir[j].lower() == 'si':
                        si()
                    j = j + 1
                    pencere.after(200, lambda: nota(j))
            nota(0)
            i = i + 1
            pencere.after(200*len(satir)+1000, lambda: notalar(i))
    notalar(0)

pencere = app.Tk()
pencere.title('Piyano')
pencere.geometry('520x400')

b1=app.Button(pencere, text='Do', font='Verdana 14 bold', bg='white', fg='black', height=10, width=3, command=do)
b1.place(x=50, y=20)
b2=app.Button(pencere, text='Re', font='Verdana 14 bold', bg='white', fg='black', height=10, width=3, command=re)
b2.place(x=110, y=20)
b3=app.Button(pencere, text='Mi', font='Verdana 14 bold', bg='white', fg='black', height=10, width=3, command=mi)
b3.place(x=170, y=20)
b4=app.Button(pencere, text='Fa', font='Verdana 14 bold', bg='white', fg='black', height=10, width=3, command=fa)
b4.place(x=230, y=20)
b5=app.Button(pencere, text='Sol', font='Verdana 14 bold', bg='white', fg='black', height=10, width=3, command=sol)
b5.place(x=290, y=20)
b6=app.Button(pencere, text='La', font='Verdana 14 bold', bg='white', fg='black', height=10, width=3, command=la)
b6.place(x=350, y=20)
b7=app.Button(pencere, text='Si', font='Verdana 14 bold', bg='white', fg='black', height=10, width=3, command=si)
b7.place(x=410, y=20)
b8=app.Button(pencere, text='Otomatik', font='Verdana 14 bold', bg='white', fg='black', height=1, width=10, command=oto)
b8.place(x=200, y=300)

pencere.bind('<a>', do)
pencere.bind('<s>', re)
pencere.bind('<d>', mi)
pencere.bind('<f>', fa)
pencere.bind('<g>', sol)
pencere.bind('<h>', la)
pencere.bind('<j>', si)

pencere.mainloop()