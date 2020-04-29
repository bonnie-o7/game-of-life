from turtle import *
import random

def determine_living_neighbors(board, cell): # [x, y]
    living = 0
    x, y = cell
    global BOARD_LENGTH

    if board[(x - 1) % BOARD_LENGTH][y] == 1: # mid left
        living += 1
    if board[(x + 1) % BOARD_LENGTH][y] == 1: # mid right
        living += 1
    if board[(x - 1) % BOARD_LENGTH][(y - 1) % BOARD_LENGTH] == 1: # top left
        living += 1
    if board[x][(y - 1) % BOARD_LENGTH] == 1: # top mid
        living += 1
    if board[(x + 1) % BOARD_LENGTH][(y - 1) % BOARD_LENGTH] == 1: # top right
        living += 1   
    if board[(x - 1) % BOARD_LENGTH][(y + 1) % BOARD_LENGTH] == 1: # bottom left
        living += 1
    if board[x][(y + 1) % 50] == 1: # bottom mid
        living += 1
    if board[(x + 1) % BOARD_LENGTH][(y + 1) % BOARD_LENGTH] == 1: # bottom right
        living += 1
    
    return living

def update_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            living_neighbors = determine_living_neighbors(board, [i, j])
            current = board[i][j]
            if current == 0 and living_neighbors == 3:
                current = 1
            elif current == 1 and (living_neighbors <= 1 or living_neighbors > 3):
                current = 0

def draw_board(board):
    tracer(False)

    color('black','white')
    for i in range(-250, 250, 10):
        for j in range(-250, 250, 10):
            goto(i, j)      
            stamp()

    color('black')
    for i in range(0, 50):
        for j in range(0, 50):
            if board[i][j] == 1:
                goto((i - 25) * 10, (j - 25) * 10)
                stamp()

    tracer(True)        
    done()

BOARD_LENGTH = 50
board = []
ALIVE_CHANCE = 0.05

for i in range(BOARD_LENGTH):
    board.append([])
    for j in range(BOARD_LENGTH):
        state = random.randint(1, 1 / ALIVE_CHANCE)
        if state == 1:
            board[i].append(1)
        else:
            board[i].append(0)

update_board(board)

hideturtle()
shape("square")
penup()
shapesize(0.5, 0.5, 0.8)

draw_board(board)