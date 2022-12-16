# declare three numbers
num1 = 100
num2 = 8
num3 = 20000

# print out whether num1 or num2 is largest
if (num1 > num2):
    print(f"{num1} (num1) is bigger than {num2} (num2)")
elif (num2 > num1):
    print(f"{num2} (num2) is bigger than {num1} (num1)")
else:
    print("Both variables (num1 & num2) have the same value")

# determine if num1 is odd or even
if (num1 % 2 == 0):
    print("num1 is even")
else:
    print("num1 is odd")

# print out the numbers in order - largest to smallest
if (num1 > num2 and num1 > num3):
    if (num2 > num3):
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
elif (num2 > num3 and num2 > num1):
    if (num3 > num1):
        print(num2, num3, num1)
    else:
        print(num2, num1, num3)
else:
    if (num2 > num1):
        print (num3, num2, num1)
    else:
        print (num3, num1, num2)
