import math
import os

# this function can be used to clear the screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# get user choice of investment or bond
print("Choose either 'investment' or 'bond' from the menu below to proceed:")
print("\ninvestment\t-\tto calculate the amount of interest you'll earn on an investment")
print("bond\t\t-\tto calculate the amount you'll have to pay on a home loan")

# convert to lowercase so it doesn't matter how the user entered it
choice = input("-> ").lower()

if (choice == "investment"):
    # clear the screen and get user to enter investment details
    cls()
    print("Welcome to the Investment Calculator")
    deposit = float(input("How much are you depositing: £\t"))
    rate = float(input("What is the interest rate (%):\t")) / 100
    years = float(input("How many years:\t"))
    int_type = input("Simple or Compound interest:\t").lower()
    final_value = deposit

    # calculate final value depending on interest type
    if (int_type == "simple"):
        final_value = deposit * (1 + rate * years)
        print(f"The final value of your investment after {years} years will be £{round(final_value,2)}.")
    elif (int_type == "compound"):
        final_value = deposit * math.pow((1 + rate), years)
        print(f"The final value of your investment after {years} years will be £{round(final_value,2)}.")
    else:
        print("Incorrect choice")
elif (choice == "bond"):
    # clear the screen and get user to enter bond details
    cls()
    print("Welcome to the Bond Calculator")
    house_value = float(input("What is the present value of your house: £\t"))
    monthly_rate = (float(input("What is the interest rate (%):\t")) / 100 ) / 12
    months = float(input("How many months to repay:\t"))

    # calculate the monthly repayment amount
    monthly_repay = int((monthly_rate * house_value) / (1 - (1 + monthly_rate) ** (-months)))

    # print monthly repayment
    print(f"You will need to repay £{monthly_repay} each month.")
else:
    cls()
    print("Incorrect choice")
