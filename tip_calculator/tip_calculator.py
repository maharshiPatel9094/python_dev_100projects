print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15 percent? "))
people = int(input("How many people to split the bill? "))

bill_after_tip = round(bill + (tip / 100 * bill), 2)
print(f"Your total bill after tip is: ${bill_after_tip}")

bill_after_split = round(bill_after_tip / people, 2)
print(f"Each person should pay: ${bill_after_split}")
