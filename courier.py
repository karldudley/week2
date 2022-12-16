# get user choices
price = float(input("Please enter the price of the package:\t"))
distance = float(input("Please enter the distance in kms:\t"))
method = input("air or freight:\t")
insurance = input("full or limit:\t")
gift = input("Gift? (y or n)\t")
speed = input("priority or standard:\t")

# based on choices, add to the total price
if (method == "air"):
    price += (0.36 * distance)
else:
    price += (0.25 * distance)

if (insurance == 'full'):
    price += 50.00
else:
    price += 25.00 

if (gift == 'y'):
    price += 15.00

if (speed == 'priorty'):
    price += 100.00
else:
    price += 20.00

# print total price
print(f"The total cost is £{price}.")
