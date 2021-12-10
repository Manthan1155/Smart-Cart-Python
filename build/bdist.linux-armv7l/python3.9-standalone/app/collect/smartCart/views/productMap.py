# import tkinter as tk
# from tkinter import ANCHOR
# from tkinter.messagebox import showinfo
#
# import firebase_admin
#
# from firebase_admin import db
#
#
# class ProductMap(tk.Tk):
#
#     def connectWithDatabase(self):
#         cred = firebase_admin.credentials.Certificate("smart-shopping-cart-1fbac-firebase-adminsdk-wfobd-09a600f28a.json")
#         default_app = firebase_admin.initialize_app(cred, {
#             'databaseURL': 'https://smart-shopping-cart-1fbac-default-rtdb.firebaseio.com/'
#         })
#         self.ref = db.reference('items')
#
#
#     def __init__(self):
#         tk.Tk.__init__(self)
#
#         self.geometry('500x500')
#         self.label = tk.Label(self, text="What aisle are you in?")
#         self.label.grid()