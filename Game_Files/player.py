from rich.console import Console
from rich.prompt import Prompt

console = Console()

#handling all the player moves
def player_move(player_name, player_symbol, board):
    while True:
        move = Prompt.ask(
            f"{player_name} ({player_symbol}), enter your move (1-9)").lower()
        if move == 'exit':
            return 'exit'
        try:
            move = int(move) - 1
            if board[move] == ' ':
                board[move] = player_symbol
                break
            else:
                console.print("[bold red]Invalid move, the cell is already occupied. Try again.[/bold red]")
        except (ValueError, IndexError):
            console.print("[bold red]Invalid input, enter a number between 1 and 9 or exit.[/bold red]")
    return None

#let player to choose their symbol
def choose_player_symbol():
    while True:
        symbol = Prompt.ask("Player 1, do you want to be [bold cyan]X[/bold cyan] or [bold cyan]O[/bold cyan]?").upper()
        if symbol in ['X', 'O']:
            player1_name = Prompt.ask(f"Enter the name for Player {symbol}")
            player2_symbol = 'O' if symbol == 'X' else 'X'
            player2_name = Prompt.ask(f"Enter the name for Player {player2_symbol}")
            return player1_name, symbol, player2_name, player2_symbol
        else:
            console.print("[bold red]Invalid choice, please choose either X or O.[/bold red]")