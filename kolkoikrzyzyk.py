#kółko i krzyżyk
#TODO 
#tryby gry gracz vs gracz i gracz vs komputer


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
        if place[1].isnumeric():
            if len(place)==2:
                if 0<=int(place[1])<=2:
                    if place[0] in ['A','B','C']:
                        t_place = translate_coord(place)
                        if check_if_present(x_board, t_place):
                            x_board=change_board(x_board,symbol,t_place)
                            if znak == True:
                                znak = False
                            else:
                                znak=True
                            ok_or_not=True
                            return x_board, znak
                    else:
                        print("Niepoprawna wartość. Pierwsza współrzędna powinna być literą A lub B lub C")
                else:
                    print("Niepoprawna wartość. Druga współrzędna powinna się składać z liczby od 0 do 2.")
            else:
                print("Niepoprawna wartość. Współrzędne powinny składać się z dwóch znaków")
        else:
            print("Niepoprawna wartość. Pierwsza współrzędna powinna być literą A lub B lub C.\n Druga współrzędna powinna się składać z liczby od 0 do 2.")

    


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

def winning_condition_check(x_board): #sprawdzamy, czy ktoś wygrał
    
    for x in range(len(x_board)):
        board_val=[]
        for y in range (len(x_board[x])):
            if x_board[y][x]=='_':
                break
            else:
                board_val.append(x_board[y][x])
            if len(board_val)==3:
                if board_val[0]==board_val[1] and board_val[1]==board_val[2]:
                    print_board(x_board)
                    print("WYGRAŁ "+ board_val[0])
                    return False
    for x in range(len(x_board)):
            board_val=[]
            for y in range (len(x_board[x])):
                if x_board[x][y]=='_':
                    break
                else:
                    board_val.append(x_board[x][y])
                if len(board_val)==3:
                    if board_val[0]==board_val[1] and board_val[1]==board_val[2]:
                        print_board(x_board)
                        print("WYGRAŁ "+ board_val[0])
                        return False
    if x_board[1][1]!='_':
        if x_board[1][1]==x_board[0][0] and x_board[0][0]==x_board[2][2]:
            print_board(x_board)
            print("WYGRAŁ "+ x_board[1][1])
            return False
        if x_board[1][1]==x_board[0][2] and x_board[0][2]==x_board[2][0]:
                    print_board(x_board)
                    print("WYGRAŁ "+ x_board[1][1])
                    return False
    return True

#inicjalizacja planszy
board = [['_' for _ in range(3)]for _ in range(3)]
sign = True
game = True
while game == True:#główna pętla gry
    print_board(board)
    board, sign = check_symbol(board, sign)
    game = winning_condition_check(board)
