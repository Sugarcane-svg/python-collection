# refactor the code into function in exercise 24(draw a game board)

# the original code was like(3x3):
# def printBoard():
#     print(" --- --- ---")
#     print("|   |   |   |")

# printBoard()
# printBoard()
# printBoard()
# print(" --- --- ---")

# what if we want to print 4 x 4, 8 x 8

a = " ---"
b = "|   "

def printSingle(r):
    print(a*r)
    print(b*(r+1))

def drawBoard(r, c):
    for i in range(c):
        printSingle(r)
    print(a*r)

#drawBoard(3,4)
drawBoard(8, 8)
