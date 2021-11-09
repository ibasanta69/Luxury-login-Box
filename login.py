import time
from tkinter import Label, Button
from tkinter import filedialog, messagebox
from tkinter import*
from tkinter import font
from tkinter.font import BOLD, ROMAN
from PIL import Image, ImageTk
import os
import pyttsx3
import webbrowser
from time import strftime
from pyttsx3 import engine
os.environ["SDL_VIDEO_CENTERED"] = "1"


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 175)
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def Github_link():
    webbrowser.open("https://github.com/ibasanta69")


def facebook_link():
    webbrowser.open("https://www.facebook.com/ibasantachaudhary")


def login():
    user = userentery.get()
    passs = passentery.get()
    if user == 'basanta' and passs == 'basanta123':
        speak('WELCOME !')
    else:
        speak("Sorry ! Invalid password and username please try again !")


def datetime():
    string=strftime('%I:%M:%S %p')
    timelabel.config(text=string)
    timelabel.after(1000,datetime)





logframe = Tk()
logframe.title("Login ")
logframe.geometry('880x500')
logframe.configure(background=('lightblue'))
timelabel=Label(logframe,width=20,height=2,font=('ds-digital',12))
timelabel.place(x=350,y=35)
datetime()
image = Image.open("C:\\Users\\Death Empire\\Desktop\\Login\\lo.jpg")
image1 = image.resize((320, 400), Image.ANTIALIAS)
newimage = ImageTk.PhotoImage(image1)

admin = Image.open("C:\\Users\\Death Empire\\Desktop\\Login\\admin.png")
admin1 = admin.resize((100, 100), Image.ANTIALIAS)
newadmin = ImageTk.PhotoImage(admin1)

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
                      width=12, font=('Arial', 12, BOLD),)
signupbutton.place(x=540, y=390)

facebookbutton = Button(logframe, text="F A C E B O O K",
                        bd=0, command=facebook_link)
facebookbutton.place(x=190, y=420)
youtubebutton = Button(logframe, text="G I T H U B", bd=0, command=Github_link)
youtubebutton.place(x=310, y=420)

logframe.resizable(False, False)
logframe.mainloop()
