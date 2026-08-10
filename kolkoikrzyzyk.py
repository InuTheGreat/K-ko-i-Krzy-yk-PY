#kółko i krzyżyk

#rysowanie planszy w terminalu
def print_board(x_board):
    print("   A B C ")
    for x in range(len(x_board)):
        print(x,end='  ') 
        for y in range(len(x_board[x])):
            print(x_board[x][y],end=' ')
        print()

#ustawianie kółka bądź krzyżyka
def set_symbol(x_board, znak):
    if znak == True:
        symbol = 'O'
    else:
        symbol = 'X'
    ok_or_not = False
    while ok_or_not==False:
        print( "Gdzie chcesz postawić " + symbol+ "? :" )
        place=input()
        if len(place)==2 and 0<=int(place[0])<=2 and (place[1].upper in ['A','B','C']):
            #change board
            ok_or_not=True
        else:
            print("Niepoprawna wartość.")


    pass 

#inicjalizacja planszy
board = [['_' for _ in range(3)]for _ in range(3)]


print_board(board)
