weight = float(input("Enter your weight: "))

height = float(input("Enter your height: "))

bmi = weight / (height ** 2)

bmi = round(bmi, 2)

if bmi < 18.5:
    print("You are underweight.")

elif bmi < 25:
    print("You have a normal weight.")

elif bmi < 30:
    print("You are overweight.")

else:
    print("You are obese.")