import subprocess
import tkinter as tk
from email.mime import message
from tkinter import ANCHOR
from tkinter.messagebox import showinfo
import time
import firebase_admin
import self as self

from firebase_admin import db

# from smartCart.views import weight
import smartCart.views.shoppingPage
# from smartCart.views import weight
from smartCart.views.paymentPage import PaymentPage
from smartCart.views.ProductMap import ProductMap


class ShoppingPage(tk.Tk):

    def connectWithDatabase(self):
        cred = firebase_admin.credentials.Certificate(
            "smart-shopping-cart-1fbac-firebase-adminsdk-wfobd-09a600f28a.json")
        default_app = firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://smart-shopping-cart-1fbac-default-rtdb.firebaseio.com/'
        })
        self.ref = db.reference('items')

    def checkItemInTheInventory(self, itemCode):
        doc = self.ref.child(itemCode).get()
        print(doc)
        if (doc != None):
            return db.reference('items').child(itemCode).get()
        else:
            return None

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('650x450')
        self.configure(background="#353839")
        self.newItem = ''
        self.connectWithDatabase()
        self.totalPrice: float = 0.0
        print(type(self.totalPrice))
        self.itemsArray = []
        self.priceArray = []
        self.itemCodeArray = []
        self.lblItemsInTheCart = tk.Label(text="Items in the cart", background="#353839", foreground="white")
        self.listItem = tk.Listbox(self)
        self.listItem.place(x=50, y=50, width=200)
        self.priceList = tk.Listbox(self)
        self.priceList.place(x=350, y=50, width=100)

        self.lblTotalPrice = tk.Label(self, background="#a1caf1", text='$ ' + str(self.totalPrice))
        self.lblTotalPrice.place(x=400, y=280)
        self.btnClearAll = tk.Button(self, text="Clear All Items", background="#a1caf1",
                                     command=lambda: self.clearAllItem()).place(x=200, y=280)
        self.btnRemoveItem = tk.Button(self, text="Remove Item", background="#a1caf1",
                                       command=lambda: self.removeItem()).place(x=50, y=280)
        self.btnHelp = tk.Button(self, text="Help", background="#a1caf1", command=lambda: self.helpCall()).place(x=50,
                                                                                                                 y=350)
        self.btnProductMap = tk.Button(self, text="Product Map", background="#a1caf1",
                                       command=lambda: self.productMap()).place(x=200, y=350)
        self.btnFinish = tk.Button(self, text="Finish", background="#a1caf1", command=lambda: self.paymentPage()).place(
            x=350, y=350)

        self.bind('<Key>', self.addNewItemInTheList)

    # subprocess.PIPE(weight.py)

    def weightcheck(self, itemweight):
        cnt = len(self.itemsArray)
        up = cnt + (cnt * 0.35)
        low = cnt - (cnt * 0.35)
        # weight_new = weight.weight
        # if(low >= weight_new or up <= weight_new):
        #    message.alert()
        print(up)
        print(low)
        print(cnt)

    # print(cartweight)

    def addNewItemInTheList(self, event):
        if event.char in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            self.newItem += event.char

        elif event.keysym == 'Return':
            print(self.newItem)
            if (self.checkItemInTheInventory(self.newItem) != None):
                jsonObj = self.checkItemInTheInventory(self.newItem)
                self.addItem(jsonObj['name'], jsonObj['price'])
                self.weightcheck(jsonObj['weight'])

            else:
                self.newItem = ''
                showinfo('Not Found !', 'This item is not available here')

    def addItem(self, itemName, itemPrice):

        self.listItem.insert(tk.END, itemName)
        self.priceList.insert(tk.END, itemPrice)
        self.totalPrice = self.totalPrice + float(itemPrice)
        self.itemsArray.append(itemName)
        self.priceArray.append(itemPrice)
        self.itemCodeArray.append(self.newItem)
        self.updatePriceLbl()
        self.lblTotalPrice.config(text=str(self.totalPrice))
        self.newItem = ''

        # self.weightcheck()

    def paymentPage(self):
        self.destroy()
        print(self.itemsArray)
        print(self.priceArray)
        PaymentPage(self.itemsArray, self.priceArray, self.totalPrice, self.itemCodeArray)

    def updatePriceLbl(self):
        self.lblTotalPrice.config(text="$ " + str(self.totalPrice))

    # def helpCall(self):

    def productMap(self):
        # self.destroy()
        ProductMap()

    def removeItem(self):
        selection = self.listItem.curselection()
        selection = str(selection)
        idx = int(selection[1])
        print("Currently removing : " + str(idx))
        self.listItem.delete(idx)
        self.itemsArray.pop(idx)
        self.priceArray.pop(idx)
        self.itemCodeArray.pop(idx)
        itemPrice = self.priceList.get(idx)
        self.totalPrice = self.totalPrice - float(itemPrice)
        self.priceList.delete(idx)
        self.updatePriceLbl()

    def clearAllItem(self):
        self.listItem.delete(0, self.listItem.size() - 1)
        self.priceList.delete(0, self.priceList.size() - 1)
        self.totalPrice = 0.0
        self.updatePriceLbl()
