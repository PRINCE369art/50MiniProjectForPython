import random

#define a function to play the game
def main():  #this is a function main()
    user_action = input("Enter a choice (rock, paper, scissors): ")  #user_action is a variable that stores the user's input
    possible_actions = ["rock", "paper", "scissors"]  # possible_actions is a list that stores the possible actions
    computer_action = random.choice(possible_actions)  # computer_action is a variable that stores a random choice from the possible_actions list
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n") 

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")   #print this if both players selected the same action

    elif user_action == "rock":                     #rock
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")

    elif user_action == "paper":                    #paper
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")

    elif user_action == "scissors":                 #scissors
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

if __name__ == "__main__":
    main()