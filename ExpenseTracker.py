from tabulate import tabulate
#Tabulate module is to tabulate the data into a table format
import datetime
import os


filename = 'budget.txt'
dataDir = 'data'
dt = datetime.datetime.now()
results = []
#Allows user to select a function.
def main():
    end = 'no'
    totalbudget = 0
    while end == 'no':
        print('\nExpense Tracker Program')
        print('Menu:')
        print('1. Add Expense: ')
        print('2. Add Revenue: ')
        print('3. Check Balance: ')
        print('4. Edit Expense: ')
        print('5. Save Your Progress: ')
        print('6. Exit Program ')

        selection = int(input('Enter Your Selection: '))
        if selection == 1:
            totalbudget = expense(totalbudget)
        elif selection == 2:
            totalbudget = revenue(totalbudget)
        elif selection == 3:
            print('Your Balance Is RM{0}'.format(totalbudget))
            print(tabulate(results))
        elif selection == 4:
            print(tabulate(results))
            selection = int(input('Enter Which Item You Wish To Delete (0 Is The First Item): '))
            results.remove(results[selection])
        elif selection == 5:
            save(totalbudget)
            print('Your Progress Has Been Saved')
        elif selection == 6:
            end = 'yes'
            print('Program Will Be Closed')
        else:
            print('Invalid Input. Try Again')
            
#Function that allows users to add expenses.
def expense(totalbudget):
    global exp
    global category
    global date
    global description
    global results
    exp = (float(input('Enter Your Amount: RM ')))
    
    totalbudget -= exp
    category = input('Enter A Category: ')
    date=input('Enter Date (DD/MM/YY): ')
    description = input('Enter Description Of Expense: ')
    exp=str(exp)
    category=str(category)
    date=str(date)
    description=str(description)
    results.append([exp,category,date,description])

    choice = input('Do You Wish To Continue To Add More Expenses? (Yes/No): ')
    while choice != 'no' or choice != 'No':
        if choice == 'yes' or choice == 'Yes':
                exp = (float(input('Enter Your Amount: RM ')))
                totalbudget -= exp
                category = input('Enter A Category: ')
                date=input('Enter Date (DD/MM/YY): ')
                description = input('Enter Description Of Expense: ')
                exp=str(exp)
                category=str(category)
                date=str(date)
                description=str(description)
                results.append([exp,category,date,description])

                choice = input('Do You Wish To Continue To Add More Expenses? (Yes/No): ')

        elif choice == 'no' or choice == 'No':
            print(tabulate(results))
            print('Your remaining budget is: {0}'.format(totalbudget))
            return totalbudget
        else:
            print('Invalid Input. Try Again.')
            choice = input('Do You Wish To Continue To Add More Expenses? (Yes/No): ')            

#Function to allow users to add revenue.            
def revenue(totalbudget):
    rev = (float(input('Enter Your Revenue: RM ')))
    totalbudget = totalbudget + rev
    print('Your New Budget: {0}'.format(totalbudget))
    return totalbudget


#Function that formats how the data will be saved in the text file.
def save(totalbudget):
    with open('data/budget.txt', 'a') as f:
        f.write('Last saved: ')
        f.write(str(dt))
        f.write('\r\n')
        f.write(tabulate(results))
        f.write('\r\n')
        f.write(str(totalbudget))
        f.write('\r\n')
    f.close()


def get_file_path(filename):
    currenDirPath = os.getcwd()
    filepath = os.path.join(currenDirPath, dataDir, filename)
    return filepath

def readBudget(file_path):
    with open(file_path, 'r') as f:
        cBudget = f.read()
        return cBudget

path = get_file_path(filename)
currentBudget = readBudget(path)

if __name__ == '__main__':
    readBudget(path)


main()


    
            
    
        
        
            
    
    

        
