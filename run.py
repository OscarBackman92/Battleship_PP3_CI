import random

def create_board():
    """
    Function to create an empty board.
    """
    board = []
    for _ in range(9):
        row = [' '] * 9
        board.append(row)
    return board

def print_board(board, hide_ships=False):
    """
    Function to print the board.
    """
    print('   A B C D E F G H I')
    print('  -------------------')
    for i in range(9):
        row = []
        for j in range(9):
            if hide_ships and board[i][j] == 'O':
                row.append(' ')
            else:
                row.append(board[i][j])
        print(f'{i+1} |{"|".join(row)}|')
        print('  -------------------')

# Add docstrings to the remaining functions...

def play_game():
    """
    Function to play the game.
    """
    player_board = create_board()
    computer_board = create_board()
    place_ships(player_board)
    place_ships(computer_board)
    guesses = 0
    while True:
        print('Player Board:')
        print_board(player_board)
        print('Computer Board:')
        print_board(computer_board, hide_ships=True)
        guess = input('Enter your guess (e.g. A1): ')
        if not validate_input(guess):
            print('Invalid input. Please enter a valid guess.')
            continue
        col = guess[0].upper()
        row = int(guess[1:]) - 1
        if player_board[row][ord(col) - ord('A')] == 'O':   
            player_board[row][ord(col) - ord('A')] = 'X'
            print('Hit!')
        else:
            player_board[row][ord(col) - ord('A')] = 'M'
            print('Miss!')
        guesses += 1
        if all(all(cell != 'O' for cell in row) for row in player_board):
            print('Game Ended')
            print(f'Total Guesses: {guesses}')
            break
        computer_row, computer_col = computer_guess(computer_board)
        if computer_board[computer_row][computer_col] == 'O':
            computer_board[computer_row][computer_col] = 'X'
            print('Computer hit your ship!')
        else:
            computer_board[computer_row][computer_col] = 'M'
            print('Computer missed your ship!')
        print(f"Computer guessed {chr(computer_col + ord('A'))}{computer_row + 1}")

# Main program
print('Welcome to Battleship!')
name = input('Enter your name: ')
print(f'Hello, {name}!')
input('Press Enter to start the game...')
play_game()
