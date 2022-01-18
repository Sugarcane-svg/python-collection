# determine which player wins in 3 x 3 game board

import numpy as np


def check_row(l):
    for i in l:
        if i[0] == i[1] == i[2] and np.sum(i) != 0:
            return i[1]
    return 0


def check_col(l):
    l = np.transpose(l)
    return check_row(l)


def check_diag(l):
    if l[1][1] != 0:
        if l[0][0] == l[1][1] == l[2][2]:
            return l[1][1]
        elif l[2][0] == l[1][1] == l[0][2]:
            return l[1][1]

    return 0


def is_win(l):

    # make sure it is list of list with 3 x 3
    if len(l) != 3:
        return 'this is not a (3 x 3) game board'

    if check_row(l) > 0:
        print('player %d win in row' % check_row(l))
    elif check_col(l) > 0:
        print('player %d win in col' % check_col(l))
    elif check_diag(l) > 0:
        print('player %d win in diag' % check_diag(l))
    else:
        print('no winner')


if __name__ == '__main__':

    game1 = [[2, 2, 0],
             [2, 1, 0],
             [2, 1, 1]]

    game2 = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 1]]

    game3 = [[0, 1, 0],
             [2, 1, 0],
             [2, 1, 1]]

    game4 = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 2]]

    game5 = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 0]]
    is_win(game1)
    is_win(game2)
    is_win(game3)
    is_win(game4)
    is_win(game5)
