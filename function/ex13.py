amount=15000
def balancecheck():
    print('Current amount is:',amount)
def deposit(amt):
    global amount
    amount=amount+amt
    print(amt,'Deposit Tx done & update balance is:' ,amount)
def withdraw(amt):
    global amount
    if amt>amount:
        print('Insufficient Balance')
    else:
        amount = amount - amt
        print(amt, ' withdraw Tx done & update balance is:' , amount)

deposit(4500)
withdraw(3500)
balancecheck()