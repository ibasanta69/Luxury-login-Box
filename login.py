import os
import time
import threading
import webbrowser
from tkinter import *
from tkinter import font
from tkinter import filedialog, messagebox
import pyttsx3
from pyttsx3 import engine


os.environ["SDL_VIDEO_CENTERED"] = "1"


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 175)
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


def Github_link():
    logframe.after(100, lambda: webbrowser.open("https://github.com/ibasanta69"))


def facebook_link():
    logframe.after(100, lambda: webbrowser.open("https://www.facebook.com/ibasantachaudhary"))


def login():
    user = userentery.get()
    passs = passentery.get()

    if user == 'basanta' and passs == 'basanta123':
        thread = threading.Thread(target=speak, args=['Welcome !'])

    else:
        thread = threading.Thread(target=speak, args=["Sorry ! Invalid password and username please try again !"])

    thread.start()


def datetime():
    string=time.strftime('%I:%M:%S %p')
    timelabel.config(text=string)
    timelabel.after(1000, datetime)


def OpenAtCenter():
    width, height = 880, 500
    screenwidth = logframe.winfo_screenwidth() // 2

    screenheight = logframe.winfo_screenheight() // 2
    logframe.geometry(f'{width}x{height}+{screenwidth - width // 2}+{screenheight - height // 2}')


logframe = Tk()
logframe.withdraw()
logframe.after(0, logframe.deiconify)

OpenAtCenter()
logframe.title("Login ")
logframe.config(bg='lightblue')
timelabel=Label(logframe,width=20,height=2,font=('ds-digital',12))
timelabel.place(x=350,y=35)
logframe.after(0, datetime)
logframe.iconbitmap('WindowIcon.ico')

newimage = PhotoImage(file='lo.png')
newadmin = PhotoImage(file='admin.png')

frame1 = Frame(logframe, width=780, height=500, bd=2)
admin = Label(frame1, image=newimage,
              border=0, height=350, width=310).place(x=0, y=0)
frame1.place(x=130, y=100)

lbe = Label(frame1, text="W e l C o m e", font=('Arial', 12, 'italic'))
lbe.grid(padx=260, pady=160)

adminlabel = Label(logframe, width=130, height=130, image=newadmin)
adminlabel.place(x=535, y=120)

userlabel = Label(logframe, text="User Name", font=('Arial', 12,))
userlabel.place(x=556, y=240)

userentery = Entry(logframe, relief='groove', bd=0,
                   justify=CENTER, font=('Arial', 12), width=19, bg='#d4d2d2')
userentery.place(x=515, y=270)

passlabel = Label(logframe, text=" Password ", font=('Arial', 12,))
passlabel.place(x=556, y=300)

passentery = Entry(logframe, relief=GROOVE, bd=0, justify=CENTER,
                   font=('Arial', 12), width=19, bg='#d4d2d2', show='*')
passentery.place(x=515, y=330)

signupbutton = Button(logframe, text="Sign in", relief=GROOVE, command=login,
                      width=12, font=('Arial', 12, 'bold'),)
signupbutton.place(x=540, y=390)

facebookbutton = Button(logframe, text="F A C E B O O K",
                        bd=0, cursor='hand2', command=facebook_link)
facebookbutton.place(x=190, y=420)

youtubebutton = Button(logframe, text="G I T H U B", bd=0, cursor='hand2', command=Github_link)
youtubebutton.place(x=310, y=420)

logframe.resizable(0, 0)
logframe.mainloop()
