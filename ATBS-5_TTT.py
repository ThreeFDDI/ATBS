#!/usr/local/bin/python3

winner = False

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# function to print the current tic-tac-toe board
def printBoard(theBoard):
    print()
    print(theBoard['top-L'] + " | " + theBoard['top-M'] + " | " + theBoard['top-R'] + "\n" + "-"*9)
    print(theBoard['mid-L'] + " | " + theBoard['mid-M'] + " | " + theBoard['mid-R'] + "\n" + "-"*9)
    print(theBoard['low-L'] + " | " + theBoard['low-M'] + " | " + theBoard['low-R'] + "\n" )

# function to check each of the 8 possible winning combinations and return True if a winner is found
def checkWin(theBoard, player):
    if (theBoard['low-L'], theBoard['low-M'], theBoard['low-R']) == (player, player, player) or \
        (theBoard['mid-L'], theBoard['mid-M'], theBoard['mid-R']) == (player, player, player) or \
        (theBoard['top-L'], theBoard['top-M'], theBoard['top-R']) == (player, player, player) or \
        (theBoard['top-L'], theBoard['mid-L'], theBoard['low-L']) == (player, player, player) or \
        (theBoard['top-M'], theBoard['mid-M'], theBoard['low-M']) == (player, player, player) or \
        (theBoard['top-R'], theBoard['mid-R'], theBoard['low-R']) == (player, player, player) or \
        (theBoard['top-L'], theBoard['mid-M'], theBoard['low-R']) == (player, player, player) or \
        (theBoard['low-L'], theBoard['mid-M'], theBoard['top-R']) == (player, player, player):
            print("You are the winner!!")
            return True
    else:
         return False

# function for a player to make a move
def makeMove(theBoard, player):
    print("\n{}'s turn. The following spots are open. Where would you like to move?\n".format(player))
    
    # show open spots on the board
    for k, v in theBoard.items():
        print(k) if v == " " else next
    
    # prompt the player for their move
    theBoard[input("\n")] = player

    # print the board
    printBoard(theBoard)
    
    # return True or False for winner
    return checkWin(theBoard, player)

# alternate between players until there is a winner
while winner == False:
    winner = makeMove(theBoard, "X")

    # ipdb demo
    import ipdb; ipdb.set_trace()
    
    if winner == True:
            break
    else:
        winner = makeMove(theBoard, "O")


