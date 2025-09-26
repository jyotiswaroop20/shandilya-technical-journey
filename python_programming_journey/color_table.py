from tabulate import tabulate
from colorama import Fore, Style, init

init(autoreset=True)

header = [Fore.YELLOW + "Name", Fore.YELLOW + "Age", Fore.YELLOW + "City"]
data = [
    [Fore.RED + "Alice", Fore.GREEN + "30", Fore.BLUE + "New York"],
    [Fore.RED + "Bob", Fore.GREEN + "25", Fore.BLUE + "Los Angeles"],
    [Fore.RED + "Charlie", Fore.GREEN + "35", Fore.BLUE + "Chicago"]
]

print(tabulate([header] + data, headers="firstrow", tablefmt="fancy_grid"))
