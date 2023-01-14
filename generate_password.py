import tkinter as tk
from tkinter import *
import string
import secrets

class fenetre(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1280x720")
        self.title("Password Generator")
        self.config(bg="white")
        
        
    # create the button
        self.button_generate = tk.Button(self, text='GENERATE', width=100, command=self.check_password)
        self.button_generate.pack(side='top')
    # create text who spawn
        self.status_label = tk.Label(self, text="")
        self.status_label.pack(side='top')
        self.status_label.config(bg='white')
                     
            
    def check_password(self):
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation
        alphabet = letters + digits + special_chars
        pwd_length = 12
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))
        if self.button_generate:
            self.status_label.config(text=pwd, font='Arial 30')
            
            
        


   
           

root = fenetre()
root.mainloop()    