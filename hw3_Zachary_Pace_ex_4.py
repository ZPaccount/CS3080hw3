'''
Homework 3-4
Name: Zachary Pace
Date: 2/22/2023
Description: Tic-Tac-Toe
'''


# Function definitions
def showBoard(board):
    print(board['TL'] + ' |' + board['TC'] + ' |' + board['TR'])
    print('--------')
    print(board['ML'] + ' |' + board['MC'] + ' |' + board['MR'])
    print('--------')
    print(board['BL'] + ' |' + board['BC'] + ' |' + board['BR'])


def showKey():
    print('Key:\nTL|TC|TR\n--------\nML|MC|MR\n--------\nBL|BC|BR\n')


def moveX(board, move):
    board[move] = 'X'


def moveO(board, move):
    board[move] = 'O'


# Defining the board
board = {'TL': ' ', 'TC': ' ', 'TR': ' ',
         'ML': ' ', 'MC': ' ', 'MR': ' ',
         'BL': ' ', 'BC': ' ', 'BR': ' '}

# Starting Game
playing = True
showKey()
while playing:
    showBoard(board)
    moveX(board, str(input("X turn to move: ")))
    showBoard(board)
    moveO(board, str(input("O turn to move: ")))
