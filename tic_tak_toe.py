board={"T1":" ","T2":" ","T3":" ",
"M1":" ","M2":" ","M3":" ",
"D1":" ","D2":" ","D3":" "}

print("Tic Tac Toe Game")
print("\nT1|T2|T3")
print("- +- +-")
print("M1|M2|M3")
print("- +- +-")
print("D1|D2|D3")

def check():
    if(board['T1']=='X'and board['T2'] =='X' and board['T3']=='X'):
        print('Player one won')
        return 1
    elif (board['M1'] == 'X' and board['M2'] == 'X' and board['M3'] == 'X'):
        print('Player one won')
        return 1
    elif (board['D1'] == 'X' and board['D2'] == 'X' and board['D3'] == 'X'):
        print('Player one won')
        return 1
    elif (board['T1'] == 'X' and board['D1'] == 'X' and board['M1'] == 'X'):
        print('Player one won')
        return 1
    elif (board['T2'] == 'X' and board['M2'] == 'X' and board['D2'] == 'X'):
        print('Player one won')
        return 1
    elif (board['T3'] == 'X' and board['M3'] == 'X' and board['D3'] == 'X'):
        print('Player one won')
        return 1
    elif (board['T1'] == 'X' and board['M2'] == 'X' and board['D3'] == 'X'):
        print('Player one won')
        return 1
    elif (board['T3'] == 'X' and board['M2'] == 'X' and board['D1'] == 'X'):
        print('Player one won')
        return 1
    elif (board['T1'] == 'O' and board['T2'] == 'O' and board['T3'] == 'O'):
        print('Player two won')
        return 1
    elif (board['M1'] == 'O' and board['M2'] == 'O' and board['M3'] == 'O'):
        print('Player two won')
        return 1
    elif (board['D1'] == 'O' and board['D2'] == 'O' and board['D3'] == 'O'):
        print('Player two won')
        return 1
    elif (board['T1'] == 'O' and board['D1'] == 'O' and board['M1'] == 'O'):
        print('Player two won')
        return 1
    elif (board['T2'] == 'O' and board['M2'] == 'O' and board['D2'] == 'O'):
        print('Player two won')
        return 1
    elif (board['T3'] == 'O' and board['M3'] == 'O' and board['D3'] == 'O'):
        print('Player two won')
        return 1
    elif (board['T1'] == 'O' and board['M2'] == 'O' and board['D3'] == 'O'):
        print('Player two won')
        return 1
    elif (board['T3'] == 'O' and board['M2'] == 'O' and board['D1'] == 'O'):
        print('Player two won')
        return 1

player=1
count=0
while True:
    print(board['T1'] + '|' + board['T2'] + '|' + board['T3'])
    print("-+-+-")
    print(board['M1'] + '|' + board['M2'] + '|' + board['M3'])
    print("-+-+-")
    print(board['D1'] + '|' + board['D2'] + '|' + board['D3'])
    if count==9 or check()==1:
        break
    while True:
        if player==1:
            place=input('Player1 Choose your position ')
            if place.upper() in board and board[place.upper()]==' ':
                board[place.upper()]='X'
                player=2
                break
            else:
                print("plz choose valid input")
                continue
        else:
            place = input('Player2 Choose your position ')
            if place.upper() in board and board[place.upper()] == ' ':
                board[place.upper()]= 'O'
                player = 1
                break
            else:
                print("plz choose valid input")
                continue

    count+=1
    print("Match Tie!!")

