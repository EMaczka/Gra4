import random, copy

def drawBoard(board):
    print(board['1']+'|'+board['2']+'|'+board['3']+'|'+board['4'])
    print('-------')
    print(board['5']+'|'+board['6']+'|'+board['7']+'|'+board['8'])
    print('-------')
    print(board['9']+'|'+board['10']+'|'+board['11']+'|'+board['12'])
    print('-------')
    print(board['13']+'|'+board['14']+'|'+board['15']+'|'+board['16'])

def inputPlayerLetter():
    letter=''
    while not(letter=='X' or letter =='O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X','O']
    else:
        return ['O','X']

def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    return ((bo['1']==le and bo ['2'] == le and bo['3']==le and bo['4']==le) or
        (bo['5']==le and bo ['6'] == le and bo['7']==le and bo['8']==le) or
        (bo['9']==le and bo ['10'] == le and bo['11']==le and bo['12']==le) or
        (bo['13']==le and bo ['14'] == le and bo['15']==le and bo['16']==le) or   
        (bo['1']==le and bo ['5'] == le and bo['9']==le and bo['13']==le) or
        (bo['2']==le and bo ['6'] == le and bo['10']==le and  bo['14']==le) or
        (bo['3']==le and bo ['7'] == le and bo['11']==le and bo['15']==le) or
        (bo['4']==le and bo ['8'] == le and bo['12']==le and bo['16']==le) or
        (bo['1']==le and bo ['6'] == le and bo['11']==le and bo['16']==le) or
        (bo['4']==le and bo ['7'] == le and bo['10']==le and bo['13']==le))

def isSpaceFree(board, move):
    return board[move]== ' '

def getPlayerMove(board):
    move=' '
    while move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'.split() or not isSpaceFree(board,move):
        print('What is your next move? 1-16')
        move = input()
    return move

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves)!=0:
        return random.choice(possibleMoves)
    else:
        return None
    
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
        
    #check if we(computer) can win in next move
    for i in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'.split():
        dupe = copy.copy(board)
        if isSpaceFree(dupe, i):
            makeMove(dupe, computerLetter, i)
            if isWinner(dupe, computerLetter):
                return i

    #check if player could win in next move, and block them
    for i in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'.split():
        dupe = copy.copy(board)
        if isSpaceFree(dupe, i):
            makeMove(dupe, playerLetter, i)
            if isWinner(dupe, playerLetter):
                return i

    #try to take one of the corners if they are free
    move = chooseRandomMoveFromList (board, ['1','13','4','16'])
    if move != None:
        return move

    #try to take the center if it is free
    move = chooseRandomMoveFromList (board, ['6','7','10','11'])
    if move != None:
        return move

    return chooseRandomMoveFromList(board, ['2','3','5','8','9','12','14','15'])

def isBoardFull(board):
    for i in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'.split():
        if isSpaceFree(board, i):
            return False
    return True

print('Welcome to Tic Tac Toe')
playerLetter, computerLetter = inputPlayerLetter()
print('In the game you can choose fields for your ' + playerLetter +'s by entering numbers from 1 to 16 like below:')
print('1 | 2 | 3 | 4 ')
print('-------------')
print('5 | 6 | 7 | 8 ')
print('-------------')
print('9 |10 |11 |12')
print('-------------')
print('13|14 |15 |16')
print('')

while True:
    #reset the board
    theBoard = {'1': ' ','2': ' ', '3': ' ', '4': ' ',
                '5': ' ','6': ' ', '7': ' ', '8': ' ',
                '9': ' ','10': ' ', '11': ' ', '12': ' ',
                '13': ' ','14': ' ', '15': ' ', '16': ' '}
    
    turn = whoGoesFirst()
    print ('The '+turn+' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    print ('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner (theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)                
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
                
    break
    
