# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import datetime
import random
import time
import tkinter
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("1350x650+0+0")
root.title("Point On Sale System")

Tops = Frame(root, width=1350, height=100, bd=8, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)

f2 = Frame(root, width=440, height=650, bd=8, relief="raise")
f2.pack(side=RIGHT)

f1a = Frame(f1, width=900, height=330, bd=8, relief="raise")
f1a.pack(side=TOP)

f2a = Frame(f1, width=900, height=320, bd=8, relief="raise")
f2a.pack(side=BOTTOM)

f1aa = Frame(f1a, width=400, height=430, bd=8, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=400, height=430, bd=8, relief="raise")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width=450, height=330, bd=8, relief="raise")
f2aa.pack(side=LEFT)

f2ab = Frame(f2a, width=450, height=330, bd=8, relief="raise")
f2ab.pack(side=RIGHT)

lblInfo = Label(Tops, font=('Corbel', 60, 'bold'), text="                    Point On Sale System                    ",
                bd=10, anchor='w')
lblInfo.grid(row=0, column=0)

# Calc code part==========================================================================================================================


text_Input = StringVar()
operator = ""
PaymentRef = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
Burgers = StringVar()
Soda = StringVar()
Fries = StringVar()
HomeDelivery = StringVar()
CostofBurgers = StringVar()
CostofSoda = StringVar()
CostofFries = StringVar()
CostofDelivery = StringVar()
DateofOrder = StringVar()
# Sgst = (ToC * 2.5)/100
# Cgst = (ToC * 2.5)/100
# Gst = Sgst+Cgst


Burgers.set(0)
Soda.set(0)
Fries.set(0)
HomeDelivery.set(0)
DateofOrder.set(time.strftime("%d/%m/%Y"))


def CostOfOrder():
    BurgerPrice = float(Burgers.get())
    SodaPrice = float(Soda.get())
    FriesPrice = float(Fries.get())
    DeliveryCost = float(HomeDelivery.get())

    BurgerCost = "Rs.", str('%.2f' % (BurgerPrice * 70.00))
    CostofBurgers.set(BurgerCost)

    SodaCost = "Rs.", str('%.2f' % (SodaPrice * 40.00))
    CostofSoda.set(SodaCost)

    FriesCost = "Rs.", str('%.2f' % (FriesPrice * 50.00))
    CostofFries.set(FriesCost)

    DeliveryCharges = "Rs.", str('%.2f' % (DeliveryCost * 30.00))
    CostofDelivery.set(DeliveryCharges)

    ToC = "Rs.", str('%.2f' % ((BurgerPrice * 70.00) + (SodaPrice * 40.00) + (FriesPrice * 50)
                               + (DeliveryCost * 30)))
    SubTotal.set(ToC)

    gst = (0.025 + 0.025)
    Tax = "Rs", str(
        '%.2f' % (((BurgerPrice * 70.00) + (SodaPrice * 40.00) + (FriesPrice * 50) + (DeliveryCost * 30)) * gst))
    PaidTax.set(Tax)

    TaxPay = (((BurgerPrice * 70.00) + (SodaPrice * 40.00) + (FriesPrice * 50)
               + (DeliveryCost * 30)) * gst)

    Cost = ((BurgerPrice * 70.00) + (SodaPrice * 40.00) + (FriesPrice * 50)
            + (DeliveryCost * 30))

    CostOfItems = "Rs.", str('%.2f' % (TaxPay + Cost))

    TotalCost.set(CostOfItems)

    x = random.randint(10034, 699812)
    randomRef = str(x)
    PaymentRef.set("Bill" + randomRef)


def PayReference():
    x = random.randint(10034, 699812)
    randomRef = str(x)
    PaymentRef.set("Bill" + randomRef)


def i_Exit():
    qExit = messagebox.askyesno("Billing System", "Do You Want To Exit The System")
    if qExit > 0:
        root.destroy()
        return ()


def I_Reset():
    PaymentRef.set("")
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    Burgers.set(0)
    Soda.set(0)
    Fries.set(0)
    HomeDelivery.set(0)
    CostofBurgers.set("")
    CostofSoda.set("")
    CostofFries.set("")
    CostofDelivery.set("")


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""


txtDisplay = Entry(f2, font=('Corbel', 20, 'bold'), textvariable=text_Input,
                   bd=40, insertwidth=6, justify='right')
