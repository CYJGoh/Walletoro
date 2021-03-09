import locale
locale.setlocale( locale.LC_ALL, '' )


#For user to input the 1st person bill
def sbill_input():

    global price
    global tax
    global price_list
    global tprice
    
    price=float(input('Enter the your total bill: '))
    tax=float(input('Enter the amount of tax charged (in %): '))
    tprice=price+price*tax
    price_list=str(tprice).split(',')

    global choice
    choice=input('Do you wish to continue adding more bill? (Yes/No): ')

#For user if they wish to continue to add more bill
def sbill_cont():
    price=float(input('Enter another bill: '))
    tprice=str(price+price*tax)
    price_list.append(tprice)
    global choice
    choice=input('Do you wish to continue adding more bills? (Yes/No): ')
    
#Display the output after user decide to not continue
def sbill_output():
    count=0
    total=0
    print('Summary: \n')
    for item in price_list:
        count+=1
        item=float(item)
        print('Person',count,'required to pay', locale.currency(item))
        total+=item
    print('\nTotal bill:',locale.currency(total))
    print('Total tax charged:', locale.currency(total*tax))

#Actual flow of the program
sbill_input()
while choice!='no' or choice!='No':
    if choice=='yes' or choice=='Yes':
        sbill_cont()

    elif choice=='no' or choice=='No':
        sbill_output()
        print('That\'s all I can do. Have a nice day ahead!')
        break

    else:
        print('Invalid input. Please try again.')
        choice=input('Do you wish to continue adding more bills? (Yes/No): ')
