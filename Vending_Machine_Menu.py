print("===== VENDING MACHINE =====")

print("1. Soda - $1.50")
print("2. Chips - $2.00")
print("3. Coke - $1.00")
print("4. Pepsi - $1.50")

choice = int(input("Enter your choice: "))  #this is a variable that stores the user's choice 
 
match choice: #here we are using a match statement to check the user's choice and print the corresponding message
    case 1:                    #this is a case statement that checks if the user's choice is 1
        print("You have selected Soda.")

    case 2:
        print("You have selected Chips.")

    case 3:
        print("You have selected Coke.")

    case 4:
        print("You have selected Pepsi.")

    case _:  #this is a case statement that checks if the user's choice is not 1, 2, 3, or 4 
        print("Invalid choice.")