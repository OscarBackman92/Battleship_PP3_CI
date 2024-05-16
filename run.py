import random

# Function to create an empty board
def create_board():
    board = []
    for _ in range(9):
        row = [' '] * 9
        board.append(row)
    return board

# Function to print the board
def print_board(board, hide_ships=False):
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

# Function to place ships randomly on the board
def place_ships(board):
    ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
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

# Function to validate user input
def validate_input(guess, board):
    if len(guess) != 2:
        return False
    col = guess[0].upper()
    row = guess[1:]
    if col not in 'ABCDEFGHI' or row not in '123456789':
        return False
    return True

# Function for computer to make a random guess
def computer_guess(board):
    while True:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] == ' ' or board[row][col] == 'O':
            return row, col

# Function to play the game
def play_game():
    player_board = create_board()
    computer_board = create_board()
    place_ships(player_board)
    place_ships(computer_board)
    guesses = 0
    guessed_coords = set()  # Set to store guessed coordinates

    while True:
        print('Player Board:')
        print_board(player_board)
        print('Computer Board:')
        print_board(computer_board, hide_ships=True)
        guess = input('Enter your guess (e.g. A1): ')

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
        if computer_board[row][ord(col) - ord('A')] == 'O':   # Now guessing on computer's board
            computer_board[row][ord(col) - ord('A')] = 'X'
            print('Hit!')
        else:
            computer_board[row][ord(col) - ord('A')] = 'M'
            print('Miss!')
        guesses += 1
        if all(all(cell != 'O' for cell in row) for row in computer_board):  # Checking computer's board
            print('Game Ended')
            print(f'Total Guesses: {guesses}')
            break
        computer_row, computer_col = computer_guess(player_board)  # Now computer guesses on player's board
        if player_board[computer_row][computer_col] == 'O':  # Now guessing on player's board
            player_board[computer_row][computer_col] = 'X'
            print('Computer hit your ship!')
        else:
            player_board[computer_row][computer_col] = 'M'
            print('Computer missed your ship!')
        print(f"Computer guessed {chr(computer_col + ord('A'))}{computer_row + 1}")

# Main program
print('Welcome to Battleship!')
name = input('Enter your name: ')
print(f'Hello, {name}!')
input('Press Enter to start the game...')
play_game()