txtDisplay.grid(columnspan=4)
# First Row Buttons :----------------------------------------------------------------------------------------------------------------------
btn7 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 18, 'bold'),
              text="7", command=lambda: btnClick(7)).grid(row=1, column=0)
btn8 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 18, 'bold'),
              text="8", command=lambda: btnClick(8)).grid(row=1, column=1)
btn9 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 18, 'bold'),
              text="9", command=lambda: btnClick(9)).grid(row=1, column=2)
btnPlus = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 18, 'bold'),
                 text="+", command=lambda: btnClick("+")).grid(row=1, column=3)
# Second Row Buttons -----------------------------------------------------------------------------------------------------------------------
btn4 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 18, 'bold'),
              text="4", command=lambda: btnClick(4)).grid(row=3, column=0)
btn5 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 18, 'bold'),
              text="5", command=lambda: btnClick(5)).grid(row=3, column=1)
btn6 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 18, 'bold'),
              text="6", command=lambda: btnClick(6)).grid(row=3, column=2)
btnMin = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 18, 'bold'),
                text="-", command=lambda: btnClick("-")).grid(row=3, column=3)
# Third Row Buttons--------------------------------------------------------------------------------------------------------------------------
btn1 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 18, 'bold'),
              text="1", command=lambda: btnClick(1)).grid(row=4, column=0)
btn2 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 18, 'bold'),
              text="2", command=lambda: btnClick(2)).grid(row=4, column=1)
btn3 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 18, 'bold'),
              text="3", command=lambda: btnClick(3)).grid(row=4, column=2)
btnMul = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 18, 'bold'),
                text="*", command=lambda: btnClick("*")).grid(row=4, column=3)
# fourth Row Buttons :-----------------------------------------------------------------------------------------------------------------------
btn0 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 18, 'bold'),
              text="0", command=lambda: btnClick(0)).grid(row=5, column=0)
btnClr = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 18, 'bold'),
                text="C", command=btnClearDisplay).grid(row=5, column=1)
btnEql = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 18, 'bold'),
                text="=", command=btnEqualsInput).grid(row=5, column=2)
btnDiv = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 18, 'bold'),
                text="/", command=lambda: btnClick("/")).grid(row=5, column=3)

# End Of Calc ----------------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------Order info for f11----------------------------------------------------

lblRef = Label(f1aa, font=('Corbel', 20, 'bold'), text="Sales Reference", bd=16,
               justify='left')
lblRef.grid(row=0, column=0)
textRef = Entry(f1aa, font=('Corbel', 20, 'bold'),
                textvariable=PaymentRef, bd=10, insertwidth=2, justify='left')
textRef.grid(row=0, column=1)
# --------------------------------
lblBurgers = Label(f1aa, font=('Corbel', 20, 'bold'), text="Burgers", bd=16,
                   justify='left')
lblBurgers.grid(row=1, column=0)
textBurgers = Entry(f1aa, font=('Corbel', 20, 'bold'),
                    textvariable=Burgers, bd=10, insertwidth=2, justify='left')
textBurgers.grid(row=1, column=1)
# ----------------------------------
lblSoda = Label(f1aa, font=('Corbel', 20, 'bold'), text="Soda", bd=16,
                justify='left')
lblSoda.grid(row=2, column=0)
textSoda = Entry(f1aa, font=('Corbel', 20, 'bold'),
                 textvariable=Soda, bd=10, insertwidth=2, justify='left')
textSoda.grid(row=2, column=1)
# -----------------------------------
lblFries = Label(f1aa, font=('Corbel', 20, 'bold'), text="Fries", bd=16,
                 justify='left')
lblFries.grid(row=3, column=0)
textFries = Entry(f1aa, font=('Corbel', 20, 'bold'),
                  textvariable=Fries, bd=10, insertwidth=2, justify='left')
textFries.grid(row=3, column=1)
# ----------------------------------
lblHomeDelivery = Label(f1aa, font=('Corbel', 20, 'bold'), text="Home Delivery", bd=16,
                        justify='left')
lblHomeDelivery.grid(row=4, column=0)
textHomeDelivery = Entry(f1aa, font=('Corbel', 20, 'bold'),
                         textvariable=HomeDelivery, bd=10, insertwidth=2, justify='left')
