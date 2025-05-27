from .board import display_board, initialize_board
from .player import player_move
from .history import save_game_history, save_session_stats
from rich.console import Console

console = Console()

#check if there is a winning condition on the board
def check_win(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return True
    return False

def check_draw(board):
    return ' ' not in board

#handling the logic of the game
def play_game(player1_name, player1_symbol, player2_name, player2_symbol, session_stats, timestamp):
    board = initialize_board()
    current_player_name, current_player_symbol = player1_name, player1_symbol

    while True:
        display_board(board)
        exit_signal = player_move(current_player_name, current_player_symbol, board)
        if exit_signal == 'exit':
            return 'exit'
        if check_win(board):
            display_board(board)
            console.print(f"[bold green]{current_player_name} ({current_player_symbol}) wins![/bold green]")
            if current_player_symbol == "X":
                session_stats['playerX_wins'] += 1
            else:
                session_stats['playerO_wins'] += 1

            save_session_stats(session_stats, timestamp)  # Update and save session stats after each game
            break
        elif check_draw(board):
            display_board(board)
            console.print("[bold yellow]It's a draw![/bold yellow]")
            session_stats['draws'] += 1
            save_session_stats(session_stats, timestamp)  # Update and save session stats after each game
            break
        if current_player_symbol == player1_symbol:
            current_player_name, current_player_symbol = player2_name, player2_symbol
        else:
            current_player_name, current_player_symbol = player1_name, player1_symbol

    # Append game result to game history
    if check_win(board):
        save_game_history(current_player_name, current_player_symbol, player2_name, player2_symbol, 'win')

    elif check_draw(board):
        save_game_history(current_player_name, current_player_symbol, player2_name, player2_symbol, 'draw')