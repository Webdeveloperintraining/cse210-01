#Author:Irvin Silva -- Subject CSE 210 -- Instructor name: Brother Duane Richards
def main():
    round=0
    player=0
    print("Welcome to Tic-Tac-Toe")
    game="1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9"
    print(game)
    while round<=8:
        player=players(round)
        game=play(player,game)
        print(game)
        round+=1
        print()
        if win_condition(game,player):
            #print(f"Thanks for playing, Player {player} wins")
            break
    #print(f"Thanks for playing, Player {player} wins")
    print('Game Over')
    

def players(round):
    if round in range(0,10,2):
        player="X"
    else:
        player="O"
    return player

def play(player,game):
    move=str(input(f'Player {player}, please select a number (1-9) '))
    while move not in game:   
        print("Sorry, that's an invalid input, please try again")
        move=str(input('Please select a number (1-9) ')) 
    game= game.replace(move,player)
    return game

def win_condition(game,player):
    if player == game[0]== game[2] == game[4] or game[12]== game[14] == game[16] or game[24]== game[26] == game[28] or game[0]== game[14] == game[28] or game[4]== game[14] == game[24] or game[0]== game[12] == game[24] or game[2]== game[14] == game[4] or game[0]== game[16] == game[28]:
        print('Game over')        

main()