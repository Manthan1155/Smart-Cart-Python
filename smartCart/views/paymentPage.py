import tkinter as tk
import firebase_admin

from firebase_admin import db

from smartCart.views.CreditCardPage import CreditCardPage


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
        self.geometry('650x450')
        self.configure(background="#353839")
        font_label = ("Comic Sans MS", 18, "bold")
        self.listItems = listItem
        self.priceItems = priceItem
        self.totalPrice = totalPrice
        self.itemCodesList = itemCodesList
        self.optlbl = tk.Label(text="Select your Payment Option", font=font_label).place(x=150, y=200)
        self.btnCredit = tk.Button(text="Credit Card", background = "#a1caf1", command = lambda : self.goToCredit()).place(x=300, y=400)




    def goToCredit(self):
        self.destroy()
        CreditCardPage(self.listItems,self.priceItems, self.totalPrice, self.itemCodesList)


# --- main ---

#win = ShoppingPage()
#win.mainloop()

#Window().mainloop()