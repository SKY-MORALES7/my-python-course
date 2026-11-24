# from rich import print

# print("[bold red]Danger[/bold red]")
# print("[green]Success[/green]")
# print("[blue]Python Weekend[/blue]")

# panels:
from colorama import Fore, Back
from rich.panel import Panel
from rich import print

print(
    Panel(
        "Welcome to Python Weekend",
        title="Dashboard"
    )
)

# print(Fore.WHITE + Back.BLUE + "ERROR")

# tables
from rich.table import Table
from rich.console import Console

console = Console()

table = Table(title="Students")

table.add_column("Name")
table.add_column("Score")
table.add_column("age")

table.add_row("Kenter", "95", '10')
table.add_row("John", "88", '15')

console.print(table)

# lines segments
from rich.console import Console

console = Console()

console.rule("[bold red]Mission Start")