# get users weight and height
weight = float(input("Please enter you weight in kg:\t"))
height = float(input("Please enter you height in m:\t"))

bmi = round((weight / height ** 2),2)
print (f"Thanks. Your BMI is {bmi}.")

# give feedback based on BMI
if (bmi >= 30):
    print("Your BMI score suggests you are obese.")
elif (bmi >= 25):
    print("Your BMI score suggests you are overweight.")
elif (bmi >= 18.5):
    print("Your BMI score suggests you weight is normal.")
else:
    print("Your BMI suggests you are underweight.")
