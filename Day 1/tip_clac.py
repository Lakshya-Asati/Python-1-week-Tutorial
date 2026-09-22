print("--- Tip Calculator ---")
bill = float(input("Total bill amount: $"))
tip_pct = int(input("Tip percentage (10, 12, or 15): "))
people = int(input("How many people to split the bill? "))

total_bill = bill/2* (1 + tip_pct / 100)
per_person = total_bill / people

print(f"Each person should pay: ${per_person:.2f}")