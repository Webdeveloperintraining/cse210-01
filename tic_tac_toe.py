#Author:Irvin Silva -- Subject CSE 210 -- Instructor name: Brother Duane Richards
def main():
    round=0
    player=0
    print("Welcome to Tic-Tac-Toe")
    board=make_board()
    while not win_condition(board):
        display_board(board)
        player=players(round)
        play(player,board)
        round+=1
        if round > 8:
            break
    display_board(board)
    print('Game Over')
    
def make_board():
    board=[]
    for i in range (9):
        board.append(i+1)
    return board

def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def players(round):
    if round in range(0,10,2):
        player="X"
    else:
        player="O"
    return player

def play(player,game):
    move=int(input(f'Player {player}, please select a number (1-9) '))
    while move not in game:   
        print("Sorry, that's an invalid input, please try again")
        move=int(input(f'Player {player}, please select a number (1-9) '))
    game[move - 1] = player
    return game

def win_condition(board):
    return (board[0] == board[1] == board[2] or
        board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or
        board[0] == board[3] == board[6] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8] or
        board[0] == board[4] == board[8] or
        board[2] == board[4] == board[6])

main()