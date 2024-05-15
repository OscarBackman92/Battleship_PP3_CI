import random

# Function to create an empty board
def create_board():
    board = []
    for _ in range(9):
        row = [' '] * 9
        board.append(row)
    return board

# Function to print the board
def print_board(board):
    print('   A B C D E F G H I')
    print('  -------------------')
    for i in range(9):
        print(f'{i+1} |{"|".join(board[i])}|')
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
def validate_input(guess):
    if len(guess) != 2:
        return False
    col = guess[0].upper()
    row = guess[1:]
    if col not in 'ABCDEFGHI' or row not in '123456789':
        return False
    return True

# Function to play the game
def play_game():
    player_board = create_board()
    computer_board = create_board()
    place_ships(player_board)
    place_ships(computer_board)
    guesses = 0
    while True:
        print('Player Board:')
        print_board(player_board)
        print('Computer Board:')
        print_board(computer_board)
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
            player_board[row][ord(col) - ord('A')] = '-'
            print('Miss!')
        guesses += 1
        if all(all(cell != 'O' for cell in row) for row in player_board):
            print('Game Ended')
            print(f'Total Guesses: {guesses}')
            break

# Main program
print('Welcome to Battleship!')
name = input('Enter your name: ')
print(f'Hello, {name}!')
input('Press Enter to start the game...')
play_game()