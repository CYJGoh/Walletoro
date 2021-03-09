import locale
locale.setlocale(locale.LC_ALL,'')

#Return the index of minimum value
def getMin(arr): 
      
    minInd = 0
    for i in range(1, N): 
        if (arr[i] < arr[minInd]): 
            minInd = i 
    return minInd 

#Return the index of maximum value  
def getMax(arr): 
  
    maxInd = 0
    for i in range(1, N): 
        if (arr[i] > arr[maxInd]): 
            maxInd = i 
    return maxInd 

#To find the minimum value of 2 values  
def minOf2(x, y):
    if x < y:
        return x
    else:
        return y


def minCashFlowRec(amount): 
  
#Max creditor has the max net amount 
    mxCredit = getMax(amount)
#Max debitor has the least net amount
    mxDebit = getMin(amount) 
  
#If both amounts are 0, then all amounts are settled
    if (amount[mxCredit] == 0 and amount[mxDebit] == 0): 
        return 0

#To find minimum value of the 2  
    Min = minOf2(-amount[mxDebit], amount[mxCredit]) 
    amount[mxCredit] -= Min
    amount[mxDebit] += Min
  
    print("Person " , str(mxDebit+1) , " pays" , locale.currency(Min)
        , " to " , "Person " , str(mxCredit+1))

#Repeat this calculation until amount[maxCredit] or amount[maxDebit] becomes 0  
    minCashFlowRec(amount) 

#To find and print the minimum cash flow   
def minCashFlow(graph): 

#Create an array amount[] and initialise all value to 0
    amount = [0 for i in range(N)] 

#Calculate the net amount to be paid by person p and stores it in amount[p]  
    for p in range(N): 
        for i in range(N): 
            amount[p] += (graph[i][p] - graph[p][i]) 
  
    minCashFlowRec(amount) 

#Prompt user to input amount of people involved
N = int(input('Enter the number of people involved: '))
count=0

#Allow user to add the person's debts according the number of people involved
graph=[]
while count<N:
    a=input('Enter the amount each person should pay to every person involved in sequence(seperated by comma): ').split(',')
    count += 1
    person_list=list(map(float,a))
    graph.append(person_list)
    
minCashFlow(graph) 
