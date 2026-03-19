from time import sleep
from rich.console import Console

def typing(text):
    console = Console()
    for n in text:
        console.print(n, style="italic bold", end="")
        sleep(0.05)