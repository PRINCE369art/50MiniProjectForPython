import random

number = random.randint(1, 100)

print("===== NUMBER GUESSING GAME =====")

while True:
    user_guess = int(input("Guess a number between 1 and 100: "))

    if user_guess == number:
        print("Congratulations! You guessed the correct number. 🎉")
        break

    elif user_guess < number:
        print("Your guess is too low. Try again.")

    else:
        print("Your guess is too high. Try again.")
