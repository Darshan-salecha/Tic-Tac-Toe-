import math
import random
board={7:" ",8:" ",9:" ",
4:" ",5:" ",6:" ",
1:" ",2:" ",3:" "}

print("Tic Tac Toe Game")
print("\nT1|T2|T3")
print("- +- +-")
print("M1|M2|M3")
print("- +- +-")
print("D1|D2|D3")

def check(count):
    if(board[1]=='X'and board[2] =='X' and board[3]=='X'):
        return 'X'
    elif (board[4] == 'X' and board[5] == 'X' and board[6] == 'X'):
        return 'X'
    elif (board[7] == 'X' and board[8] == 'X' and board[9] == 'X'):
        return 'X'
    elif (board[1] == 'X' and board[4] == 'X' and board[7] == 'X'):
        return 'X'
    elif (board[2] == 'X' and board[5] == 'X' and board[8] == 'X'):
        return 'X'
    elif (board[3] == 'X' and board[6] == 'X' and board[9] == 'X'):
        return 'X'
    elif (board[1] == 'X' and board[5] == 'X' and board[9] == 'X'):
        return 'X'
    elif (board[3] == 'X' and board[5] == 'X' and board[7] == 'X'):
        return 'X'
    elif (board[1] == 'O' and board[2] == 'O' and board[3] == 'O'):
        return 'O'
    elif (board[4] == 'O' and board[5] == 'O' and board[6] == 'O'):
        return 'O'
    elif (board[7] == 'O' and board[8] == 'O' and board[9] == 'O'):
        return 'O'
    elif (board[1] == 'O' and board[4] == 'O' and board[7] == 'O'):
        return 'O'
    elif (board[2] == 'O' and board[5] == 'O' and board[8] == 'O'):
        return 'O'
    elif (board[3] == 'O' and board[6] == 'O' and board[9] == 'O'):
        return 'O'
    elif (board[1] == 'O' and board[5] == 'O' and board[9] == 'O'):
        return 'O'
    elif (board[3] == 'O' and board[5] == 'O' and board[7] == 'O'):
        return 'O'
    elif count==9:
        return 'tie'
    else:
        return 0
player=1
count=0
scores={'X':10,'O':-10,'tie':0}
def minimax(board,depth,maximizing,count):
    result=check(count)
    if(result!=0):
        return scores[result]
    elif(maximizing):
        best_score = -math.inf
        for i in range(1, 10):
            if (board[i] == ' '):
                board[i] = 'X'
                score = minimax(board,depth+1, False,count)
                board[i] = ' '
                best_score=max(score,best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(1, 10):
            if (board[i] == ' '):
                board[i] = 'O'
                score = minimax(board, depth + 1, True,count)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score




def ai_move():
    best_score= -math.inf
    move=0
    for i in range(1,10):
        if(board[i]==' '):
            board[i]='X'
            score=minimax(board,0,False,count)
            board[i]=' '
            if(score>best_score):
                best_score=score
                move=i
    board[move]='X'



while True:
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("-+-+-")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("-+-+-")
    print(board[1] + '|' + board[2] + '|' + board[3])

    print('\n')
    if check(count)!=0:
        if check(count)=='X':
            print('Computer wins')
        elif check(count)=='O':
            print('Player wins')
        else:
            print('Match Tie')
        break
    while True:
        if player==1:
            print('computer turn')
            if count==0:
                place=random.randint(1,9)
                board[place] = 'X'
            else:

                ai_move()
            player=2
            break
        else:
            place = int(input('Player Choose your position '))
            if 0<place<=9  and board[place] == ' ':
                board[place]= 'O'
                player = 1
                break
            else:
                print("plz choose valid input")
                continue

    count+=1
