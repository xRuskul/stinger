# Import Modules #
from tkinter import *
import time
import random

##################
##### Definitions ####
def credits():
    root2 = Tk()
    root2.title("Stinger - Credits")
    root2.iconbitmap('logo1.ico')
    root2.geometry('350x350')
    text = Text(root2)
    text.insert(INSERT,"Wodsobe - Banner\nNoobJamesPro - Music\nMichaelReeve's Discord - Code\nHatbringer - Icons\nAll Contributers on our website!\nhttps://sites.google.com/view/textstinger!" )
    text.config(state=DISABLED, fg="BLACK")
    text.pack()
    root2.mainloop()

def newserv():
    root3 = Tk()
    root3.title("Stinger - Create New Server (Host Name)")
    root3.iconbitmap('logo1.ico')
    root3.geometry('350x500')
    root3.mainloop()
def joinlclserv():
    root4 = Tk()
    root4.title("Stinger - Join Local Server")
    root4.iconbitmap('logo1.ico')
    root4.geometry('350x500')
    root4.mainloop()

def joinpubserv():
    root5 = Tk()
    root5.title("Stinger - Public Server")
    root5.iconbitmap('logo1.ico')
    root5.geometry('350x500')
    l1 = Label(root5, text="This feature is unavalible until further notice").pack()
    root5.mainloop()

def info():
    root6 = Tk()
    root6.title("Stinger - Join Local Server")
    root6.iconbitmap('logo1.ico')
    root6.geometry('500x500')
    text = Text(root6)
    text.insert(INSERT,"~~ Information ~~\n- Welcome to Stinger Beta 1.0! Here you can find:\n-Texting (I'm Trying My Best To Get This All Working and Try To Make It Look Good.\n I'm Sorry If This Isn't What You Expected!)\n -Names (We're Still Working On Getting It Working For Public Use/Looks)\n -Colors! (Yes, I Know There Is Colors Dont Be Too Excited Ok?)\n ~~ People That Have Helped Make Stinger What it is Today! ~~\n NoobJamesPro - Music (Commercial)\n Hatbringer - Icon/Logos!\n Michael Reeve's Discord - Code\n Wodsobe - Banner!\n All Links To Their Social Media/Choice Of Platform Is On Our Website! https://sites.google.com/view/textstinger\n Want to help us out? Use #TextStinger on ANY Social Media and We Might Put It On Our Website!" )
    text.config(state=DISABLED, fg="BLACK")
    text.pack()
    root6.mainloop()

def ex():
    exit()
##################
##### Variables #####
version = "1.0 Beta"
author = "Rhylend C."
app = "Stinger Launcher"
username = "Guest"
##################
root1 = Tk()
root1.title("Stinger - Launcher")
root1.iconbitmap('logo1.ico')
root1.geometry('350x500')
fr = Frame(root1).grid()
fr2 = Frame(root1).grid()
Label(fr2, text='Stinger - Home\n', font=('bold', 25)).grid(row=0,column=0)
b1 = Button(fr, text="Credits", command=credits).grid(row=100,column=1)
ex = Button(fr, text="Quit", command=ex).grid(row=100,column=5)
b2 = Button(fr2, text="Create New Local Server", command=newserv, bg="red").grid()
b3 = Button(fr2, text="Join Local Server (Host Name)", command=joinlclserv, bg="green").grid()
b4 = Button(fr2, text="Join Public Server (Coming Soon)", command=joinpubserv, bg="gray", state=DISABLED).grid()
b5 = Button(fr2, text="Information On Stinger 1.0",command=info, bg="blue").grid()
root1.mainloop()
