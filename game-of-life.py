import turtle
import random

# beginning state random
# 

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

print(board)