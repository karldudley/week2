import math

# get building shape from user and initialise area variable as a float
shape = input("Please enter the shape of the building (square, rectangle or round):\t")
area = 0.0

# get dimensions based on shape
if (shape == "square"):
    length = float(input("What's the length of the square in metres:\t"))
    print(f"The square has an area of {round(length ** 2,2)} metres squared.")
elif (shape == "rectangle"):
    length = float(input("What's the length of the rectangle in metres:\t"))
    width = float(input("What's the width of the rectangle in metres:\t"))
    print(f"The rectangle has an area of {round(length * width,2,)} metres squared.")
elif (shape == "round"):
    radius = float(input("What's the radius of the circle in metres:\t"))
    print(f"The circle has an area of {round(math.pi * radius ** 2,2)} metres squared.")
else:
    print("You entered an incorrect shape.")
    