bill = float (input("Enter the total bill amount: ")) 
tip_percentage = float (input("Enter tip percentage:"))
tip = bill * tip_percentage / 100
total  = bill + tip
# print(total)
round_total = round(total, 2)
f"₹{round_total:.2f}"

print(f"Total bill amount including tip: ₹{round_total:.2f}")