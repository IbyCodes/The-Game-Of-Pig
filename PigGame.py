
# All work done by: MOHAMMAD IBRAHIM KHAN

import random


playerOneNew = 0 # Initializing some variables
playerTwoNew= 0



whosTurn = random.randint(1, 2) # The first turn must be random, so I decided to use the same random function as the dice but make it 1 or 2 as possibilities
# 1 will be AI's turn, 2 will indicate Human's turn

print ("A random player will be picked for the first turn.") # Will only be shown at the start of the game
print ("Choosing...")


while True: # a while loop will help me with looping back to the top of this section of code so the two computers can keep playing until one reaches >=100

    # AI variables and things I need to save/keep track of or initialize
    playerOneCurrent = playerOneNew
    playerOneOriginal = playerOneCurrent
    playerOneTurn = 0
    playerOneNew = playerOneCurrent

    # Human player variables and things I need to save/keep track of or initialize
    playerTwoCurrent = playerTwoNew
    playerTwoOriginal = playerTwoCurrent
    playerTwoTurn = 0
    playerTwoNew = playerTwoCurrent




    print ("") # This is me just being a bit fancy with the format of how it will look in the console when it's run
    print ("The AI's total score is:", playerOneNew) # Here I will print the player's total scores after each round is done (each player has had a turn each)
    print ("")
    print ("The human player's total score is:", playerTwoNew)
    print ("")

    if whosTurn == 1: # all of the AI player's CODE
        print ("Its the AI's turn!")
        while playerOneTurn < 20 and playerTwoNew<100:

            randomRoll = random.randint(1, 6)
            print("rolled a", randomRoll)
            playerOneTurn= playerOneTurn + randomRoll

            playerOneNew = playerOneTurn + playerOneCurrent

            whosTurn = 2  #I want to make sure the next turn is player 2's so here I change the value of whos turn it is


            if randomRoll == 1:  # If the computer rolls a 1, I must account for "pigging out"
                playerOneTurn = 0  # the score for the computer's turn instantly becomes 0
                print("Pigged out!")
                playerOneNew = playerOneOriginal  # I can now point this to the variable I stored earlier of the original score
                break  # I must break out of the loop or else the while loop will keep going until a score >= 20 is achieved

            if playerOneNew >= 100:  # we don't want the computer to keep rolling beyond 100 points, so we'll instantly break out of the loop
                print ("AI has reached the targeted goal!")
                break


        print ("Turn Score of the AI =", playerOneTurn) # simply printing the turn score of the AI player




    if whosTurn == 2: # HUMAN PLAYER CODE RESIDES HERE!
        print ("Its the human player's turn!")
        print ("Your total score at the moment is:",playerTwoNew) # this is just for ease of the human player so he/she knows what their score is before rolling

        while playerTwoTurn < 20 and playerOneNew < 100:
            # I need to add "playerOneNew < 100" because or else if the AI's turn happens to be first and it wins,
            # the human player will still be prompted to roll or hold which I DON'T WANT.

                randomRoll = random.randint(1, 6)
                print("rolled a", randomRoll)
                playerTwoTurn= playerTwoTurn + randomRoll

                playerTwoNew = playerTwoTurn + playerTwoCurrent

                whosTurn = 1  # Now Player 1's turn should be next right after player 2's turn is done

                if playerTwoNew >= 100:  # we don't want to keep rolling beyond 100 points, so we'll instantly break out of the loop
                    print ("The human player has reached the targeted goal!") # I want to state this to avoid any confusion
                    break # the winner is whoever reaches the targeted goal FIRST

                if randomRoll == 1:  # If the program rolls a 1, I must account for "pigging out"
                    playerChoice = "h" # I don't want the computer to ask the player if they want to roll again or not if they get a 1 (pig out)
                    playerTwoTurn = 0  # the score for the human player's turn instantly becomes 0
                    print("Sorry you pigged out!")
                    playerTwoNew = playerTwoOriginal  # I can now point this to the variable I stored earlier of the original score
                    break  # I must break out of the loop or else the while loop will keep going until a score >= 20 is achieved

                playerChoice = input("Would you like to roll again or hold onto your points?: Type 'R' to roll or 'H' to hold: ")  # prompt for human player's choice to roll or hold

                if playerChoice == "R" or playerChoice == "r": # will continue the loop and roll again
                    print ("Alright! Let's roll again!")

                elif playerChoice == "H" or playerChoice == "h": # will break out of the loop and end the player's turn
                    print ("Ok. Your turn ends here.")
                    break

                else:  # gotta punish the user for playing with the code!
                    print ("You did not type in a valid input. As a consequence, your turn ends here with a score of 0.")
                    playerTwoTurn = 0
                    break


        print ("Turn Score of the human =", playerTwoTurn)






    if playerOneNew >= 100: # If the AI wins, we want to display that it won
        print ("Final Score:","AI-",playerOneNew, "vs ", "Human-", playerTwoNew)  # display final scores with the winner's score stated first
        print ("AI Wins!")
        break

    if playerTwoNew >= 100: # If the human player wins , we want to display that it won
        print ("Final Score:","Human-",playerTwoNew, "vs", "AI-", playerOneNew)  # display final scores with the winner's score stated first
        print ("Human Wins!")
        break

