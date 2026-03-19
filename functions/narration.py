from time import sleep
from rich.console import Console

def narration(text, delay):
    print("")

    console = Console()
    for n in text:
        console.print(n, style="italic bold", end="")
        sleep(0.05)

    sleep(int(delay))

    print("")

    proceed = input("Press F to proceed: ")
    while proceed.lower() != "f":
        print("Try Again!")
        proceed = input("Press F to proceed: ")
    
    return 