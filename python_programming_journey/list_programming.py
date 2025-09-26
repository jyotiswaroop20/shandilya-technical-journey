import os
from tabulate import tabulate

os.system("clear")
data = [
    ["Name", "Age", "City", "State", "Country"],
    ["Alice", 30, "New York City", "NY", "USA"],
    ["Bob", 25, "Los Angeles", "CA", "USA"],
    ["Charlie", 35, "Chicago", "IL", "USA"]
]

print(tabulate(
    data,
    headers="firstrow",
    colalign=("left", "right", "center", "center", "center"),
    showindex=True,
    tablefmt="fancy_grid"
))
print("\n")
