# Tip Calculator
print('Welcome to the tip calculator')
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_amount = (total_bill * tip_percentage) / 100
each_person_pays = (total_bill + tip_amount) / people
print(f"Each person should pay: ${round(each_person_pays, 2)}")
