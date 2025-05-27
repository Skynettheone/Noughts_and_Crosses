import os
from rich.console import Console

console = Console()
#sace the results in a history file
def save_game_history(current_player_name, current_player_symbol, player2_name, player2_symbol, result):

    directory = 'Game_History'
    os.makedirs(directory, exist_ok=True)  # Create the directory if it doesn't exist
    filename_txt = os.path.join(directory, 'game_history.txt')
    filename_html = os.path.join(directory, 'game_history.html')

    #append to a text file
    with open(filename_txt, 'a') as file:
        if result == 'win':
            file.write(f"{current_player_name} ({current_player_symbol}) vs {player2_name} ({player2_symbol}): {result} for {current_player_name} ({current_player_symbol})\n")
        elif result == 'draw':
            file.write(f"{current_player_name} ({current_player_symbol}) vs {player2_name} ({player2_symbol}): {result}\n")

    #append to a html file
    with open(filename_html, 'a') as file:
        if result == 'win':
            file.write(f"<p>{current_player_name} ({current_player_symbol}) vs {player2_name} ({player2_symbol}): {result} for {current_player_name} ({current_player_symbol})</p>\n")
        elif result == 'draw':
            file.write(f"<p>{current_player_name} ({current_player_symbol}) vs {player2_name} ({player2_symbol}): {result}</p>\n")

#saving game stats at the end of the session
def save_session_stats(session_stats, timestamp):
    directory = 'Game_Stats'
    os.makedirs(directory, exist_ok=True)  # Create the directory if it doesn't exist
    filename_txt = os.path.join(directory, f'session_stats_{timestamp}.txt')
    filename_html = os.path.join(directory, f'session_stats_{timestamp}.html')\

    with open(filename_txt, 'w') as file:
        file.write(f"Total wins by Player X: {session_stats['playerX_wins']}\n")
        file.write(f"Total wins by Player O: {session_stats['playerO_wins']}\n")
        file.write(f"Total draws: {session_stats['draws']}\n")

    with open(filename_html, 'w') as file:
        file.write(f"<p>Total wins by Player X: {session_stats['playerX_wins']}</p>\n")
        file.write(f"<p>Total wins by Player O: {session_stats['playerO_wins']}</p>\n")
        file.write(f"<p>Total draws: {session_stats['draws']}</p>\n")

#display the game history from the text file
def view_game_history():
    directory = 'Game_History'
    filename = os.path.join(directory, 'game_history.txt')

    if os.path.exists(filename):
        with open(filename, 'r') as file:
            console.print("\n[bold green]Game History:[/bold green]\n")
            console.print(file.read())
    else:
        console.print("[bold red]No game history found.[/bold red]")
