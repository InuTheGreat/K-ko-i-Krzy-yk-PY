#kółko i krzyżyk

#rysowanie planszy w terminalu
def print_board(x_board):
    print("   A B C ")
    for x in range(len(x_board)):
        print(x,end='  ') 
        for y in range(len(x_board[x])):
            print(x_board[y][x],end=' ')
        print()

#wpisujemy O bądź X i sprawdzamy, czy współrzędne są poprawne
def check_symbol(x_board, znak):
    if znak == True:
        symbol = 'O'
    else:
        symbol = 'X'
    ok_or_not = False
    while ok_or_not==False:
        print( "Gdzie chcesz postawić " + symbol+ "?" )
        print("Pamiętaj aby podać porawnie współrzędne: ")
        place=input()
        place=place.upper()
        if len(place)==2:
            if 0<=int(place[1])<=2:
                if place[0] in ['A','B','C']:
                    t_place = translate_coord(place)
                    if check_if_present(x_board, t_place):
                        x_board=change_board(x_board,symbol,t_place)
                        if symbol == True:
                            symbol = False
                        else:
                            symbol=True
                        ok_or_not=True
                        return x_board
                else:
                    print("Niepoprawna wartość. Pierwsza współrzędna powinna być literą A lub B lub C")
            else:
                print("Niepoprawna wartość. Druga współrzędna powinna się składać z liczby od 0 do 2.")
        else:
            print("Niepoprawna wartość. Współrzędne powinny składać się z dwóch znaków")

    


def check_if_present(x_board,miejsce):
    loop_check = False
    if x_board[miejsce[0]][miejsce[1]]=='_':
        loop_check = True
    else:
        print("Na tym miejscu stoi już inna figura!")
    return loop_check

def translate_coord(coord): #zamieniamy współrzędne typu litery na cyfry
    coord_dict = {
        'A':0,
        'B':1,
        'C':2
    }
    translated_coord = [coord_dict[coord[0]],int(coord[1])]
    return translated_coord


def change_board(x_board,symbol,place):
    x_board[place[0]][place[1]]=symbol
    return x_board

#inicjalizacja planszy
board = [['_' for _ in range(3)]for _ in range(3)]
while True:#główna pętla gry

    sign = True
    board = check_symbol(board, sign)

    print_board(board)
