# Yasmin Gil
# yasmingi@usc.edu
# Loan and Interest Repayments Analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# Method to error check input
def IfValidInput(num):
    is_number = False
    while not is_number:
        try:
            float(num)
            is_number = True
        except ValueError:
            is_number = False
            num = input("Please enter a valid number.")
    return num

def Question1():
    # Generate random integers and store array into x&y
    x = np.random.randint(low=1, high=201, size=200)
    y = np.random.randint(low=1, high=201, size=200)
    # Plot x & Y and set labels
    fig, ax = plt.subplots(1,1)
    ax = plt.scatter(x, y, c='r', s=3)
    plt.xlabel('Random Integer', c='b')
    plt.ylabel('Random Integer', c='b')
    plt.title('Scatter of Random Integers', c='g', size=14)
    plt.show()

def Question2():
    # Plot data from NOAA, NCDC, plot global temp for the past 140 years
    # load data from csv & skip first 4 rows of header
    temp = pd.read_csv("data.csv", skiprows=4)
    # print(temp)
    plt.plot(temp['Year'], temp['Value'], marker='o', linestyle='--', c='r')
    plt.xlabel('Year(year)')
    plt.ylabel('Temperature Anomaly (degrees C)')
    plt.title('Global Temperature')
    plt.show()

def Question3():
    # from hw 1
    # Gather user input and store into variables
    user = input("Enter the loan amount: ")
    PV = float(IfValidInput(user))
    user = input("Enter the interest rate: ")
    i = float(IfValidInput(user))
    i = i / (12 * 100)
    user = input("Enter the term of the loan in months: ")
    n = int(IfValidInput(user))
    # use math library to calculate powers
    PMT = PV * i * math.pow(1 + i, n) / (math.pow(1 + i, n) - 1)

    # calculate principal balance over time
    balance = list()
    interest_payments = list()
    for month in range(0,n+1):
        balance.append(PV)
        interest = PV * i
        PV -= (PMT - interest)
        interest_payments.append(interest)
    # print(balance)
    # print(interest_payments)
    balance_ser = pd.Series(balance)
    interest_payments_ser = pd.Series(interest_payments)


    # plot using subplots & set x & y labels w/ titles
    fig, ax = plt.subplots(1,2)
    ax[0].plot(balance_ser, color='b', marker='o')
    ax[0].set(xlabel='Month', ylabel='Loan Balance ($USD)', title='Loan Balance vs Month')
    ax[1].plot(interest_payments_ser, color='b', marker='o')
    ax[1].set(xlabel='Month', ylabel='Interest Paid ($USD)', title='Interest Paid vs Month')
    fig.suptitle('Loan quantities plotting')
    plt.show()

def main():
    # homework questions are in different functions
    Question1()
    Question2()
    Question3()


if __name__ == '__main__':
    main()