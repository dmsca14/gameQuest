# Created by Dominic Sangster

# import modules
import random
import time

# global variables
total_count = 0
gameEnd = False
lost = False

# choose who goes first
def initialGame():
    started = False
    # while the game is not started
    while started == False:
        yes = ["y", "Y"]
        no = ["n", "N"]
        print("\n\nWelcome to the game!")
        answer = input("Would you like to go first? (y/n)")
        # you go first, and the game starts
        if answer in yes:
            play_first = True
            print("You're up first. Good luck!")
            started = True
        # you go second, and the game starts
        elif answer in no:
            play_first = False
            print("Computer is up first. Good luck!")
            started = True
        # game does not start until a valid answer is given
        else:
            print("Please answer 'y' or 'n' only.")
            started = False
    return(play_first)

# player's turn; can pick a number from 1-3
def playerPlay():
    choices = [1, 2, 3]
    play1 = int(input("How many numbers do you want to call? Choose from " + str(choices)))
    print("You chose to add " + str(play1) + ".")
    add_score(play1)

# computer's turn; picks a random number from 1-3
def compPlay():
    play2 = random.randint(1,3)
    print("The computer added " + str(play2) + ".")
    add_score(play2)

# add the score
def add_score(number_played):
    global total_count
    global gameEnd
    global lost
    total_count += number_played
    print("The total score is now " + str(total_count))
    if total_count >= 21:
        gameEnd = True
        lost = True

# alternate turns and trigger loss sequence when someone reaches 21 or above
def game():
    play_first = initialGame()
    global gameEnd
    global lost

    # start game with player first
    if play_first:
        # captures the moment the game ends and specifically who played last
        while not gameEnd:
            # player made last move
            playerPlay()
            if lost:
                print("You lost!")
            else:
                # computer made last move
                compPlay()
                if lost:
                    print("You won!")

    #sStart game with cpu first
    # same as above
    else:
        while not gameEnd:
            compPlay()
            if lost:
                print("You won!")
            else:
                playerPlay()
                if lost:
                    print("You lost!")

game()