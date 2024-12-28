![image](https://github.com/user-attachments/assets/006739b9-4406-4039-8b29-0aa0675d60a1)



# Python Tic-Tac-Toe Game

A command-line implementation of the classic Tic-Tac-Toe game with a clean, modular structure.

## Project Structure

```
├── board.py          # Board class and game state management
├── display.py        # Display functions for the game board
├── game.py          # Main game loop and logic
├── input_handler.py  # User input handling and validation
└── README.md        # Project documentation
```

## Features

- Clean, modular code structure
- Input validation
- Visual board display
- Two-player gameplay
- Win and tie detection

## How to Play

1. Run the game:
```bash
python game.py
```

2. Players take turns entering positions (0-8) to place their marks:
```
Positions:
 0 | 1 | 2 
-----------
 3 | 4 | 5 
-----------
 6 | 7 | 8 
```

3. First player to get three in a row (horizontally, vertically, or diagonally) wins!

## Game Controls

- Enter numbers 0-8 to place your mark
- Player 1 uses 'X'
- Player 2 uses 'O'
