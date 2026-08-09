#kółko i krzyżyk
def print_board(x_board):
    for x in range(len(x_board)):
        for y in range(len(x_board[x])):
            print(x_board[x][y],end=' ')
        print()
    


board = [['_' for _ in range(3)]for _ in range(3)]


print_board(board)
