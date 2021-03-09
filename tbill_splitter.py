import locale
locale.setlocale( locale.LC_ALL, '' )


price = 0.0
tip = 0.0
total = 0.0
payment = 0.0
split = 0
    

#For user to input their total bill 
def tbill_input():
    global price
    global tip
    global tax_amount
    global split
    
    price = float(input('Enter your total bill: '))
    tip = float(input('Enter amount of tip gave: '))
    tax_amount = float(input('Enter the amount of tax charged (in %): '))
    split = int(input('Enter at how many persons split a bill: '))

#Calculations to split evenly depending on the number of persons to split
def tbill_calc():
    global taxcost
    global payment
    total = price+tip+(price*tax_amount)
    taxcost=price*tax_amount
    payment = total/split
    return payment
    return taxcost

#Display the output of each person's required payment
def tbill_output():
    print('Each person is required to pay:', locale.currency(payment))
    print('Your amount of tax paid is',locale.currency(taxcost),'\n')

    global cont
    cont=input('Do you wish you continue (Yes/No): ')
    return cont

#The actual flow of program
tbill_input()
tbill_calc()
tbill_output()

while cont!='no' or cont!='No':
    if cont=='yes' or cont=='Yes':
        tbill_input()
        tbill_calc()
        tbill_output()

    elif cont=='no' or cont=='No':
        print('Alright, roger that!')
        break

    else:
        print('Invalid input. Please try again.')
        cont=input('Do you wish you continue (Yes/No): ')
