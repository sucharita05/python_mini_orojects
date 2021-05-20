print("Welcome to tip calculator!")
bill = float(input("What was the total bill?₹ "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
person = int(input("How many people to split the bill? "))

tip_percent = (tip)/100
total_bill = (bill * tip_percent) + bill
avg_bill = total_bill / person
final_bill = "{:.2f}".format(avg_bill)
print(f"Each person should pay: ₹{final_bill}")