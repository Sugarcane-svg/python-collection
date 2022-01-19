# ask user for the postion where to put the X and O

def move(l, steps, player):
    if l[int(steps[0])-1][int(steps[1])-1] == 0 and player == 1: 
        l[int(steps[0])-1][int(steps[1])-1] = 'X'
    elif l[int(steps[0])-1][int(steps[1])-1] == 0 and player == 2:
        l[int(steps[0])-1][int(steps[1])-1] = 'O'
    else: 
        return -1
    
    return l


def initial_game_board():
    return [[0,0,0],[0,0,0],[0,0,0]]

def get_steps(s):
    if len(s) > 3:
        return 'you entered more than 2 number'
    elif len(s) < 3:
        return 'you need 2 numbers to locate a position'

    return s.strip().split(',')

def print_board(l):
    if l == -1:
        print('you cannot place your piece over the other')
    else: 
        for i in l:
            print(i)

def player(l, player):
    play = ''
    if player == 1:
        play = input('enter a coordinate separate by "," for player1: ')
    else:
        play = input('enter a coordinate separate by "," for player2: ')

    steps = get_steps(play)
    moves = move(l, steps, player)
    print_board(moves)





if __name__ == '__main__':

    total_moves = 9
    game = initial_game_board()
    while total_moves > 0:
        player(game, 1)
        total_moves -= 1
        if total_moves == 0:
            break
        player(game, 2)
        total_moves -=1
        

    print('game board is full, the game is finished')
    