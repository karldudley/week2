# setup variables
hot = False
weekend = False
sunny = False

# get temperature and update variable
temp = int(input("What's the temperature today?\t"))
if (temp > 20):
    hot = True

# get weekday and update variable
day = input("What day is it?\t")
if (day.lower() == "saturday" or day.lower() == "sunday"):
    weekend = True

# get weather and update variable
weather = input("Is it sunny today? (y or n)\t")
if (weather == "y"):
    sunny = True

# decide what the user should wear based on temp
if (hot):
    print("It's hot today, wear a short-sleeved shirt.")
else:
    print("It's cold today, wear a long-sleeved shirt.")

# decide what the user should wear based on day
if (weekend):
    print("It's the weekend, so wear shorts.")
else:
    print("It's a weekday, so wear jeans.")

# decide what the user should wear based on weather
if (sunny):
    print("It's sunny today, so please wear a cap.")
else:
    print("It's not very sunny, please wear a raincoat.")
