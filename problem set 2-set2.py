# -*- coding: utf-8 -*-
#Problem 2 b 
#  write a program that calculates the minimum fixed monthly payment needed 
# in order pay off a credit card balance within 12 months. 
# By a fixed monthly payment, we mean a single number which does not change each month, 
# but instead is a constant amount that will be paid each month.

balance = 4773
annualInterestRate = 0.2
month =0
fixedpayment = 10

def totalpayment(fixedpayment,month,monthlybalance,annualInterestRate):
    for month in range (1,13):
        monthlybalance = monthlybalance - fixedpayment
        monthlybalance = monthlybalance + ((annualInterestRate/12.0) * monthlybalance)
        month +=1
    return monthlybalance   
while totalpayment(fixedpayment, month, balance, annualInterestRate) > 0:
    fixedpayment+=10
    month = 0
    totalpayment(fixedpayment, month, balance, annualInterestRate)
print "Lowest Payment: ", str(fixedpayment)

#首先定義一個function，有四個變量，月份，每月利息，每月餘額，每月付錢
#然後限定若是得出的每月餘額大於0，那麼就是每月付錢要多付10塊錢，這時還是從0個月計算
#while中按照現在給的balance走一次那個function
#最後就可以印出來每月付錢。