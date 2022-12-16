# get times for each even
print("Well done on completing the triathalon. Please enter how many minutes each stage took below.")
swim = int(input("Swimming:\t"))
cycle = int(input("Cycling:\t"))
run = int(input("Running:\t"))

# calculate total time
total = swim + cycle + run

# print total time
print(f"Thanks. You completed the event in a total time of {total} minutes.")

# decide the award
if (total < 100):
    print("Award: Provincial Colours")
elif (total < 105):
    print("Award: Provincial Half Colours")
elif (total < 110):
    print("Award: Provincial Scroll")
else:
    print("No award this time. Keep training!")
