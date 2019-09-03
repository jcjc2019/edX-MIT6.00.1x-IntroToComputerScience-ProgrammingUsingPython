# Problem 2 a
# Write a program to calculate the credit card balance after one year
# if a person only pays the minimum monthly payment required by the credit card company each month.

balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


def min_monthly_payment(monthlyPaymentRate, balance, annualInterestRate):
    total_payment = 0
    for month in range(1, 13):
        min_monthly_payment = monthlyPaymentRate * balance
        monthly_unpaid_balance = balance - min_monthly_payment
        balance = monthly_unpaid_balance + annualInterestRate/12 * monthly_unpaid_balance
        print "Month: ", int(month)
        print "Minimum monthly payment: ", str(round(min_monthly_payment, 2))
        print "Remaining balance: ", str(round(balance, 2))
        total_payment += min_monthly_payment
        month += 1
    print "Total paid:", round(total_payment, 2)
    print "Remaining balance", round(balance, 2)


min_monthly_payment(monthlyPaymentRate, balance, annualInterestRate)
