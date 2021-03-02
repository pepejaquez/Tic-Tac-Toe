import sys
import Color
import copy

StartBoard = [ ["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"] ]
Board = copy.deepcopy(StartBoard)

def DrawBoard(Board):
    
    for row in range(len(Board)):
        line = "   "
        for col in range(len(Board[row])):
            # X's turn change the color to red
            if (Board[row][col] == "X"):
                line += " " + Color.Red_Color + Board[row][col] + Color.Reset_Color + " "
            # O's turn change the color to blue
            elif (Board[row][col] == "O"):
                line += " " + Color.Blue_Color + Board[row][col] + Color.Reset_Color + " "
            # Default board color is white
            else:
                line += " " + Board[row][col] + " "
            # Add column dividers, make them green
            if (col < len(Board[row]) - 1):
                line += Color.Green_Color + "|" + Color.Reset_Color
        print (line)
        #  Add row dividers, make them green 
        if (row < len(Board) - 1):
            print (Color.Green_Color + "    ---------" + Color.Reset_Color)
    print ("\n")
            
def flipTurn(turn):
    if (turn == "X"):
        return "O"
    else:
        return "X"

def checkWin(Board):
    ret = ""
    
    # Set the color of the winner message or the tie message
    winnerX = Color.Red_Color + " X is the Winner!!\n" + Color.Reset_Color
    winnerO = Color.Blue_Color + " O is the Winner!!\n" + Color.Reset_Color
    tieGame = Color.Red_Color + " Tie Game. No Winner!\n" + Color.Reset_Color
    # Top Row
    if (Board[0][0] == Board[0][1] == Board[0][2]):
        if (Board[0][0] == "X"):
            ret = winnerX
        else:
            ret = winnerO
        
    # Middle Row
    if (Board[1][0] == Board[1][1] == Board[1][2]):
        if (Board[1][0] == "X"):
            ret = winnerX
        else:
            ret = winnerO
        
    # Bottom Row
    if (Board[2][0] == Board[2][1] == Board[2][2]):
        if (Board[2][0] == "X"):
            ret = winnerX
        else:
            ret = winnerO
        
    # Left Column
    if (Board[0][0] == Board[1][0] == Board[2][0]):
        if (Board[0][0] == "X"):
            ret = winnerX
        else:
            ret = winnerO
        
    # Middle Column
    if (Board[0][1] == Board[1][1] == Board[2][1]):
        if (Board[0][1] == "X"):
            ret = winnerX
        else:
            ret = winnerO
        
    # Right Column
    if (Board[0][2] == Board[1][2] == Board[2][2]):
        if (Board[0][2] == "X"):
            ret = winnerX
        else:
            ret = winnerO
        
    # Diagonal - Upper Left to Lower Right
    if (Board[0][0] == Board[1][1] == Board[2][2]):
        if (Board[0][0] == "X"):
            ret = winnerX
        else:
            ret = winnerO
        
    # Diagonal - Lower Left to Upper Right
    if (Board[2][0] == Board[1][1] == Board[0][2]):
        if (Board[2][0] == "X"):
            ret = winnerX
        else:
            ret = winnerO
            
    # Counter counts the X's and O's for a tie game. If all nine spot are
    # taken and no winner, counter will be 9 and trigger the checkTie.
    counter = 0
    
    # Check for a tie game
    for row in range(len(Board)): 
        for col in range(len(Board[row])):
            # Count the X's and O's for tie game 
            if ((Board[row][col] == "X") or (Board[row][col] == "O")):
                counter += 1
    if (counter == 9):
        counter = 0
        ret = tieGame
        
    return ret
        
playing = True

# X begins play
turn = "X"

# Trigger for bad user input
badCoice = False

# Trigger for spot already played
spotTaken = False

while (playing == True):
    # Clear the console
    print (Color.Clear_Screen)
    
    if (badCoice == True):
        print (Color.Red_Color + " INVALID CHOICE!!" + Color.Reset_Color + "\n")
        badCoice = False
        
    if (spotTaken == True):
        print (Color.Red_Color + " SPOT ALREADY TAKEN!!" + Color.Reset_Color + "\n")
        spotTaken = False
        
    # Check player move for win
    win = checkWin(Board)
    if (win != ""):
        print (win)
        DrawBoard(Board)
        # prompt user choice to keep playing
        print (Color.Red_Color + " Would you like to play again?" + Color.Reset_Color)
        playAgain = input(" Yes/No: ")
        
        if (playAgain == "No" or playAgain == "no" or playAgain == "N" or playAgain == "n"):
            # Game over
            break            
        else:
            # Make a new copy of the board to keep playing
            Board = copy.deepcopy(StartBoard)
            # Reset the player turn to 'X'
            turn = "X"
            # Clear the previous game
            print (Color.Clear_Screen)
        
    # print the game header
    print (Color.Yellow_Color + " ***************")
    print (" * " + Color.Magenta_Color + "Tic-Tac-Toe " + Color.Yellow_Color + "*")
    print (" ***************\n" + Color.Reset_Color)
    
    # Draw the game board every time a play is made
    DrawBoard(Board)
    
    # Swap the message for current player turn
    if (turn == "X"):
        print (" " + Color.Red_Color + turn + "'s turn" + Color.Reset_Color)
    else:
        print (" " + Color.Blue_Color + turn + "'s turn" + Color.Reset_Color)
    
    choice = input("\n Enter 1 - 9 or Q: ")
    
    row = -1
    col = -1
    
    # Player choices
    if (choice == "q" or choice == "Q"):
        playing = False
    elif (choice == "1"):
        col = 0
        row = 0
    elif (choice == "2"):
        col = 1
        row = 0
    elif (choice == "3"):
        col = 2
        row = 0
    elif (choice == "4"):
        col = 0
        row = 1
    elif (choice == "5"):
        col = 1
        row = 1
    elif (choice == "6"):
        col = 2
        row = 1
    elif (choice == "7"):
        col = 0
        row = 2
    elif (choice == "8"):
        col = 1
        row = 2
    elif (choice == "9"):
        col = 2
        row = 2
        
    # Check the player move to see if it's valid
    if (row != -1 and col != -1 and playing == True):
        current = Board[row][col]
        # If cell is not taken fill it with the current player
        if (current != "X" and current != "O" ):
            Board[row][col] = turn
            # Flip the turn to the next player
            turn = flipTurn(turn)
        else:
            # Bad move, spot already played
            spotTaken = True            
    else:
        # Player made an invalid choice
        if (playing == True):
            badCoice = True
            
# Game is over
print ("\n" + Color.Red_Color + " Good Bye!")  
