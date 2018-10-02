import random
import os
def clear(): 
  
	# linux or os
    os.system('clear') 
    # windows  
	# os.system('cls')
        
def display_board(board):
    	# clear screen before every update
	clear()
	print()
	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')
	print()


def player_input():
    # marker 'x' or 'o'
    marker = ' '
    while not (marker == 'O' or marker == 'X'):
        marker = input("Player 1: Do you want to be x or o ? ").upper()
        
    if marker == 'X':
        return ('X','O')
    elif marker == 'O':
        return ('O','X')
  
    
def place_marker(board, marker, pos):
    board[pos] = marker
    

def win_check(board, mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board, int(position)):
        
        position = int(input('Choose your next position: (1-9) '))
    return position

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

def game_loop():
    print('Welcome to Tic Tac Toe!')

    while True:
        # Reset the board
        theBoard = [' '] * 10
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + ' will go first.')
		# bool variable to check if the game still running
        game_on = True
    
        while game_on:
            if turn == 'Player 1':
                # Player1's turn.
                
                display_board(theBoard)
                print(" {} player1 turn ".format(player1_marker))
                print()
                position = int(player_choice(theBoard))
                place_marker(theBoard, player1_marker, position)
    
                if win_check(theBoard, player1_marker):
                    display_board(theBoard)
                    print('Congratulations! You have won the game!')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'
    
            else:
                # Player2's turn.
                
                display_board(theBoard)
                print(" {} player2 turn ".format(player2_marker))
                print()
                position = player_choice(theBoard)
                place_marker(theBoard, player2_marker, position)
    
                if win_check(theBoard, player2_marker):
                    display_board(theBoard)
                    print('Player 2 has won!')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'Player 1'
    
        if not replay():
            break


def main():
	game_loop()

if __name__ == "__main__":
	main()
