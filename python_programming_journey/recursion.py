import os

os.system("clear")

def sum_natural(n):
    if n == 1:                  # Base case
        return 1
    else:                       # Recursive case
        return n + sum_natural(n - 1)
    

# ---- User Input ----0
n = int(input("Enter a number: "))
# ---- Function Call & Output ----
print(f"Sum of first", {n}, "natural numbers is:", sum_natural(n))
