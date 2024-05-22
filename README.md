# Battleship Game

This Battleship game is a console-based implementation of the classic board game where two players (a human and a computer) take turns guessing the locations of each other's ships on a 9x9 grid. The first player to sink all of the opponent's ships wins the game.

## Table of Contents

1. [How to Play](#how-to-play)
2. [How it Works](#how-it-works)
3. [Why This Implementation](#why-this-implementation)
4. [Deployment](#deployment)
5. [Testing](#testing)
6. [Future Improvements](#future-improvements)

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

## Deployment

To deploy the game, follow these steps:

1. **Clone the Repository**: Clone the repository to your local machine.

    ```sh
    git clone https://github.com/yourusername/battleship-game.git
    cd battleship-game
    ```

2. **Install Python**: Ensure you have Python installed on your system. The game is compatible with Python 3.x.

3. **Run the Game**: Execute the script to start the game.

    ```sh
    python battleship.py
    ```

## Future Improvements

1. **Enhanced AI**: Implement a more sophisticated AI for the computer player to make smarter guesses.
2. **Graphical User Interface**: Develop a GUI version of the game to make it more visually appealing and user-friendly.
3. **Multiplayer Mode**: Add a feature to allow two human players to play against each other, either locally or over the internet.
4. **Customizable Board Size and Ships**: Allow players to customize the board size and the number and size of ships.
5. **Save and Load Game**: Implement functionality to save the current game state and load it later.

---

## Flow

![flow_chart](docs/flow/flow_chart_1.png)

![flow_chart_2](docs/flow/flow_chart_2.png)

## Technologies

- Python - Python is what this program is built in.
- Emojis - In requirements there is an module needed to install for the game to function, pip install emoji

## Testing

To test the game, you can follow these steps:

1. **Manual Testing**:

    - Play the game several times to ensure all game mechanics are working correctly.
    - Test different inputs, including valid and invalid guesses, and ensure the game handles them appropriately.

2. **Unit Testing**:
    - Create unit tests for individual functions such as `validate_input`, `validate_name`, `place_ships`, and `is_ship_sunk`.
    - Use a testing framework like `unittest` or `pytest` to automate these tests.

## Thank you

Thank you for playing Battleship! If you have any suggestions or feedback, feel free to contribute or open an issue on the GitHub repository.
