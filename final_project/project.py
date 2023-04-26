import random

def main():
    player = get_random_first_player()
    if player == 1:
        player = "X"
    else:
        player = "O"

    board = create_board()
    while True:
        print_board(board)
        
        print (f"Player: {player}")
        try:
            user_input = input("Please enter a position row and column or enter \"x\" to quit: ")
            if quit(user_input): break

            # taking user input
            r, col = list(map(int, user_input.split()))
            print()

            if r < 0 or r > 2 or col < 0 or col > 2:
                print("\n ❌  Did you attempt to play a row or column outside the range of 0, 1 or 2? try again.  ❌ \n")
                continue
            elif board[r][col] != "-":
                print("\n ❌  This space is occupied, try another!  ❌ \n")
                continue
            
            board[r][col] = player

            if check_win(board, player):
                print(f"    congratulations !! 🎉 Player {player} won!!  🥇 \n")
                break

            if check_tie(board):
                print(" Match Draw! 🔥")
                break
            else:
                # swapping the player 
                player = "X" if player == "O" else "O"
        except ValueError:
            print( "\n ❌  Invalid input. Please enter two integers separated by a space.  ❌ \n" )
            pass

# create an empty 3x3 board
def create_board():
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append('-')
        board.append(row)
    return board

def print_board(board):
    print("   0  1  2")
    for i in range(len(board)):
        row_str = f"{i}  "
        for j in range(len(board[i])):
            row_str += f"{board[i][j]}  "
        print(row_str)

# first player is chosen ramdonly
def get_random_first_player():
    return random.randint(1, 2)

# if user doesn't want to continue the game, there is always option to leave. with press a programm exit
def quit(user_input):
    if user_input == "x":
        print("Thanks for playing")
        return True
    else: return False

def check_win(board, player):
    win = None
    n = len(board)
    # checking rows
    for i in range(n):
        win = True
        for j in range(n):
            if board[i][j] != player:
                win = False
                break
        if win:
            return win

    # checking columns
    for i in range(n):
        win = True
        for j in range(n):
            if board[j][i] != player:
                win = False
                break
        if win:
            return win

    # checking diagonals
    win = True
    for i in range(n):
        if board[i][i] != player:
            win = False
            break
    if win:
        return win

    win = True
    for i in range(n):
        if board[i][n - 1 - i] != player:
            win = False
            break
    if win:
        return win
    return False

def check_tie(board):
    for row in board:
        if "-" in row:
            return False
    return True



if __name__ == "__main__":
    main()