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
def set_symbol(znak):#będzie jeszcze argument x_board
    if znak == True:
        symbol = 'O'
    else:
        symbol = 'X'
    ok_or_not = False
    while ok_or_not==False:
        print( "Gdzie chcesz postawić " + symbol+ "? :" )
        place=input()
        if len(place)==2:
            if 0<=int(place[1])<=2:
                if place[0].upper() in ['A','B','C']:
                    #change board
                    ok_or_not=True
                else:
                    print("Niepoprawna wartość. Pierwsza współrzędna powinna być literą A lub B lub C")
            else:
                print("Niepoprawna wartość. Druga współrzędna powinna się składać z liczby od 0 do 2.")
        else:
            print("Niepoprawna wartość. Współrzędne powinny składać się z dwóch znaków")

    print("test udany")


    pass 

#inicjalizacja planszy
board = [['_' for _ in range(3)]for _ in range(3)]
sign = True
set_symbol(sign)

print_board(board)
