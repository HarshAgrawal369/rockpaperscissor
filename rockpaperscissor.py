import random

choices = ['rock','paper', 'scissors']

while True:
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Enter a choice (rock, paper, scissors): ").lower()
        if player not in choices:
            print("Invalid input. Please enter rock, paper, or scissors.")
            continue

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("It is a tie")
    elif player == 'rock':
        if computer == 'scissors':
            print("computer: ",computer)
            print("player: ",player)
            print("You win")
        else:
            print("computer: ",computer)
            print("player: ",player)
            print("You lose")
    elif player == 'paper':
        if computer == 'rock':
            print("computer: ",computer)
            print("player: ",player)
            print("You win")
        else:
            print("computer: ",computer)
            print("player: ",player)
            print("You lose")
    elif player == 'scissors':
        if computer == 'paper':
            print("computer: ",computer)
            print("player: ",player)
            print("You win")
        else:
            print("computer: ",computer)
            print("player: ",player)
            print("You lose")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    while play_again not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        play_again = input("Do you want to play again? (yes/no): ").lower()
    
    if play_again == 'no':
        print("Thanks for playing!")
        break
