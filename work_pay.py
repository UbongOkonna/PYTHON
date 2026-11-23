name = input("enter freelancer name: ")
hourly_rate = str(input("enter hourly rate :"))
hours_worked = int(input("enter total hours worked :"))

total_pay = hourly_rate * hours_worked
print(f"\n--- payment slip for {name} ---")
print(f"Rate: {hourly_rate :,.2f}/hr x {hours_worked } hrs")
print(f"Tool pay: {total_pay :,.2f}")