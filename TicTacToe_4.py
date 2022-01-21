# make the whole game. Reuse the code from practicepython.org

# draw board
def drawboard(board):

    print (' ' + str(board[0][0]) + ' | ' + str(board[0][1]) + ' | ' + str(board[0][2]))
    print ('-----------')
    print (' ' + str(board[1][0]) + ' | ' + str(board[1][1]) + ' | ' + str(board[1][2]))
    print('-----------')
    print (' ' + str(board[2][0]) + ' | ' + str(board[2][1]) + ' | ' + str(board[2][2]))


#drawboard(['', '', '', '', '', '', '', '', ''])


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


def player(l, player):
    play = ''
    if player == 1:
        play = input('enter a coordinate separate by "," for player1: ')
    else:
        play = input('enter a coordinate separate by "," for player2: ')

    steps = p.get_steps(play)
    moves = p.move(l, steps, player)
    drawboard(moves)

import TicTacToe_3 as p
if __name__ == "__main__":
    total_moves = 9
    game = p.initial_game_board()
    drawboard(game)
    # while total_moves > 0:
    #     p.player(game, 1)
    #     total_moves -= 1
    #     if total_moves == 0:
    #         break
    #     p.player(game, 2)
    #     total_moves -= 1
    # print('game board is full, the game is finished')
