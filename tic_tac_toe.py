# #Author:Irvin Silva -- Subject CSE 210 -- Instructor name: Brother Duane Richards

def main():
    round=0
    win_conditions=["X|X|X\n-+-+-\n4|5|6\n-+-+-\n7|8|9","1|2|3\n-+-+-\nX|X|X\n-+-+-\n7|8|9","1|2|3\n-+-+-\n4|5|6\n-+-+-\nX|X|X","X|2|3\n-+-+-\n4|X|6\n-+-+-\n7|8|X","1|2|X\n-+-+-\n4|X|6\n-+-+-\nX|8|9","X|2|3\n-+-+-\nX|5|6\n-+-+-\nX|8|9","1|X|3\n-+-+-\n4|X|6\n-+-+-\n7|X|9","1|2|X\n-+-+-\n4|5|X\n-+-+-\n7|8|X","O|O|O\n-+-+-\n4|5|6\n-+-+-\n7|8|9","1|2|3\n-+-+-\nO|O|O\n-+-+-\n7|8|9","1|2|3\n-+-+-\n4|5|6\n-+-+-\nO|O|O","O|2|3\n-+-+-\n4|O|6\n-+-+-\n7|8|O","1|2|O\n-+-+-\n4|O|6\n-+-+-\nO|8|9","O|2|3\n-+-+-\nO|5|6\n-+-+-\nO|8|9","1|O|3\n-+-+-\n4|O|6\n-+-+-\n7|O|9","1|2|O\n-+-+-\n4|5|O\n-+-+-\n7|8|O"]
    print("Welcome to Tic-Tac-Toe")
    game="1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9"
    print(game)  
    while round !=5:
        move1=str(input('Please select a number (1-9) '))        
        if move1 not in game:
            print("Sorry, that's an invalid input, please try again")
        else:
            game= game.replace(move1,"X")
        print(game)
        move2=str(input('Please select a number (1-9) '))        
        if move2 not in game:
            print("Sorry, that's an invalid input, please try again")
        else:
            game= game.replace(move2,"O")
        print(game)
        round+=1
        print (round)
    print('game over')
main()





#win_conditions2=["O|O|O\n-+-+-\n4|5|6\n-+-+-\n7|8|9","1|2|3\n-+-+-\nO|O|O\n-+-+-\n7|8|9","1|2|3\n-+-+-\n4|5|6\n-+-+-\nO|O|O","O|2|3\n-+-+-\n4|O|6\n-+-+-\n7|8|O","1|2|O\n-+-+-\n4|O|6\n-+-+-\nO|8|9","O|2|3\n-+-+-\nO|5|6\n-+-+-\nO|8|9","1|O|3\n-+-+-\n4|O|6\n-+-+-\n7|O|9","1|2|O\n-+-+-\n4|5|O\n-+-+-\n7|8|O"]
