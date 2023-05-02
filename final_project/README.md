# Tic-Tac-Toe Game

### Video Demo: 
https://youtu.be/Ulmx2jQEr-k

## Description: 
This is a simple Tic Tac Toe game built in python.

## Rules of the Game
There will be two players in a game. "X" and "O" represent players. There will be a board with 9 boxes. First, one user will place sign in one available empty boxes, than the second player. The winner will be a player, who place their signs comletely horizontally, vertically or diagonally. the game goes on until a player wins or it ended up in a draw by filling all boxes without a winning match. Than programm will ask, if users want to play again. The users have opinion to game again or quit.

## TODO
- Create a board
- Player, who starts
- User input: row, column
- Update board and player
- Check whether a player has won or not
- Check whether the board is filled or not
- output winner and final view of the board.
- User input: play again or break

### Inputs, Processes, Outputs
Inputs: row, column, game again: Yes or No, option to stop game anytime.

Proccesses: start, play

Output: board, player, position of players, win, draw match, question, notification if something goes wrong.

### Tests
- test create board
- test check win with no winning board
- test check win vertical
- test check win diagonal
- test tie

### Used libraries
random

### Pseudocode
Initialize first player - random
Initialize game board with 9 boxes

Promp for row  and column with "Please enter a position row and column or enter "x" to quit:"

update board with player sign or show message: "Did you attempt to play a row or column outside the range of 0, 1 or 2? try again."

show winner or Match draw

promp for play again or quit.