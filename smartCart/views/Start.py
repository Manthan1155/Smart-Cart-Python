import tkinter as tk

from smartCart.views.welcomePageView import WelcommePage
from PIL import Image, ImageTk

class Start(tk.Tk, tk.Toplevel):

    def __init__(self):
        tk.Tk.__init__(self)
        global img
        self.geometry('650x450')
        self.configure(background="#353839")
        self.myimg = ImageTk.PhotoImage(Image.open("logo.jpeg"))
        self.mylabel = tk.Label(image=self.myimg)
        self.mylabel.pack()
        font_label = ("Comic Sans MS", 18, "bold")
        font_label2 = ("Comic Sans MS", 16, "bold")
        self.label = tk.Label(self, text="Smart Shopping Cart")
        self.label.place(x=220, y=150)
        self.label.pack()
        self.label2 = tk.Label(self, text="Devloped by : \n\n Hitarth Bhavsar \n Manthan Patel \n Kalp Patel", background="#353939", foreground="white", font=font_label2)
        self.label2.place(x=50, y=250)
        self.label2.pack()
        self.label3= tk.Label(self, text="\nUnder Guidance of : \n\n Prof. Weijing Ma \n Prof. Ning Zhu", background="#353939", foreground="white", font=font_label2)
        self.label3.place(x=350, y=250)
        self.label3.pack()
        self.label.configure(font=font_label, background="#353839", foreground="white")
        self.btnStart = tk.Button(self, background="#a1caf1", width=20, text="Start", command=lambda: self.goToWelcomePageView()).place(x=250, y=420)






    def goToWelcomePageView(self):
        self.destroy()
        WelcommePage()



win = Start()

win.mainloop()
