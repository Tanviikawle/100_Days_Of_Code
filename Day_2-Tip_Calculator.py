print("Welcome to Tip Calculator!")
bill=int(input("What was the total bill? $"))
ppl=int(input("How many people to split the bill? "))
tip=int(input("What percentage tip would you like to give? 10,12 or 15 "))
tip_as_percentage=tip/100
total_tip=bill*tip_as_percentage
total_bill=bill+total_tip
bill_per_person=total_bill/ppl
final_amt=round(bill_per_person,2)
final_amt="{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amt}")