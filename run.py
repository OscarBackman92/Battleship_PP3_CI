import time
import random
import re

# Define ships globally
ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}


def create_board():
    """
    This function creates a 9x9 empty board with all cells initialized to ' '.
    """
    board = []
    for _ in range(9):
        row = [' '] * 9
        board.append(row)
    return board


def print_board(board, hide_ships=False):
    """
    This function prints the board with the specified rows and columns.
    The board is printed with row numbers on the left and column letters
     on the top.
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



def place_ships(board):
    """
    This function randomly places the ships on the board.
    It checks if the ship can be placed in the specified orientation
    (horizontal or vertical)
    without overlapping with other ships or going out of bounds.
    If the ship can be placed, it updates the board with
    the ship's position.
    The function continues to place ships until all ships
    have been placed successfully.
    """
    global ships
    for ship, size in ships.items():
        placed = False
        while not placed:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                row = random.randint(0, 8)
                col = random.randint(0, 9 - size)
                if all(board[row][col+i] == ' ' for i in range(size)):
                    for i in range(size):
                        board[row][col+i] = 'O'
                    placed = True
            else:
                row = random.randint(0, 9 - size)
                col = random.randint(0, 8)
                if all(board[row+i][col] == ' ' for i in range(size)):
                    for i in range(size):
                        board[row+i][col] = 'O'
                    placed = True

def validate_input(guess, board):
    """
    This function validates the user's input for the guess.
    It checks if the input is in the correct format (e.g., 'A1')
    and within the valid range.
    If the input is valid, it returns True; otherwise, it returns False.
    """
    if len(guess) != 2:
        return False
    col = guess[0].upper()
    row = guess[1:]
    if col not in 'ABCDEFGHI' or row not in '123456789':
        return False
    return True


"""
    This function validates the user's input for the name.
    It checks if the input is empty or contains only whitespace.
    It also checks if the name starts with a number.
    If the input is valid, it returns True; otherwise, it returns False.

"""
def validate_name(name):
    if not name.strip():  # Check if name is empty or contains only whitespace
        return False
    if re.match(r'^[0-9]', name):  # Check if name starts with a number
        return False
    return True

"""
    This function generates a random guess for the computer player.
    It randomly selects a row and column on the board that has not been guessed before.
    If the selected cell is empty or contains a ship, it returns the row and column.
"""
def computer_guess(board):
    while True:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] == ' ' or board[row][col] == 'O':
            return row, col


def play_game():
    """
    This function is the main game loop where the player and computer take turns guessing each other's ships.
    It displays the player's board, the computer's board, and prompts the player to enter a guess.
    The player can enter 'exit' to quit the game at any time.
    The game continues until all the ships of either the player or the computer have been sunk.
    It also keeps track of the number of guesses made by the player and the computer.
    """
    # Validate name input
    name = input('Enter your name: ')
    while not validate_name(name):
        print('Invalid name. Please enter a valid name.')
        name = input('Enter your name: ')
        time.sleep(1)

    input('Press Enter to start the game...')

    global ships
    player_board = create_board()
    computer_board = create_board()

    print('Placing ships on the board...')
    time.sleep(2)

    place_ships(player_board)
    place_ships(computer_board)
    player_ships_sunk = {'Carrier': False, 'Battleship': False, 'Cruiser': False, 'Submarine': False, 'Destroyer': False}
    computer_ships_sunk = {'Carrier': False, 'Battleship': False, 'Cruiser': False, 'Submarine': False, 'Destroyer': False}
    guesses = 0
    guessed_coords = set()  # Set to store guessed coordinates


    while True:
        print('Player Board:')
        print_board(player_board)
        print('Computer Board:')
        print_board(computer_board, hide_ships=True)
        guess = input('Enter your guess (e.g. A1), or type "exit" to quit: ')

        # Check if the player wants to exit
        if guess.lower() == 'exit':
            print('Quitting the game...')
            return

        # Check if guess is valid
        if not validate_input(guess, computer_board):
            print('Invalid input. Please enter a valid guess.')
            continue

        # Check if guess has already been made
        col = guess[0].upper()
        row = int(guess[1:]) - 1
        if (row, ord(col) - ord('A')) in guessed_coords:
            print('You have already guessed that coordinate. Please try again.')
            continue

        # Add current guess to guessed coordinates
        guessed_coords.add((row, ord(col) - ord('A')))

        # Process the guess
        # Now guessing on computer's board
        if computer_board[row][ord(col) - ord('A')] == 'O':   
            computer_board[row][ord(col) - ord('A')] = 'X'
            print('Hit!')

            # Add delay for dramatic effect
            time.sleep(1)  

            # Check if a ship has been sunk
            for ship, size in ships.items():
                if all(cell == 'X' for cell in computer_board[row]) or \
                        all(computer_board[i][ord(col) - ord('A')] == 'X' for i in range(9)):
                    print(f'Computer {ship} sunk!')
                    computer_ships_sunk[ship] = True
                    break
        else:
            computer_board[row][ord(col) - ord('A')] = 'M'
            print('Miss!')

        guesses += 1
        if all(computer_ships_sunk.values()):
            print('Congratulations! You sunk all the computer\'s ships. You win!')
            print(f'Total Guesses: {guesses}')
            break

        # Now computer guesses on player's board
        computer_row, computer_col = computer_guess(player_board)  

        # Now guessing on player's board
        if player_board[computer_row][computer_col] == 'O':  
            player_board[computer_row][computer_col] = 'X'
            print('Computer hit your ship!')

            # Add delay for dramatic effect
            time.sleep(1)  

            # Check if a ship has been sunk
            for ship, size in ships.items():
                if all(cell == 'X' for cell in player_board[computer_row]) or \
                        all(player_board[i][computer_col] == 'X' for i in range(9)):
                    print(f'Your {ship} has been sunk!')
                    player_ships_sunk[ship] = True
                    break
        else:
            player_board[computer_row][computer_col] = 'M'
            print(f"Computer guessed {chr(computer_col + ord('A'))}{computer_row + 1}")

        guesses += 1
        if all(player_ships_sunk.values()):
            print('Game Over! All your ships have been sunk. Better luck next time.')
            print(f'Total Guesses: {guesses}')
            break

        print('Computer missed your ship!')
        time.sleep(1)

# Main function to start the game

print('Welcome to Battleship!')
play_game()
print('Thanks for playing!')
