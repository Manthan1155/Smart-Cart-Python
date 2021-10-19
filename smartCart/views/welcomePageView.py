import tkinter as tk

from self import self

from views.shoppingPage import *


class WelcommePage(tk.Tk,tk.Toplevel):
    def __init__(self):
        tk.Tk.__init__(self)

        self.geometry('500x500')
        self.label = tk.Label(self, text="Welcome to Smart Cart")
        self.label.grid()
        self.btnStart = tk.Button(self, text="Start", command = lambda : self.goToShoppingPage()).grid()

    def goToShoppingPage(self):
        self.destroy()
        ShoppingPage()



# --- main ---

win = WelcommePage()

win.mainloop()