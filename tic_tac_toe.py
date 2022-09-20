# #Author:Irvin Silva -- Subject CSE 210 -- Instructor name: Brother Duane Richards

def main():
    round=0
    print("Welcome to Tic-Tac-Toe")
    game="1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9"
    print(game)

    while round !=5:
        move1=str(input('Please select a number (1-9) '))
        while move1 not in game:       
            print("Sorry, that's an invalid input, please try again")
            move1=str(input('Please select a number (1-9) '))
        else:
            game= game.replace(move1,"X")
        print(game)

        move2=str(input('Please select a number (1-9) '))        
        while move2 not in game:   
            print("Sorry, that's an invalid input, please try again")
            move2=str(input('Please select a number (1-9) ')) 
        else:
            game= game.replace(move2,"O")
        print(game)
        if win_condition(game):
            break
        round+=1


    
    print('Game Over')

def win_condition(game):
    win_conditions1=["X|X|X\n-+-+-\n4|5|6\n-+-+-\n7|8|9","1|2|3\n-+-+-\nX|X|X\n-+-+-\n7|8|9","1|2|3\n-+-+-\n4|5|6\n-+-+-\nX|X|X","X|2|3\n-+-+-\n4|X|6\n-+-+-\n7|8|X","1|2|X\n-+-+-\n4|X|6\n-+-+-\nX|8|9","X|2|3\n-+-+-\nX|5|6\n-+-+-\nX|8|9","1|X|3\n-+-+-\n4|X|6\n-+-+-\n7|X|9","1|2|X\n-+-+-\n4|5|X\n-+-+-\n7|8|X"]
    win_conditions2=["O|O|O\n-+-+-\n4|5|6\n-+-+-\n7|8|9","1|2|3\n-+-+-\nO|O|O\n-+-+-\n7|8|9","1|2|3\n-+-+-\n4|5|6\n-+-+-\nO|O|O","O|2|3\n-+-+-\n4|O|6\n-+-+-\n7|8|O","1|2|O\n-+-+-\n4|O|6\n-+-+-\nO|8|9","O|2|3\n-+-+-\nO|5|6\n-+-+-\nO|8|9","1|O|3\n-+-+-\n4|O|6\n-+-+-\n7|O|9","1|2|O\n-+-+-\n4|5|O\n-+-+-\n7|8|O"]
    if game in win_conditions1:
        print("Thanks for playing, player 1 wins")
    elif game in win_conditions2:
        print("Thanks for playing, player 2 wins")

main()





