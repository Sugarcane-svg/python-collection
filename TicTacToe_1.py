
def build_row(size):
    r = ''
    for row in range(size):
        r += " " + horizontal
    return r


def build_col(size):
    c = ''
    for col in range(size+1):
        c += verticle + "   "
    return c


def build_board(size):
    row = build_row(size)
    col = build_col(size)
    for i in range(2*size+1):
        if i % 2 == 0:
            print(row)
        else:
            print(col)


if __name__ == '__main__':
    size = int(input('size of your game board?(it will be square): '))
    verticle = '|'
    horizontal = '---'

    build_board(size)
