# Battleship Game

![GIF_of_App](docs/screenshots/app.gif)

This Battleship game is a console-based implementation of the classic board game where two players (a human and a computer) take turns guessing the locations of each other's ships on a 9x9 grid. The first player to sink all of the opponent's ships wins the game.

Link to live site (https://battleship-pp3-oscar-87f5a22df472.herokuapp.com/)

## Table of Contents

1. [Features](#features)
2. [How to Play](#how-to-play)
3. [How it Works](#how-it-works)
4. [Why This Implementation](#why-this-implementation)
5. [Future Improvements](#future-improvements)
6. [Flow Chart](#flow-chart)
7. [Technologies](#technologies)
8. [Testing](#testing)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Thank You](#thank-you)

## Features

### 1. Welcome Screen

- **Description**: Upon starting the game, a welcome message and instructions are displayed.
- **Purpose**: Introduces the player to the game and provides initial instructions on how to play.

![Welcome_Screen](docs/screenshots/open_game.png)

### 2. Name Input

- **Description**: Players are prompted to enter their name.
- **Validation**: Ensures the name is non-empty, doesn't start with a number, and is a valid string.
- **Purpose**: Personalizes the game experience and ensures valid input from the player.

![Input_your_name](docs/screenshots/enter_name.png)

### 3. Game Board Setup

- **Description**: A 9x9 grid board is created for both the player and the computer.
- **Purpose**: Sets up the game environment where ships will be placed and guesses will be made.

![Board](docs/screenshots/game_has_started.png)

### 4. Ship Placement

- **Description**: Ships are randomly placed on both the player's and the computer's boards.
- **Types of Ships**: 
  - Carrier (5 cells)
  - Battleship (4 cells)
  - Cruiser (3 cells)
  - Submarine (3 cells)
  - Destroyer (2 cells)
- **Purpose**: Mimics the traditional setup phase of Battleship, ensuring a unique game experience each time.

![Ships_dictionary](docs/screenshots/ships_dict.png)

### 5. Turn-Based Gameplay

- **Player Turn**:
  - **Description**: The player enters coordinates to guess the location of the computer's ships.
  - **Validation**: Ensures the input is in the correct format (e.g., A1) and within the bounds of the board.

![Players_Turn](docs/screenshots/player_guess.png)

- **Computer Turn**:
  - **Description**: The computer randomly guesses the location of the player's ships.
- **Purpose**: Facilitates alternating turns between the player and the computer, simulating the classic Battleship gameplay.

![Computers_Turn](docs/screenshots/computer_guess.png)


### 6. Hit and Miss Feedback

- **Description**: Feedback is provided for each guess, indicating whether it was a hit or a miss.
- **Visual Representation**:
  - 'X' marks a hit.
  - 'M' marks a miss.
  - **Purpose**: Keeps the player informed of their progress and helps them strategize their next move.

![Player_hit](docs/screenshots/player_hit.png)

![Player_miss](docs/screenshots/player_miss.png)

### 7. Ship Sunk Notifications

- **Description**: Notifies the player when they have sunk one of the computer's ships and vice versa.
- **Purpose**: Adds to the excitement and progression of the game, providing a sense of achievement.

![Player_sunk_ship](docs/screenshots/player_sunk_carrier.png)

![Computer_ship_sunk](docs/screenshots/computer_sunk_crusier.png)

### 8. Game End Conditions

- **Description**: The game ends when all ships of either the player or the computer are sunk.
- **Victory Message**: Displayed when the player sinks all the computer's ships.
- **Defeat Message**: Displayed when the computer sinks all the player's ships.
- **Purpose**: Defines the winning and losing conditions, bringing the game to a natural conclusion.

![Player_win](docs/screenshots/player_win.png)

![Player_defeat](docs/screenshots/defeat.png)

### 9. Exit Functionality

- **Description**: Allows the player to exit the game at any time by typing 'exit'.
- **Purpose**: Provides an option for the player to quit the game gracefully if they choose to do so.

![Exit](docs/screenshots/exit_game.png)

### User Interaction

- **Simple Text-Based Interface**: The game runs in the console, making it accessible and easy to play without the need for a graphical user interface.
- **Prompts and Messages**: Clear prompts and messages guide the player through each stage of the game, ensuring a smooth and engaging experience.

![input](docs/screenshots/player_guess.png)

### Error Handling

- **Input Validation**: Ensures that all user inputs are valid and within the expected format, preventing errors and enhancing the robustness of the game.
- **Duplicate Guess Prevention**: Prevents players from guessing the same coordinate more than once, maintaining the integrity of the game.

![Error](docs/screenshots/invalid_guess.png)

![Invalid](docs/screenshots/invalid_name_empty.png)

![invalid_Name](docs/screenshots/invalid_name_numbers.png)

### Future Feature Considerations

- **Enhanced AI**: Developing a more strategic computer opponent.
- **Graphical User Interface**: Transitioning to a GUI-based version for improved user experience.
- **Multiplayer Mode**: Allowing two human players to compete against each other.
- **Customizable Game Settings**: Enabling players to customize board size, number of ships, and other game settings.
- **Save and Load Functionality**: Allowing players to save their game progress and resume later.

## How to Play

1. **Start the Game**: Run the script to start the game.
2. **Enter Your Name**: You will be prompted to enter your name.
3. **Game Setup**: The game will create a 9x9 board for both you and the computer and place ships randomly.
4. **Take Turns**:
    - You will guess the location of the computer's ships by entering coordinates (e.g., A1).
    - The computer will also make guesses to find your ships.
5. **Game End**: The game ends when either you or the computer has sunk all of the opponent's ships.
6. **Exit**: You can exit the game at any time by typing 'exit' during your turn.

## How it Works

### 1. Imports and Emoji Initialization

The Python code imports necessary modules like `random`, `re`, `time`, and `emoji` for functionality. It also initializes emoji support.

### 2. Global Ship Definitions

The `ships` dictionary defines the ships used in the game along with their sizes.

### 3. Board Creation Function

The `create_board()` function creates a 9x9 empty board with all cells initialized to empty spaces.

### 4. Board Printing Function

The `print_board()` function prints the game board with row numbers on the left and column letters on the top. It optionally hides ships when `hide_ships` parameter is set to True.

### 5. Ship Placement Function

The `place_ships()` function randomly places ships on the board, ensuring they don't overlap or go out of bounds.

### 6. Input Validation Functions

The `validate_input()` and `validate_name()` functions validate user input for guess and name respectively.

### 7. Computer Guess Function

The `computer_guess()` function generates a random guess for the computer player.

### 8. Ship Sunk Check Function

The `is_ship_sunk()` function checks if a specific ship has been sunk by the opponent.

### 9. Game Loop Function

The `play_game()` function is the main game loop where players take turns guessing each other's ships until all ships of one player are sunk.

### 10. Main Function

The `main()` function is the entry point of the program. It displays the welcome message, instructions, and calls `play_game()` to start the game.

### Game Initialization

- The game begins by displaying a welcome message and instructions.
- Players are prompted to enter their name, which is validated to ensure it is non-empty and does not start with a number.
- Both the player and computer boards are created as 9x9 grids.
- Ships are randomly placed on both boards using the `place_ships` function.

### Main Game Loop

- The player is asked to enter a guess (e.g., A1). The input is validated to ensure it is within the correct format and range.
- The guess is processed:
  - If it's a hit, the board is updated, and the game checks if any ship has been completely sunk.
  - If it's a miss, the board is updated accordingly.
- The computer then makes a random guess on the player's board.
- The game continues until all ships of either the player or the computer are sunk.

### Ending the Game

- The game ends when all ships of either the player or the computer are sunk.
- A victory or defeat message is displayed, and the total number of guesses is shown.

## Why This Implementation

- **Simplicity**: The console-based implementation focuses on core gameplay mechanics without the need for a graphical user interface.
- **Random Ship Placement**: Ensures a different game experience each time by placing ships randomly.
- **Turn-based Mechanics**: Mimics the classic Battleship game, providing a familiar and engaging experience.
- **Input Validation**: Ensures user inputs are correct, enhancing the robustness of the game.

## Future Improvements

1. **Enhanced AI**: Implement a more sophisticated AI for the computer player to make smarter guesses.
2. **Graphical User Interface**: Develop a GUI version of the game to make it more visually appealing and user-friendly.
3. **Multiplayer Mode**: Add a feature to allow two human players to play against each other, either locally or over the internet.
4. **Customizable Board Size and Ships**: Allow players to customize the board size and the number and size of ships.
5. **Save and Load Game**: Implement functionality to save the current game state and load it later.

## Flow Chart

![flow_chart](docs/flow/flow_chart_one.png)

## Technologies

- Python: Python is what this program is built with, and I used several standard Python libraries and one external library for the program.
  - Random: To place ships on the board at random.
  - Re: Used to validate user inputs.
  - Time: Used to delay computer response for better user experience.
  - OS: To clear the console screen
  - emoji: To display emojis in the console game.

## Testing

### 1. **Manual Testing**: 

- Tested various scenarios including all possible valid and invalid inputs to ensure that the program behaves as expected.
- Simulated full games to test all winning and losing conditions.
- Verified the random placement of ships and the random guessing mechanism of the computer player.

### 2. **Unit Testing**:

- Implemented unit tests for input validation functions to ensure they correctly handle valid and invalid inputs.

### 3. **Automated Testing**:

- Utilized automated testing frameworks like `unittest` to run a suite of tests and verify the correctness of individual components.

### 4. **User Testing**:

- Collected feedback from a small group of users to identify any usability issues and ensure the game is enjoyable.

## Deployment

1. **Setup Environment**:
    - Ensure Python is installed.
    - Install necessary dependencies using `pip install -r requirements.txt`.
2. **Run the Game**:
    - Execute the `battleship.py` script using Python: `python battleship.py`.
3. **Hosting**:
    - The game can be hosted on platforms like Heroku for wider accessibility.

## Credits

- **Code Institute**: Provided the base template and project guidelines.
- **Python Documentation**: For extensive resources and documentation.
- **Stack Overflow Community**: For troubleshooting and solutions.

## Thank You

Thank you for checking out my Battleship game! I hope you enjoy playing it as much as I enjoyed building it. If you have any feedback or suggestions for improvements, feel free to reach out.

---

Link to live site (https://battleship-pp3-oscar-87f5a22df472.herokuapp.com/)
