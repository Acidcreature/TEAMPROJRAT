# This program is the GUI from the POS system. The basic layout came from ____________________________*******************__________________.com

# import all the things
import datetime
import random
import time
import tkinter
from tkinter import *
from tkinter import messagebox
# set root to be tkinter
root = Tk()
# set the size of the window
root.geometry("1920x1080+0+0")
#define the title
root.title("POS Point OF Sale System")
# Build all the frames within the frame
Tops = Frame(root, width=1350, height=100, bd=8, relief="raise")
Tops.pack(side=TOP)
f1 = Frame(root, width=900, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)
f2 = Frame(root, width=540, height=650, bd=8, relief="raise")
f2.pack(side=RIGHT)
f1a = Frame(f1, width=900, height=330, bd=8, relief="raise")
f1a.pack(side=TOP)
f2a = Frame(f1, width=900, height=320, bd=8, relief="raise")
f2a.pack(side=BOTTOM)
f1aa = Frame(f1a, width=400, height=430, bd=8, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=400, height=430, bd=8, relief="raise")
f1ab.pack(side=RIGHT)
f2aa = Frame(f2a, width=550, height=330, bd=8, relief="raise")
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=550, height=330, bd=8, relief="raise")
f2ab.pack(side=RIGHT)
# Label for the top of the POS system
lblInfo = Label(Tops, font=('Corbel', 60, 'bold'), text="                    Point OF Sale System                    ",
                bd=10, anchor='w')
lblInfo.grid(row=0, column=0)

# Calc code part==========================================================================================================================

# set variables to hold string variables
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
#set the other variables to hold values
Burgers.set(0)
Soda.set(0)
Fries.set(0)
HomeDelivery.set(0)
# use the date time thing to set the date time thing
DateofOrder.set(time.strftime("%d/%m/%Y"))
# define the function to get the cost of the order
def CostOfOrder():
    # set the variables to get the price of the input on the POS system
    BurgerPrice = float(Burgers.get())
    SodaPrice = float(Soda.get())
    FriesPrice = float(Fries.get())
    DeliveryCost = float(HomeDelivery.get())
    # Set the cost of the item to be the number of item times the price
    BurgerCost = "$" + str('%.2f' % (BurgerPrice * 5.80))
    CostofBurgers.set(BurgerCost)
    # Set the cost of the item to be the number of item times the price
    SodaCost = "$" + str('%.2f' % (SodaPrice * 2.50))
    CostofSoda.set(SodaCost)
    # Set the cost of the item to be the number of item times the price
    FriesCost = "$" + str('%.2f' % (FriesPrice * 3.00))
    CostofFries.set(FriesCost)
    # Set the cost of the item to be the number of item times the price
    DeliveryCharges = "$" + str('%.2f' % (DeliveryCost * 10.00))
    CostofDelivery.set(DeliveryCharges)
    # Set the cost of the item to be the number of item times the price
    ToC = "$" +  str('%.2f' % ((BurgerPrice * 5.80) + (SodaPrice * 2.50) + (FriesPrice * 3.00)
                               + (DeliveryCost * 10.00)))
    SubTotal.set(ToC)
    # set the tax rate
    gst = (0.0625)
    # set the cost of the tax based off the number of items selected times the tax
    Tax = "$" + str(
        '%.2f' % (((BurgerPrice * 5.80) + (SodaPrice * 2.50) + (FriesPrice * 3.00) + (DeliveryCost * 10.00)) * gst))
    PaidTax.set(Tax)
    # set the price of tax to pay
    TaxPay = (((BurgerPrice * 5.80) + (SodaPrice * 2.50) + (FriesPrice * 3.00)
               + (DeliveryCost * 10.00)) * gst)
    # set the cost
    Cost = ((BurgerPrice * 5.80) + (SodaPrice * 2.50) + (FriesPrice * 3.00)
            + (DeliveryCost * 10.00))
    # get the total cost and then set it
    CostOfItems = "$" + str('%.2f' % (TaxPay + Cost))
    TotalCost.set(CostOfItems)
    # set the customer/payment reference using randint
    x = random.randint(10034, 699812)
    randomRef = str(x)
    PaymentRef.set("Bill" + randomRef)
# define the par reference function
def PayReference():
     # set the customer/payment reference using randint
    x = random.randint(10034, 699812)
    randomRef = str(x)
    PaymentRef.set("Bill" + randomRef)
# define the function to exit
def i_Exit():
    # call a prompt asking if they want to exit if yes then destroy the POS thing
    qExit = messagebox.askyesno("Billing System", "Do You Want To Exit The System")
    if qExit > 0:
        root.destroy()
        return ()
# Define the funciton to reset all the values
def I_Reset():
    # set the values back to the default values
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
# Define the function to set the input to show what buttons the user presses
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)
# Defind the function to set the input fields back to default values
def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")
# Define the funciton that will add the things all together
def btnEqualsInput():
    global operator
    if str(operator) == '88224646ba':
        qprompt = messagebox.askokcancel('lives','You have unlocked 30 lives')
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""
# define the function to show the display that text gets put into
txtDisplay = Entry(f2, font=('Corbel', 20, 'bold'), textvariable=text_Input,
                   bd=40, insertwidth=8, justify='right')
txtDisplay.grid(columnspan=5)
# Define the buttons on the calculator 
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
btna = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 18, 'bold'),
              text="a", command=lambda: btnClick('a')).grid(row=1, column=4)
btnb = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 18, 'bold'),
                text="b", command=lambda: btnClick("b")).grid(row=3, column=4)
btnc = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 18, 'bold'),
                text="c", command=lambda: btnClick("c")).grid(row=4, column=4)
btndot = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 18, 'bold'),
                text=".", command=lambda: btnClick(".")).grid(row=5, column=4)
# --------------------------------------------------------------------------------Order info for f11----------------------------------------------------
# Define the inputs and stuff for the items the customer can order
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
lblSoda = Label(f1aa, font=('Corbel', 20, 'bold'), text="Litres of Cola", bd=16,
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
lblCostofSoda = Label(f1ab, font=('Corbel', 20, 'bold'), text="Cost of Litres of Cola", bd=16,
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
# Define the fields to get the tax and subtotal and the total cost
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
# Define the buttons to get the things like exit and cost and reset and payreference
# ---------------------------------Order Info Buttons-------------------------------
btnTotal = Button(f2ab, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 20, 'bold'),
                  width=15, text="Total Cost", command=CostOfOrder).grid(row=0, column=0)
btnRefer = Button(f2ab, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 20, 'bold'),
                  width=15, text="Sales Reference", command=PayReference).grid(row=0, column=1)
btnReset = Button(f2ab, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 20, 'bold'),
                  width=15, text="Reset", command=I_Reset).grid(row=1, column=0)
btnExit = Button(f2ab, padx=16, pady=16, bd=8, fg="black", font=('Corbel', 20, 'bold'),
                 width=15, text="Exit", command=i_Exit).grid(row=1, column=1)
# Call the mainloop to start the thing
root.mainloop()