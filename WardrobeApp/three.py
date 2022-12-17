from tkinter import *
from functools import partial

def Profile(username, password):
	print("Username :", username)
    helpme=partial(helpme)
    needHelpButton = Button(tkWindow, text="Need Help !", command=helpme).grid(row=4, column=0)

#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Login')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

tkWindow.mainloop()