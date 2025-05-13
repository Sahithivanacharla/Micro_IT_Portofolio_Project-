import random

options = ["rock", "paper", "scissors"]

while True:
    player_choice = input("Type 'quit' to exit, or choose rock, paper, or scissors: ").lower()

    if player_choice == "quit":
        print("Thanks for playing!")
        break

    if player_choice not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(options)

    print(f"You selected {player_choice}, the computer selected {computer_choice}.")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")
        