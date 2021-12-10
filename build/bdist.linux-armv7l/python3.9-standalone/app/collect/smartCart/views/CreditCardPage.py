import tkinter as tk
from fpdf import FPDF
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import stripe
import firebase_admin
from firebase_admin import db

class CreditCardPage(tk.Tk):

    stripe.api_key = "sk_test_51JgORoCgya78u3nuoADgZ8R18wfqiurkW6zgW8dzdskkgUnK3y8nOwMg8p5LYEgxdAU4uP8ng0Nx4oxCRomo0PvO00YYqS6hQN"

    def connectWithDatabase(self):
        cred = firebase_admin.credentials.Certificate(
            "smart-shopping-cart-1fbac-firebase-adminsdk-wfobd-09a600f28a.json")
        # default_app = firebase_admin.initialize_app(cred, {
        #     'databaseURL': 'https://smart-shopping-cart-1fbac-default-rtdb.firebaseio.com/'
        # })
        self.ref = db.reference('items')

    def updateItemDataInInventory(self, itemCode):
        doc = self.ref.child(itemCode).get()
        if (doc != None):
            jsonObj = db.reference('items').child(itemCode).get()
            totalQuantity = jsonObj['quantity']
            totalQuantity -= 1
            print(db.reference('items').child(itemCode).get())
            db.reference('items').child(itemCode).update({'quantity': totalQuantity})
        else:
            return None

    def __init__(self,listItems,priceItems,totalPrice,itemCodesList):
        tk.Tk.__init__(self)
        self.geometry('650x450')
        self.configure(background="#353839")
        self.lblCreditPayment = tk.Label(text = "Credit Pay").place(x=300, y=50)
        self.lblCreditPayment
        self.cardnumlbl =tk.Label(text="Card_number").place(x=30, y=120)
        self.cardnum = tk.Text().place(x=150, y=120, width=180, height=25)
        self.listItems = listItems
        self.priceItems = priceItems
        self.totalPrice = totalPrice
        self.itemCodesList = itemCodesList
        self.connectWithDatabase()
        self.msg = MIMEMultipart()
        self.fromaddr = "choudharyanuj268@gmail.com"
        self.toaddr = "snazzytalks@gmail.com"
        self.btnCredit = tk.Button(text="Credit Card", background = "#a1caf1", command=lambda: self.payByCredit()).place(x=270, y=300)
        # variable pdf
        self.pdf = FPDF()
        self.now = datetime.now()
        self.dt_string = self.now.strftime("%d/%m/%Y %H:%M:%S")




    def payByCredit(self):
        print('Get data from Stripe project')
        self.chargeCard()
        self.sendPdfToUser()
        self.updateDatabase()


    def updateDatabase(self):
        for item in self.itemCodesList:
            print("Item code "+item)
            self.updateItemDataInInventory(item)


    def sendPdfToUser(self):
        self.makePdf()
        self.msg['From'] = self.fromaddr

        self.msg['To'] = self.toaddr

        self.msg['Subject'] = "Subject of the Mail"
        body = "Body_of_the_mail"

        self.msg.attach(MIMEText(body, 'plain'))

        filename = "GFG.pdf"
        attachment = open("./GFG.pdf", "rb")

        p = MIMEBase('application', 'octet-stream')

        p.set_payload((attachment).read())

        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # attach the instance 'p' to instance 'msg'
        self.msg.attach(p)

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(self.fromaddr, "tuqlmsmxjwzozxlf")

        text = self.msg.as_string()

        s.sendmail(self.fromaddr, self.toaddr, text)

        s.quit()
        print('PDF has been sent to user')


    def makePdf(self):
        # Add a page
        self.pdf.add_page()
        totalLines = 0
        # set style and size of font
        # that you want in the pdf
        self.pdf.set_font("Arial", size=15)
        # create a cell
        self.pdf.cell(200, 10, txt="Smart Cart Shopping Center",
                      ln=1, align='C')
        # add another cell
        self.pdf.cell(200, 10, txt="Transaction made at : "+self.dt_string,
                      ln=2, align='C')

        self.pdf.cell(200, 10, txt="User name", ln=3,
                      align='L')

        self.pdf.cell(200, 10, txt="User email", ln=4,
                      align='L')


        self.pdf.cell(200, 10, txt="Items : Price",ln=5,
                      align='L')
        for index, item in enumerate(self.listItems):
            self.pdf.cell(500,10,txt=""+str(self.listItems[index])+" : "+str(self.priceItems[index]),ln=6+index,align='L')
            totalLines=6+index


        self.pdf.cell(200, 10, txt="Total Price is : "+str(self.totalPrice),ln=totalLines+1,
                      align='L')
        self.pdf.output("GFG.pdf")


    def chargeCard(self):
        self.totalPrice = self.totalPrice+((13/100)*self.totalPrice)
        totalPayment = int(self.totalPrice)
        totalPayment = totalPayment*100
        tokenDetails = stripe.Token.create(
            card={
                "number": "4242424242424242",
                "exp_month": 8,
                "exp_year": 2023,
                "cvc": "878",
            },
        )
        chargeCard = stripe.Charge.create(
            amount=0,
            currency="cad",
            source=tokenDetails.stripe_id,
            description="My First Test Charge (created for API docs)",
        )
        print(tokenDetails.stripe_id)
        print(chargeCard)


# --- main ---

# win = ShoppingPage()
# win.mainloop()

# Window().mainloop()