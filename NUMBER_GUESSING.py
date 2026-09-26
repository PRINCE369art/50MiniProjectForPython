import random
# to ask the user the top range of the game
top_of_range = input("enter a number: ")

# isdigit is check the numbe is digit or not
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("enter number larger than 0")
        quit()
    else:
        print("type a number next time")

# random.randit generate the random number between the (start , end)
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("make a guess ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("type a number next time")
        quit()
        continue

    if user_guess == random_number:
        print("you got it! ")

    elif user_guess > random_number:
        print("your are above the number")
    else:
        print("you are below the number")

    print("you got it in", guesses, "guesses")
