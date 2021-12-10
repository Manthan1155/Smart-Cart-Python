import tkinter as tk
from tkinter import *
import os
import firebase_admin
from firebase_admin import db
from PIL import Image, ImageTk

class ProductMap(tk.Tk):

    def connectWithDatabase(self):
        cred = firebase_admin.credentials.Certificate(
            "smart-shopping-cart-1fbac-firebase-adminsdk-wfobd-09a600f28a.json")
        default_app = firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://smart-shopping-cart-1fbac-default-rtdb.firebaseio.com/'
        })
        self.ref = db.reference('items')

    def getAllItems(self):
        result_data = db.reference('items').get()
        return result_data

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('650x450')
        self.configure(background="#353839")
        self.listitem = tk.Listbox(self)
        self.listitem.grid(row="2", column="0", columnspan="5")
        self.listloc = tk.Listbox(self)
        self.listloc.grid(row="2", column="6", columnspan="5")
        self.btnMap = tk.Button(self, text="Map", background="#a1caf1", command=lambda: self.mappic()).place(x=50,y=200)
        self.entry = tk.Entry(self)
        self.entry.grid(row="0", column="0", columnspan="5")
        self.items_list = self.getAllItems()
        # self.listitem.bind("<>", self.filout)
        # self.entry.bind("", self.check)

        # self.update(self.items_list)
        self.populate_data_in_list(self.items_list)
        self.populate_data_in_listloc(self.items_list)

    def populate_data_in_list(self, items_list):
        for key, value in items_list.items():
            self.listitem.insert(tk.END, value['name'])

    def populate_data_in_listloc(self, items_list):
        for key, value in items_list.items():
            self.listloc.insert(tk.END, value['location'])

    # window = Tk()
    def mappic(self):

        s = Toplevel()  # For secondary window use Toplevel
        s.title('Store Map)')
        s.geometry('650x450')
        filename = str(self.listitem.curselection())
        file = str(self.listitem.get(ACTIVE))
        if filename == '()':
            image = ImageTk.PhotoImage(Image.open("Map.jpeg"))
        else:
            imgname = file+".jpeg"
            image = ImageTk.PhotoImage(Image.open(imgname))
        panel = Label(s, image=image)
        panel.image = image
        panel.pack()
        self.listitem.selection_clear(0, END)




    def update(self, items_list):
        # Clear the listbox
        self.listitem.delete(0, END)

        # Add toppings to listbox
        for key, value in items_list.items():
            self.listitem.insert(tk.END, value['name'])

    # Update entry box with listbox clicked
    def filout(self, event):
        # Delete whatever is in the entry box
        self.entry.delete(0, END)

        # Add clicked list item to entry box
        self.entry.insert(0, self.listitem.get(ANCHOR))

    # Create function to check entry vs listbox
    def check(self, event):
        # grab what was typed
        typed = self.entry.get()

        if typed == '':
            self.items_list = self.listitem
        else:
            self.items_list = []
            for item in self.listitem:
                if typed.lower() in item.lower():
                    self.items_list.append(item)

        # update our listbox with selected items
        self.update(self.items_list)


