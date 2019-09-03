# Problem 2c
# Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code? We can make this program run faster using a technique introduced in lecture - bisection search!

balance = 3200000
annualInterestRate = 0.2

balancefirst = balance
low = balance/12.0
high = (balance * (1+annualInterestRate/12) ** 12)/12.0
fixedpayment = (high + low)/2.0
epsilon = 0.01
month = 0


def totalpayment(fixedpayment, month, monthlybalance, annualInterestRate):
    for month in range(1, 13):
        monthlybalance = monthlybalance - fixedpayment
        monthlybalance = monthlybalance + \
            (annualInterestRate/12.0) * monthlybalance
        month += 1
    return monthlybalance


while abs(balance) >= epsilon:
    balance = balancefirst
    month = 0
    balance = totalpayment(fixedpayment, month, balance, annualInterestRate)
    if balance > 0:
        low = fixedpayment
    else:
        high = fixedpayment
    fixedpayment = (high + low)/2.0
print "Lowest Payment: ", str(round(fixedpayment, 2))

# output: Lowest Payment:  291570.9
