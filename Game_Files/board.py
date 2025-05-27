from rich.console import Console

console = Console()

def initialize_board():
    board = []
    for _ in range(9):
        board.append(' ')
    return board

#Display the game board
def display_board(board):
    console.print(f"\n {board[0]} | {board[1]} | {board[2]}")
    console.print("---+---+---")
    console.print(f" {board[3]} | {board[4]} | {board[5]}")
    console.print("---+---+---")
    console.print(f" {board[6]} | {board[7]} | {board[8]}\n")

#Display the reference board showing positions 1-9
def display_reference_board():
    console.print("[bold yellow]Player's view:[/bold yellow]")
    reference_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    console.print(f"\n {reference_board[0]} | {reference_board[1]} | {reference_board[2]}")
    console.print("---+---+---")
    console.print(f" {reference_board[3]} | {reference_board[4]} | {reference_board[5]}")
    console.print("---+---+---")
    console.print(f" {reference_board[6]} | {reference_board[7]} | {reference_board[8]}\n")