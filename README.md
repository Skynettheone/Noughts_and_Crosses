# Noughts and Crosses (Tic-Tac-Toe)

![Tic Tac Toe Winning Example](https://static.wikia.nocookie.net/board-games-galore/images/4/47/Tictactoe-winning-vector-639732.jpg/revision/latest?cb=20160711013756)

A console-based Python 3.x game that simulates the classic two-player game "Noughts and Crosses" (Tic-Tac-Toe). This program allows two human players to play interactively, keeps track of their game history, and stores detailed game statistics for each session.

---

## Features

- **Menu System**:  
  - Start a new game  
  - View past game play history  
  - Exit the game

- **Game Play**:  
  - Two players take turns placing their symbols ("O" or "X") on a 3x3 grid.
  - The first player can choose their symbol; the second player gets the other.
  - The game ends when a player gets three in a row (horizontally, vertically, or diagonally), or the board is full (draw).
  - Players can exit the game at any time.
  - Multiple rounds can be played in a single session, with session stats tracked.

- **Game History & Stats**:  
  - Game history is saved in the `Game_History` directory.
  - Each session's statistics are saved in the `Game_Stats` directory, uniquely identified by date and time.
  - Both history and stats are saved in `.txt` and `.html` formats for easy viewing.
  - Session stats include total wins by each player and total draws.

- **Enhanced Console Output**:  
  - Uses the `rich` library for styled, interactive, and user-friendly console output.

- **Error Handling**:  
  - Handles invalid inputs and unexpected errors gracefully.
  - Prompts users to retry on invalid moves without terminating the game.

---

## Directory Structure

```
Noughts_and_Crosses/
│
├── Game_Files/         # Contains game logic modules (menu, board, player, game, history)
├── Game_History/       # Stores all past game wins and draws (TXT & HTML)
├── Game_Stats/         # Stores per-session statistics (TXT & HTML)
└── Noughts_and_Crosses.py  # Main entry point
```

---

## Installation

1. **Clone the repository**  
   ```bash
   git clone <your-repo-url>
   cd Noughts_and_Crosses
   ```

2. **Install required libraries**  
   The only external dependency is `rich` for enhanced console output.
   ```bash
   pip install rich
   ```

---

## How to Play

1. **Run the game**  
   ```bash
   python Noughts_and_Crosses.py
   ```

2. **Menu Options**  
   - **Start a New Game**:  
     - Choose your symbol ('X' or 'O').
     - Take turns entering your move (1-9) corresponding to board positions.
     - Type `exit` at any time to return to the main menu.
   - **View Game History**:  
     - View all past game results and session statistics.
   - **Exit**:  
     - Quit the game.

3. **Game Controls**  
   - Enter a number (1-9) to place your symbol.
   - Type `exit` to leave the current game and return to the menu.

---

## Board Reference

The board positions are numbered as follows for easy reference:

```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

---

## File Operations

- The program ensures that `Game_History` and `Game_Stats` directories exist.
- Each session's history and stats are appended to their respective files, preserving past data.
- Session files are named with the date and time for uniqueness.

---

## Code Structure & Modularity

- **menu**: Displays the main menu.
- **board**: Handles board initialization and display.
- **player**: Manages player symbol selection and moves.
- **game**: Contains the main game loop, win/draw checks, and gameplay logic.
- **history**: Handles saving and viewing game history and session stats.

This modular approach ensures:
- **Separation of Concerns**: Each module handles a specific part of the game.
- **Reusability**: Functions can be reused across the program.
- **Scalability**: New features can be added easily.

---

## Optional Feature: HTML Game History

- Game results can also be saved and viewed in HTML format for a more visual experience in your web browser.

---

## Example Output

Styled output using the `rich` library:

```python
console.print("[bold green]Congratulations! Player X wins![/bold green]")
```

Prompts and tables are also styled for clarity and user experience.

---

## Error Handling

- Invalid moves (non-integer or out of range) prompt the player to try again.
- All errors are handled gracefully to ensure a smooth gaming experience.

---

## License

This project is for educational purposes.

---

## Acknowledgements

- [Rich library documentation](https://rich.readthedocs.io/en/stable/) 
