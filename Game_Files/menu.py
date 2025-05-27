from rich.console import Console
from rich.table import Table

console = Console()

def display_menu():
    console.print("\n[bold cyan]Welcome to Noughts and Crosses[/bold cyan]")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Option", justify="center")
    table.add_column("Description", justify="left")
    table.add_row("1", "Start a new game")
    table.add_row("2", "View past game history")
    table.add_row("3", "Exit")
    console.print(table)