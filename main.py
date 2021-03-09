from tkinter import * 

gui = Tk()

def tbill():
    import tbill_splitter

def sbill():
    import sbill_splitter

def Calculator():
    import calculator

def cashflow():
    import MinCashFlow

def expense():
    import ExpenseTracker

#Initialise gui
topframe = Frame(gui,bg='lemon chiffon')
topframe.pack()
bottomframe = Frame(gui,bg='lemon chiffon')
bottomframe.pack()
gui.iconbitmap(r'images/money-bag.ico')
gui.title('Walletoro')
gui.geometry('600x600')
gui.configure(bg='lemon chiffon')

#GUI design
logo = PhotoImage(file='images/money-bag.png')
logoimg = Label(topframe, image=logo,bg='lemon chiffon')
logoimg.pack(pady=10)
name = Label(topframe,text='Walletoro',font=('Helvetica',20,'bold'),fg='green4',bg='lemon chiffon')
name.pack(pady=5)

tag = Label(topframe,text='Get your financial problems sorted here',font=('Helvetica',15,'bold'),fg='green4',bg='lemon chiffon')
tag.pack()

instruc = Label(bottomframe,text='Please select the service that you wish use',font=('Helvetica',13,'bold'),fg='green4',bg='lemon chiffon')
instruc.pack()

button1 = Button(bottomframe,text='Total Bill Splitter',font=('Helvetica',11,'bold'),borderwidth=0,fg='white',bg='green3',width=20,command=tbill)
button1.pack(pady=5)

button1 = Button(bottomframe,text='Individual Bill Splitter',font=('Helvetica',11,'bold'),borderwidth=0,fg='white',bg='green3',width=20,command= sbill)
button1.pack(pady=5)

button1 = Button(bottomframe,text='Minimum Cash Flow \nDebt Payment',font=('Helvetica',11,'bold'),borderwidth=0,fg='white',bg='green3',width=20,height=2,command= cashflow)
button1.pack(pady=5)

button1 = Button(bottomframe,text='Expense Tracker',font=('Helvetica',11,'bold'),borderwidth=0,fg='white',bg='green3',width=20,command=expense)
button1.pack(pady=5)

calculator = Button(bottomframe,text='Calculator',font=('Helvetica',11,'bold'),borderwidth=0,fg='white',bg='green3',width=20,command= Calculator)
calculator.pack(pady=5)

button1 = Button(bottomframe,text='Quit',font=('Helvetica',11,'bold'),borderwidth=0,fg='white',bg='red',width=20,command= quit)
button1.pack(pady=5)


#Driver code
gui.mainloop()
