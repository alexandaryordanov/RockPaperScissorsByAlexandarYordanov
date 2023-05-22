import random
# User input
rock = "Rock"
paper = "Paper"
scissors = "Scissors"
while True:
    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")
    # Logic
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid Input. Try again...")
    computer_random_number = random.randint(1, 3)
    computer_move = ""
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors
    # Output
    print(f"The computer chose {computer_move}.")
    if player_move == computer_move:
        print("Draw!")
    elif (player_move == rock and computer_move == paper) and (player_move == paper and computer_move == scissors) and (player_move == scissors and computer_move == rock):
        print("You lose!")
    else:
        print("You win!")
    question = input("Enter 'Y' if you want to play again, or any key for exit game:")
    if not question.lower() == 'y':
        break