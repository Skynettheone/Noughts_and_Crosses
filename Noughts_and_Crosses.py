import sys
from datetime import datetime
from rich.console import Console
from rich.prompt import Prompt
from Game_Files.menu import display_menu
from Game_Files.board import display_reference_board
from Game_Files.player import choose_player_symbol
from Game_Files.game import play_game
from Game_Files.history import view_game_history

console = Console()

def main():
    session_stats = {'playerX_wins': 0, 'playerO_wins': 0, 'draws': 0}  # Initializing session stats
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Check if command-line arguments are provided
    if len(sys.argv) > 1:
        handle_command_line_arguments(session_stats, timestamp)
    else:
        interactive_menu(session_stats, timestamp)

#getting comand line arguments to run the game in different modes
def handle_command_line_arguments(session_stats, timestamp):
    action = sys.argv[1]

    if action == 'new_game':
        player1_name, player1_symbol, player2_name, player2_symbol = choose_player_symbol()
        display_reference_board()
        while True:
            if play_game(player1_name, player1_symbol, player2_name, player2_symbol, session_stats,
                         timestamp) == 'exit':
                break
            while True:
                play_again = Prompt.ask("Do you want to play again? (y/n)").lower()
                if play_again == 'n':
                    break
                elif play_again == 'y':
                    break
                else:
                    console.print("[bold red]Invalid choice, try again.[/bold red]")
            if play_again == 'n':
                break
    elif action == 'view_history':
        view_game_history()
    else:
        console.print("[bold red]Invalid action. Available actions: new_game, view_history[/bold red]")

#main interactive menu
def interactive_menu(session_stats, timestamp):
    while True:
        display_menu()
        choice = Prompt.ask("Enter your choice (1, 2, 3)")

        if choice == '1':
            player1_name, player1_symbol, player2_name, player2_symbol = choose_player_symbol()
            display_reference_board()
            console.print("[bold yellow]Type 'exit' to return to the main menu.[/bold yellow]")
            while True:
                if play_game(player1_name, player1_symbol, player2_name, player2_symbol, session_stats,
                             timestamp) == 'exit':
                    break
                while True:
                    play_again = Prompt.ask("Do you want to play again? (y/n)").lower()
                    if play_again == 'n':
                        console.print("[bold yellow]Returning to the main menu...[/bold yellow]\n")
                        break
                    elif play_again == 'y':
                        break
                    else:
                        console.print("[bold red]Invalid choice, try again.[/bold red]")
                if play_again == 'n':
                    break
        elif choice == '2':
            view_game_history()
        elif choice == '3':
            console.print("[bold yellow]See you soon!! Good bye...[/bold yellow]")
            break
        else:
            console.print("[bold red]Invalid choice, try again.[/bold red]")

if __name__ == "__main__":
    main()
