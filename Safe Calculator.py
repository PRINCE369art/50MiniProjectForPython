#this is the code where i can 
print("===== SAFE CALCULATOR =====")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

    print(f"Result: {result}")  

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

except ValueError:
    print("Error: Please enter numbers only.")
