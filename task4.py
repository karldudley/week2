# ask use to enter a whole number
num = int(input("Please enter a whole number:\t"))

# check if it is divisible by 2, 5 or both
if (num % 2 == 0 and num % 5 ==0):
    print(f"{num} is divisible by 2 and 5!")
elif (num % 2 == 0 or num % 5 ==0):
    print(f"{num} is divisible by 2 or 5!")
else:
    print(f"{num} is not divisible by 2 or 5!")
