import random
import re
import time
import emoji
import colorama
emoji.emojize("")


# Define ships globally
ships = {
    'Carrier': 5,
    'Battleship': 4,
    'Cruiser': 3,
    'Submarine': 3,
    'Destroyer': 2
}


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
    (horizontal or vertical) without overlapping with other ships
    or going out of bounds.
    If the ship can be placed, it updates the board with
    the ship's position.
    The function continues to place ships until all ships
    have been placed successfully.
    """
    global ships
    ship_positions = {ship: [] for ship in ships}
    for ship, size in ships.items():
        placed = False
        while not placed:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                row = random.randint(0, 8)
                col = random.randint(0, 9 - size)
                if all(board[row][col + i] == ' ' for i in range(size)):
                    for i in range(size):
                        board[row][col + i] = 'O'
                        ship_positions[ship].append((row, col + i))
                    placed = True
            else:
                row = random.randint(0, 9 - size)
                col = random.randint(0, 8)
                if all(board[row + i][col] == ' ' for i in range(size)):
                    for i in range(size):
                        board[row + i][col] = 'O'
                        ship_positions[ship].append((row + i, col))
                    placed = True
    return ship_positions


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


def validate_name(name):
    """
    This function validates the user's input for the name.
    It checks if the input is empty or contains only whitespace.
    It also checks if the name starts with a number.
    If the input is valid, it returns True; otherwise, it returns False.
    """
    if not name.strip():  # Check if name is empty or contains only whitespace
        return False
    if re.match(r'^[0-9]', name):  # Check if name starts with a number
        return False
    return True


def computer_guess(board):
    """
    This function generates a random guess for the computer player.
    It randomly selects a row and column on the board that has not been
    guessed before.
    If the selected cell is empty or contains a ship, it returns the row
    and column.
    """
    while True:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] == ' ' or board[row][col] == 'O':
            return row, col


def is_ship_sunk(ship_positions, board, ship):
    """
    This function checks if a specific ship has been sunk.
    It returns True if all parts of the ship have been hit ('X'),
    otherwise False.
    """
    for position in ship_positions[ship]:
        row, col = position
        if board[row][col] != 'X':
            return False
    return True


def play_game():
    """
    This function is the main game loop where the player and
    computer take turns guessing each other's ships.
    It displays the player's board, the computer's board,
    and prompts the player to enter a guess.
    The player can enter 'exit' to quit the game at any time.
    The game continues until all the ships of either
    the player or the computer have been sunk.
    It also keeps track of the number of guesses made by the player
    and the computer.
    """

    time.sleep(1)

    # Validate name input
    name = input('Enter your name: ')
    while not validate_name(name):
        print('Invalid name. Please enter a valid name.')
        name = input('Enter your name: ')
        time.sleep(1)

    time.sleep(1)
    input('Press Enter to start the game...')

    global ships
    player_board = create_board()
    computer_board = create_board()

    print('Placing ships on the board... 🌊 🌊 🌊 🌊 🌊')
    time.sleep(1)

    player_ship_positions = place_ships(player_board)
    computer_ship_positions = place_ships(computer_board)
    player_ships_sunk = {ship: False for ship in ships}
    computer_ships_sunk = {ship: False for ship in ships}
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
            print('Quitting the game...Traitor!😈')
            return name
        time.sleep(1)

        # Check if guess is valid
        if not validate_input(guess, computer_board):
            print('Invalid input. Please enter a valid guess. 💀')
            continue

        # Check if guess has already been made
        col = guess[0].upper()
        row = int(guess[1:]) - 1
        if (row, ord(col) - ord('A')) in guessed_coords:
            print('You have already guessed that coordinate. Try again. ⛔')
            continue

        # Add current guess to guessed coordinates
        guessed_coords.add((row, ord(col) - ord('A')))

        # Process the guess
        # Now guessing on computer's board
        if computer_board[row][ord(col) - ord('A')] == 'O':
            computer_board[row][ord(col) - ord('A')] = 'X'
            print(f'{name} Hit an enemy ship! 🎯')
            # Add delay for dramatic effect
            time.sleep(1)

            # Check if a ship has been sunk
            for ship in ships:
                if is_ship_sunk(computer_ship_positions, computer_board, ship):
                    if not computer_ships_sunk[ship]:
                        print(f'{name} sunk the computer\'s {ship}! 🚩')
                        computer_ships_sunk[ship] = True
                        time.sleep(1)

        else:
            computer_board[row][ord(col) - ord('A')] = 'M'
            print(f'{name} Missed!')
            time.sleep(1)

        guesses += 1
        if all(computer_ships_sunk.values()):
            print('Victory! You sunk all the enemy\'s ships. You win! 🏆')
            print(f'Total Guesses: {guesses}')
            break
        time.sleep(1)

        # Now computer guesses on player's board
        computer_row, computer_col = computer_guess(player_board)

        # Now guessing on player's board
        if player_board[computer_row][computer_col] == 'O':
            player_board[computer_row][computer_col] = 'X'
            print('Enemy hit your ship!')

            # Add delay for dramatic effect
            time.sleep(1)

            # Check if a ship has been sunk
            for ship in ships:
                if is_ship_sunk(player_ship_positions, player_board, ship):
                    if not player_ships_sunk[ship]:
                        print(f'The computer sunk your {ship}!')
                        player_ships_sunk[ship] = True
                        time.sleep(1)

        else:
            player_board[computer_row][computer_col] = 'M'
            print('Enemy missed your ship!')
            time.sleep(1)
            print(f"Enemy: {chr(computer_col + ord('A'))}{computer_row + 1}")
            time.sleep(1)

        guesses += 1
        if all(player_ships_sunk.values()):
            print('Defeat! The computer sunk all your ships. You lose.')
            time.sleep(1)
            print(f'Total Guesses: {guesses}')
            time.sleep(1)
            break

        time.sleep(1)

    return name


# Main function to start the game
# Game instructions and setup
print("")
print("Welcome to Battleship!🚢")
time.sleep(1)
print("""
    Instructions:
1. Enter your name when prompted.
2. The game will create a 9x9 board for you and the computer.
3. Ships will be placed randomly on the board.
4. Guess the position of the enemy ships by entering a coordinate (e.g. A1)
5. The computer will tell you if your guess was a hit or a miss.
6. The computer will also guess the location of your ships.
7. The first to sink all the opponent's ships wins the game.
8. You can exit the game at any time by typing 'exit' during your turn.
9. Have fun playing Battleship! 🎮
      """)
player_name = play_game()
time.sleep(1)
print(f'Thanks for playing! Goodbye, {player_name}! 👋')
