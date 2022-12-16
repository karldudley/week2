# import datatime module to get the current year
import datetime
today = datetime.date.today()
year = today.year

# get user's birth year
birth_year = int(input("Please enter the year you were born:\t"))

# calculate age of user
age = year - birth_year

# check they are old enough (>= 18)
if (age >= 18):
    print("Congrats, you are old enough!")
else:
    print(f"Sorry, come back in {18-age} years.")
