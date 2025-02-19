#
# Crystal Egbert
# 2/13/25
# Budget Analysis Programming Project
# COSC 1010
#

monthlyBudget = 0
Expenses = 1
total = 0

#prompt user to enter amount they have budgeted for the month.
monthlyBudget = float(input('Enter your monthly budget. $ '))

# begin loop
while Expenses != 0:
    #enter expenses
    Expenses = float(input('Enter your expenses. 0 to end. $ '))
    total += Expenses
    print(total)

# print if user is within or above budget with total.
if total < monthlyBudget:
    print(f'You are under budget! $ {monthlyBudget - total:,.2f}')
elif total > monthlyBudget:
    print((f'You\'ve exceeded your monthly budget $ {total - monthlyBudget:,.2f}'))
else:
    print('You were on budget!')