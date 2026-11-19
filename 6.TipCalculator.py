bill_amt = float(input("Enter bill amount: "))
percent_tip = float(input("Percentage to tip: "))
no_of_people = int(input("Number of people: "))

# Tip Amount and Total Amount
tip_amt = bill_amt * (percent_tip / 100)
total_amt = bill_amt + tip_amt

# Tip and Bill per person
tip_pp = tip_amt / no_of_people
total_pp = total_amt / no_of_people

print()
print("Tip amount: $", str(round(tip_amt, 2)))
print("Total amount: $", str(round(total_amt,2)))
print()
print("Tip per person: $", str(round(tip_pp, 2)))
print("Total per person: $", str(round(total_pp, 2)))
