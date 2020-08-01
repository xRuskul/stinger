from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import socket
import random
import datetime
serverName = "Unknown Server Name"
version = "Beta 1.0"
serverinfo = serverName
root = Tk()
root.title('Stinger - Launcher')
root.iconbitmap('logo1.ico')
root.geometry('500x500')
conn = sqlite3.connect("data2.stng")
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS server (now TEXT NOT NULL,serverinfo TEXT NOT NULL);')
conn.commit()
now = datetime.datetime.now()
insert = 'INSERT INTO server (now,serverinfo) VALUES(?,?)'
cur.execute (insert,[(now),(serverinfo)])



































def guestwin():
    root.destroy()
    ms.showinfo('You Are Logged in As A Guest, Some Features May Not Be Avalible')
    root7 = Tk()
    root7.title("Stinger - Guest")
    root7.iconbitmap('logo1.ico')
    root7.mainloop()

def window1():
    root.destroy()
    ##################
    ##### Variables #####
    version = "1.0 Beta"
    author = "Rhylend C."
    app = "Stinger Launcher"
    username = "Guest"
    ##################
    def credits():
        root2 = Tk()
        root2.title("Stinger - Credits")
        root2.iconbitmap('logo1.ico')
        root2.geometry('350x350')
        text = Text(root2)
        text.insert(INSERT,
                    "Wodsobe - Banner\nNoobJamesPro - Music\nMichaelReeve's Discord - Code\nHatbringer - Icons\nAll Contributers on our website!\nhttps://sites.google.com/view/textstinger!")
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
        text.insert(INSERT,
                    "~~ Information ~~\n- Welcome to Stinger Beta 1.0! Here you can find:\n-Texting (I'm Trying My Best To Get This All Working and Try To Make It Look Good.\n I'm Sorry If This Isn't What You Expected!)\n -Names (We're Still Working On Getting It Working For Public Use/Looks)\n -Colors! (Yes, I Know There Is Colors Dont Be Too Excited Ok?)\n ~~ People That Have Helped Make Stinger What it is Today! ~~\n NoobJamesPro - Music (Commercial)\n Hatbringer - Icon/Logos!\n Michael Reeve's Discord - Code\n Wodsobe - Banner!\n All Links To Their Social Media/Choice Of Platform Is On Our Website! https://sites.google.com/view/textstinger\n Want to help us out? Use #TextStinger on ANY Social Media and We Might Put It On Our Website!")
        text.config(state=DISABLED, fg="BLACK")
        text.pack()
        root6.mainloop()
    def ex():
        exit()
    ##################
    root1 = Tk()
    root1.title("Stinger - Launcher")
    root1.iconbitmap('logo1.ico')
    root1.geometry('350x500')
    fr = Frame(root1).pack()
    fr2 = Frame(root1).pack()
    Label(root1, text='Stinger - Home\n', font=('bold', 25)).pack()
    b1 = Button(root1, text="Credits", command=credits).pack()
    ex = Button(root1, text="Quit", command=ex).pack()
    b2 = Button(root1, text="Create New Local Server", command=newserv, bg="red").pack()
    b3 = Button(root1, text="Join Local Server (Host Name)", command=joinlclserv, bg="green").pack()
    b4 = Button(root1, text="Join Public Server (Coming Soon)", command=joinpubserv, bg="gray", state=DISABLED).pack()
    b5 = Button(root1, text="Information On Stinger 1.0", command=info, bg="blue").pack()
    root1.mainloop()
# make database and users (if not exists already) table at program start up
with sqlite3.connect('data.stng') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY,password TEXT NOT NULL);')
db.commit()
db.close()

#main Class
class main:
    def __init__(self,master):
    	# Window 
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()

    # Login Function
    def login(self):
    	#Establish Connection
        with sqlite3.connect('data.stng') as db:
            c = db.cursor()

        #Find user: If any are found take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            window1()
        else:
            ms.showerror('Oops!','Username Not Found.')
            
    def new_user(self):
    	#Establish Connection
        with sqlite3.connect('data.stng') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT username FROM user WHERE username = ?')
        c.execute(find_user,[(self.n_username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        #Create New Account 
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()

        #Frame Packing Methods
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
    #Draw Widgets
    def widgets(self):
        self.head = Label(self.master,text = ' Login ',font = ('bold',20),pady = 10)
        self.head.pack()
        self.logf = Frame(self.master,padx =10,pady = 10)
        Label(self.logf,text = ' Username: ',font = ('',12),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',12)).grid(row=0,column=1)
        Label(self.logf,text = ' Password: ',font = ('',12),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',12),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('',12),padx=5,pady=5,command=self.login).grid()
        Button(self.logf,text = ' Continue as Guest ',bd = 3 ,font = ('',12),padx=5,pady=5,command=guestwin).grid()
        Button(self.logf,text = ' Create Account ',bd = 3 ,font = ('',12),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        self.logf.pack()
        
        self.crf = Frame(self.master,padx =10,pady = 10)
        Label(self.crf,text = ' Username: ',font = ('',12),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',12)).grid(row=0,column=1)
        Label(self.crf,text = ' Password: ',font = ('',12),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',12),show = '*').grid(row=1,column=1)
        Button(self.crf,text = ' Create Username ',bd = 3 ,font = ('',12),padx=5,pady=5,command=self.new_user).grid()
        Button(self.crf,text = ' Login ',bd = 3 ,font = ('',12),padx=5,pady=5,command=self.log).grid(row=2,column=1)
        Button(self.crf,text = ' Continue as Guest ',bd = 3 ,font = ('',12),padx=5,pady=5,command=guestwin).grid()
main(root)

root.mainloop()
