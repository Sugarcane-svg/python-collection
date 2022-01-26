# make the whole game. modify and reuse the code from practicepython.org

# draw board
def drawboard(board):
    if isinstance(board, list):
        print (' ' + str(board[0][0]) + ' | ' + str(board[0][1]) + ' | ' + str(board[0][2]))
        print ('--- --- ---')
        print (' ' + str(board[1][0]) + ' | ' + str(board[1][1]) + ' | ' + str(board[1][2]))
        print('--- --- ---')
        print (' ' + str(board[2][0]) + ' | ' + str(board[2][1]) + ' | ' + str(board[2][2]))
    else:
        print(board)

# check winner
import numpy as np
def checkGrid(grid):
	# rows
	for x in range(0,3):
		row = set([grid[x][0], grid[x][1], grid[x][2]])
		if len(row) == 1 and grid[x][1] != " ":
			return grid[x][1]

	# columns
	for x in range(0, 3):
		column = set([grid[0][x], grid[1][x], grid[2][x]])
		if len(column) == 1 and grid[0][x] != " ":
			return grid[0][x]

	# diagonals
	diag1 = set([grid[0][0], grid[1][1], grid[2][2]])
	diag2 = set([grid[0][2], grid[1][1], grid[2][0]])
	if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != " ":
		return grid[1][1]

	return 0

def init_game():
    return [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]


def get_steps(s):
    return s.strip().split(',')


def move(l, steps, player):
    a = int(steps[0])
    b = int(steps[1])

    if l[a-1][b-1] == ' ' and player == 1:
        l[a-1][b-1] = 'X'
    elif l[a-1][b-1] == ' ' and player == 2:
        l[a-1][b-1] = 'O'
    else:
        return -1

    return l

def player(l, player):
    play = ''
    if player == 1:
        play = input('enter a coordinate separate by "," for player1: ')
    else:
        play = input('enter a coordinate separate by "," for player2: ')

    steps = get_steps(play)
    return move(l, steps, player)

def display_winner(game):
    if checkGrid(game) == 'X':
            return "player1 win"
    elif checkGrid(game) == 'O':
            return 'player2 win'
    else:
        return 0

if __name__ == "__main__":
    total_step = 9

    game = init_game()
    drawboard(game)
    while total_step > 0:
        # player1 = input('enter a coordinate separated by "," for player 1: ')
        # steps = get_steps(player1)
        # print('step: ' + str(steps))
        # game = move(game, steps, 1)
        game = player(game, 1)
        if game == -1:
            print('you should not place your piece on the top of others. restart :)')
            game = player(init_game(), 1)
        total_step -=1
        drawboard(game)
        if display_winner(game) != 0:
            print(display_winner(game))
            break  
        game = player(game, 2)
        if game == -1:
            print('you should not place your piece on the top of others. restart :)')
            game = player(init_game(), 2)
        total_step -= 1
        drawboard(game)
        if display_winner(game) != 0:
            print(display_winner(game))
            break
    
    print('no winner')


        
