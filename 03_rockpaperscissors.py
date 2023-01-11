# lets make a game name Rock Paper Scissors
# lets install random
import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game Ended")
        print("You Won a total score of" +str(user_points)+ "and the computer total score is" +str(computer_points))

    if user_input == "rock":
        if computer_input == "rock":
            print("Yur Input is Rock")
            print("Computer  Input is Rock ")
            print("its a Tie")
        elif computer_input == "paper":
            print("Your Input is Rock")
            print("Computer Input is Paper")
            print("Computer Wins")
            computer_points += 1
        elif computer_input == "scissors":
            print("Your Input is Rock")
            print("Computer Input is Scissors")
            print("yoU wIN")
            user_points +=1

    elif user_input == "paper":
        if computer_input == "rock":
            print("Your Input is Paper")
            print("Computer Input is Rock")
            print("you win")
            user_points +=1
        elif computer_input == "scissors":
            print("Your Input is Paper")
            print("Computer Input is Scissors")
            print("Computer Wins")
            computer_points += 1
        elif computer_input == "paper":
            print("Your Input is Paper")
            print("Computer Input is Paper")
            print("Its A Tie")

    elif user_input == "scissors":
        if computer_input == "rock":
            print("Your Input is Scissors")
            print("Computer Input is Rock")
            print("Computer Wins")
            computer_points += 1

        elif computer_input == "paper":
            print("Your Input is Scissors")
            print("Computer Input is Paper")
            print(" You Win")
            user_points +=1 
        elif computer_input == "scissors":
            print("Your Input is Scissors")
            print("Computer Input is scissors")
            print("Its A TIE")

    elif user_input != "rock" or user_input != "paper" or user_input != "scissors":
        print("Invalid Input")


# lets run it