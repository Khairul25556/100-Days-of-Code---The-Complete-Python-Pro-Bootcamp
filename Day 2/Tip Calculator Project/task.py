import time

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?: $"))
tip = float(input("How much tip would you like to give?(10%, 20% or 15%): "))
tip_cal = round((bill * tip/100), 2)
total_bill = bill + tip_cal
friends = int(input("How many people to split the bill?: "))
individual_bill = total_bill / friends
print(f"We gave {tip}% tip. So I think you will get ${tip_cal}. And guys each one we have to give ${individual_bill}")
time.sleep(1)
print("Thanks for visiting us sir!")

