import random # built-in
import math # standard library
import os # standard library
import datetime # standard library
import matplotlib.pyplot as plt
from rich import print
from rich.console import Console

# Initialize rich console
console = Console()

# Generate a random number
number = random.randint(0, 10)
print(f"[bold magenta]Your random number is:[/bold magenta] {number}")

# Create a list of random numbers
random_numbers = [random.randint(0, 10) for _ in range(10)]
print("[bold cyan]Here are 10 random numbers:[/bold cyan]", random_numbers)

# Visualize the random numbers using matplotlib
plt.figure(figsize=(8, 4))
plt.plot(random_numbers, marker='o', linestyle='-', color='blue')
plt.title("Random Numbers Visualization")
plt.xlabel("Index")
plt.ylabel("Random Value")
plt.grid(True)
plt.tight_layout()
plt.show()

# Closing message
console.rule("[bold green]Complete![/bold green]")