textHomeDelivery.grid(row=4, column=1)
# ------------------------------Order Billing System here----------------------
lblDateofOrder = Label(f1ab, font=('Corbel', 20, 'bold'), text="Date Of Order", bd=16,
                       justify='left')
lblDateofOrder.grid(row=0, column=0)
textDateofOrder = Entry(f1ab, font=('Corbel', 20, 'bold'),
                        textvariable=DateofOrder, bd=10, insertwidth=2, justify='left')
textDateofOrder.grid(row=0, column=1)
# --------------------------------
lblCostofBurgers = Label(f1ab, font=('Corbel', 20, 'bold'), text="Cost of Burgers", bd=16,
                         justify='left')
lblCostofBurgers.grid(row=1, column=0)
textCostofBurgers = Entry(f1ab, font=('Corbel', 20, 'bold'),
                          textvariable=CostofBurgers, bd=10, insertwidth=2, justify='left')
textCostofBurgers.grid(row=1, column=1)
# ----------------------------------
lblCostofSoda = Label(f1ab, font=('Corbel', 20, 'bold'), text="Cost of Soda", bd=16,
                      justify='left')
lblCostofSoda.grid(row=2, column=0)
textCostofSoda = Entry(f1ab, font=('Corbel', 20, 'bold'),
                       textvariable=CostofSoda, bd=10, insertwidth=2, justify='left')
textCostofSoda.grid(row=2, column=1)
# -----------------------------------
lblCostofFries = Label(f1ab, font=('Corbel', 20, 'bold'), text="Cost of Fries", bd=16,
                       justify='left')
lblCostofFries.grid(row=3, column=0)
textCostofFries = Entry(f1ab, font=('Corbel', 20, 'bold'),
                        textvariable=CostofFries, bd=10, insertwidth=2, justify='left')
textCostofFries.grid(row=3, column=1)
# ----------------------------------
lblCostofDelivery = Label(f1ab, font=('Corbel', 20, 'bold'), text="Cost of Home Delivery", bd=16,
                          justify='left')
lblCostofDelivery.grid(row=4, column=0)
textCostofDelivery = Entry(f1ab, font=('Corbel', 20, 'bold'),
                           textvariable=CostofDelivery, bd=10, insertwidth=2, justify='left')
textCostofDelivery.grid(row=4, column=1)

# ---------------------------------Order Of f2aa-----------------------------------------------


# -------------------------------------
lblPaidTax = Label(f2aa, font=('Corbel', 20, 'bold'), text="Paidtax", bd=8,
                   anchor='w')
lblPaidTax.grid(row=2, column=0)
textPaidTax = Entry(f2aa, font=('Corbel', 20, 'bold'),
                    textvariable=PaidTax, bd=10, insertwidth=2, justify='left')
textPaidTax.grid(row=2, column=1)
# -------------------------------------
lblSubTotal = Label(f2aa, font=('Corbel', 20, 'bold'), text="Subtotal", bd=8,
                    anchor='w')
lblSubTotal.grid(row=3, column=0)
textSubTotal = Entry(f2aa, font=('Corbel', 20, 'bold'),
                     textvariable=SubTotal, bd=10, insertwidth=2, justify='left')
textSubTotal.grid(row=3, column=1)
# -------------------------------------
lblTotalCost = Label(f2aa, font=('Corbel', 20, 'bold'), text="Total Cost", bd=8,
                     anchor='w')
lblTotalCost.grid(row=4, column=0)
textTotalCost = Entry(f2aa, font=('Corbel', 20, 'bold'),
                      textvariable=TotalCost, bd=10, insertwidth=2, justify='left')
textTotalCost.grid(row=4, column=1)

# ---------------------------------Order Info Buttons-------------------------------

btnTotal = Button(f2ab, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 20, 'bold'),
                  width=15, text="Total Cost", command=CostOfOrder).grid(row=0, column=0)
btnRefer = Button(f2ab, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 20, 'bold'),
                  width=15, text="Sales Reference", command=PayReference).grid(row=0, column=1)
btnReset = Button(f2ab, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 20, 'bold'),
                  width=15, text="Reset", command=I_Reset).grid(row=1, column=0)
btnExit = Button(f2ab, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 20, 'bold'),
                 width=15, text="Exit", command=i_Exit).grid(row=1, column=1)

root.mainloop()
