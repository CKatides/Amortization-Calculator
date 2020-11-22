import os
import sys
import pandas as pd
import locale
locale.setlocale( locale.LC_ALL, 'en_CA.UTF-8' )

"""
A is the payment amount per period, based on the included formula
r is the interest rate per year
P is the initial principal/loan amount
n is the total number of payments or periods.

A = P((r(1+r)**n)/((1+r)**n - 1))

"""

def showtable(P,r,n,A):
        startingprincipal = P
        monthlyinterest = r
        count = 1
        df1 = pd.DataFrame(columns=['Payment No.','Towards Interest','Towards Principal','Remaining Balance'])

        while n > 0:
            interestpayment = monthlyinterest * P
            principalpayment = A - interestpayment
            remainingbalance = P - principalpayment

            valtoconv = remainingbalance 
            #Currency conversions, including commas, formatted as str
            interestpayment = round(interestpayment,2)
            interestpayment = locale.currency(interestpayment, grouping=True)
            principalpayment = round(principalpayment,2)
            principalpayment = locale.currency(principalpayment, grouping=True)
            valtoconv = round(valtoconv,2)
            valtoconv = locale.currency(valtoconv, grouping=True)
            

            data = {"Payment No.": count, "Towards Interest": interestpayment, "Towards Principal":principalpayment,"Remaining Balance": valtoconv}
            df1 = df1.append(data, ignore_index=True, sort=False)
            df1 = df1.round(2)


            P = remainingbalance
            count += 1
            n -= 1
        print(df1)

print("\nWhat is the total loan amount?\n")
P = input()

print("\nWhat is the annual interest rate, expressed as a decimal?\n")
r = input()

print("\nWhat is the total amount of payments in months?\n")
n = input()

P = int(P)
r = float(r)
n = int(n)

r = r/12 #convert to monthly interest
A = (P*((r*((1+r)**n))/(((1+r)**n) - 1))) #Find payment amount

print("\nThe payment amount per period is $%.2f" % (A))
print("\n")
tablechoice = input("Display data table...y/n? ")
tablechoice = str(tablechoice)
print("\n")

if tablechoice in ('y','Y','yes','Yes'):
    showtable(P,r,n,A)
else:
    print("No table! Ok!")
