import tkinter as tk

from smartCart.views.shoppingPage import ShoppingPage


# from smartCart.views.hx711py import example

class WelcommePage(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('650x450')
        self.configure(background="#353839")
        self.label = tk.Label(self, text="Welcome to Smart Cart")
        self.label.place(x=150, y=150)
        font_label = ("Comic Sans MS", 28, "bold")
        self.label.configure(font = font_label, background="#353839", foreground="white")
        self.btnStart = tk.Button(self, background = "#a1caf1", width=20, text="Start", command = lambda : self.goToShoppingPage()).place(x=250, y=250)

      #  self.btnStart.pack(fill = BOTH, expand = TRUE)

    def goToShoppingPage(self):
        self.destroy()
        ShoppingPage()






