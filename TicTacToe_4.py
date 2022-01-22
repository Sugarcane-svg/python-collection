# make the whole game. Reuse the code from practicepython.org

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
def checkGrid(grid):
	# rows
	for x in range(0, 3):
		row = set([grid[x][0], grid[x][1], grid[x][2]])
		if len(row) == 1 and grid[x][0] != 0:
			return grid[x][0]

	# columns
	for x in range(0, 3):
		column = set([grid[0][x], grid[1][x], grid[2][x]])
		if len(column) == 1 and grid[0][x] != 0:
			return grid[0][x]

	# diagonals
	diag1 = set([grid[0][0], grid[1][1], grid[2][2]])
	diag2 = set([grid[0][2], grid[1][1], grid[2][0]])
	if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
		return grid[1][1]

	return 0

def init_game():
    return [['0', '0', '0'],
            ['0', '0', '0'],
            ['0', '0', '0']]


def get_steps(s):
    return s.strip().split(',')


def move(l, steps, player):
    if l[int(steps[0])-1][int(steps[1])-1] == 0 and player == 1:
        l[int(steps[0])-1][int(steps[1])-1] = 'X'
    elif l[int(steps[0])-1][int(steps[1])-1] == 0 and player == 2:
        l[int(steps[0])-1][int(steps[1])-1] = 'O'
    else:
        return -1

    return l

# def player(l, player):
#     play = ''
#     if player == 1:
#         play = input('enter a coordinate separate by "," for player1: ')
#     else:
#         play = input('enter a coordinate separate by "," for player2: ')

#     steps = get_steps(play)
#     moves = move(l, steps, player)
#     drawboard(moves)

import TicTacToe_3 as p
if __name__ == "__main__":
    total_moves = 9
    game = init_game()
    drawboard(game)
    
    # moves = move(game, get_steps(player1), 1)
    # print(moves)
    # while total_moves > 0:
    #      player(game, 1)
    #      total_moves -= 1
    #      if total_moves == 0:
    #         break
    #      player(game, 2)
    #      total_moves -= 1
    # print('game board is full, the game is finished')
