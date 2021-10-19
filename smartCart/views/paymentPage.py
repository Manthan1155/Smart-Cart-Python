import tkinter as tk
from tkinter import ANCHOR
from tkinter.messagebox import showinfo

import firebase as firebase
import firebase_admin
from firebase_admin import credentials
from numpy.core import double
from pyasn1.compat.octets import null
from pyrebase import pyrebase
from firebase_admin import db
import geocoder

from views.CreditCardPage import *
from views.shoppingPage import *


class PaymentPage(tk.Tk):


    def connectWithDatabase(self):
        cred = firebase_admin.credentials.Certificate("smart-shopping-cart-1fbac-firebase-adminsdk-wfobd-09a600f28a.json")
        default_app = firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://smart-shopping-cart-1fbac-default-rtdb.firebaseio.com/'
        })
        self.ref = db.reference('items')




    def checkItemInTheInventory(self,itemCode):

        doc = self.ref.child(itemCode).get()
        print(doc)
        if(doc != None):
            return db.reference('items').child(itemCode).get()
        else:
            return None

    def __init__(self,listItem,priceItem,totalPrice,itemCodesList):
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.listItems = listItem
        self.priceItems = priceItem
        self.totalPrice = totalPrice
        self.itemCodesList = itemCodesList
        self.btnCredit = tk.Button(text="Credit Card", command = lambda : self.goToCredit()).grid()




    def goToCredit(self):
        self.destroy()
        CreditCardPage(self.listItems,self.priceItems, self.totalPrice, self.itemCodesList)


# --- main ---

#win = ShoppingPage()
#win.mainloop()

#Window().mainloop()