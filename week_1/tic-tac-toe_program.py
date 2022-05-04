#Tic-Tac-Toe Program CSE 210, by Irvin Silva 

def main():
    print('Welcome to Tic-Tac-Toe game\nInstructions:\n')
    print('Each player will type a number between 1 and 9 representing\nthe squares formed by the grid."X" is for player one and "O" for player two.\nThe first player who connects three Xs or Os (horizontally,vertically or diagonally) wins.')
    grid=create_grid()
    round=0
    print()
    game(grid)
    print()
    while not (has_winner(grid) or is_a_draw(grid)):
        turn=round+1
        player=define_player(turn)
        play=int(input(f"{player}'s turn to choose a square (1-9):")) 
        print()
        grid[play-1]=player
        game(grid)
        print()
        round+=1
        if is_a_draw(grid)==False:
            if player=='X':
                player='Player 1'
                print(f"The winner is {player}!!!")
            else:
                player='Player 2'
                print(f"The winner is {player}!!!")
    print('Good game. Thanks for playing!')

def create_grid():
    options=[]
    for i in range(9):
        options.append(i+1)
    return options

def game(list):
    print(f'{list[0]}|{list[1]}|{list[2]}\n-+-+-\n{list[3]}|{list[4]}|{list[5]}\n-+-+-\n{list[6]}|{list[7]}|{list[8]}')
    
def has_winner(grid):
    return (grid[0] == grid[1] == grid[2] or
            grid[3] == grid[4] == grid[5] or
            grid[6] == grid[7] == grid[8] or
            grid[0] == grid[3] == grid[6] or
            grid[1] == grid[4] == grid[7] or
            grid[2] == grid[5] == grid[8] or
            grid[0] == grid[4] == grid[8] or
            grid[2] == grid[4] == grid[6])
           
def is_a_draw(grid):
    for square in range(9):
        if grid[square] != "X" and grid[square] != "O":
            return False
    print("It's a tie")
    return True 

def define_player(round):
    player=' '
    if round in [1,3,5,7,9,11,13,15,17,19,21]:
        player='X'
    elif round in [2,4,6,8,10,12,14,16,18,20]:
        player='O'
    return player
main()
