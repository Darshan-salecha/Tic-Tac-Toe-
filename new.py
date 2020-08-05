board={7:" ",8:" ",9:" ",
4:" ",5:" ",6:" ",
1:" ",2:" ",3:" "}

print("Tic Tac Toe Game")
print("\nT1|T2|T3")
print("- +- +-")
print("M1|M2|M3")
print("- +- +-")
print("D1|D2|D3")

def check():
    if(board[1]=='X'and board[2] =='X' and board[3]=='X'):
        print('Player one won')
        return 1
    elif (board[4] == 'X' and board[5] == 'X' and board[6] == 'X'):
        print('Player one won')
        return 1
    elif (board[7] == 'X' and board[8] == 'X' and board[9] == 'X'):
        print('Player one won')
        return 1
    elif (board[1] == 'X' and board[4] == 'X' and board[7] == 'X'):
        print('Player one won')
        return 1
    elif (board[2] == 'X' and board[5] == 'X' and board[8] == 'X'):
        print('Player one won')
        return 1
    elif (board[3] == 'X' and board[6] == 'X' and board[9] == 'X'):
        print('Player one won')
        return 1
    elif (board[1] == 'X' and board[5] == 'X' and board[9] == 'X'):
        print('Player one won')
        return 1
    elif (board[3] == 'X' and board[5] == 'X' and board[7] == 'X'):
        print('Player one won')
        return 1
    elif (board[1] == 'O' and board[2] == 'O' and board[3] == 'O'):
        print('Player two won')
        return 1
    elif (board[4] == 'O' and board[5] == 'O' and board[6] == 'O'):
        print('Player two won')
        return 1
    elif (board[7] == 'O' and board[8] == 'O' and board[9] == 'O'):
        print('Player two won')
        return 1
    elif (board[1] == 'O' and board[4] == 'O' and board[7] == 'O'):
        print('Player two won')
        return 1
    elif (board[2] == 'O' and board[5] == 'O' and board[8] == 'O'):
        print('Player two won')
        return 1
    elif (board[3] == 'O' and board[6] == 'O' and board[9] == 'O'):
        print('Player two won')
        return 1
    elif (board[1] == 'O' and board[5] == 'O' and board[9] == 'O'):
        print('Player two won')
        return 1
    elif (board[3] == 'O' and board[5] == 'O' and board[7] == 'O'):
        print('Player two won')
        return 1

player=1
count=0
while True:
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("-+-+-")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("-+-+-")
    print(board[1] + '|' + board[2] + '|' + board[3])
    if count==9 or check()==1:
        break
    while True:
        if player==1:
            place=int(input('Player1 Choose your position '))
            if 0<=place<=9  and board[place]==' ':
                board[place]='X'
                player=2
                break
            else:
                print("plz choose valid input")
                continue
        else:
            place = int(input('Player2 Choose your position '))
            if 0<place<=9  and board[place] == ' ':
                board[place]= 'O'
                player = 1
                break
            else:
                print("plz choose valid input")
                continue

    count+=1
    print("Match Tie!!")
