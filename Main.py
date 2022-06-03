from multiprocessing import RLock
from tracemalloc import stop
from winsound import PlaySound


C = True
while C == True:
    possible_choice = ["rock", "paper", "scissors"]
    print("Welcome")
    print("Game Starts in a second")
    print("This is a rock, paper and scissors game")


# Taking Users actions

    user_choice = input("Enter a choice( rock, paper, scissors): ")
    for letter in user_choice:
        if letter in possible_choice:
            continue
        else:
            break
            print("Choice not found")

    import random
    
# Making the Computer choice

    computer_choice = random.choice(possible_choice)
    print(f"\n You chose {user_choice}, computer chose {computer_choice},\n")

# Determining a winner
    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("rock smashes scissors! You win")
        else:
            print("paper covers rock! You lose.")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("paper covers rock! You win!")
        else:
            print("scissors cuts paper! You lose")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("scissors cut paper! You win!")
        else:
            print("rock smashes scissors! You lose.")

    elif user_choice not in possible_choice:
        print("wrong input")

        print("Do you want to play again, Yes or No")
    play_again = input("Enter 'Yes' to continue or 'No' to end: ")

    
    if play_again == "yes":
            continue

    elif play_again == "no":
         print("Game has ended")
         break