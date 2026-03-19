from functions.sprites import print_sprite
from rich.console import Console
from rich.table import Table
from time import sleep

# TODO: implement sprites
def dialogue(character, sprite, text, answers):
    print_sprite(character, sprite)
    table = Table()
    
    table.add_column("❤", justify="center", style="cyan", no_wrap=True)
    table.add_column(text, style="magenta")

    for letter, answer in answers.items():
        table.add_row(f"{letter.upper()})", answer["text"])

    console = Console()
    console.print(table)

    letter = input("Enter your answer: ")

    while letter not in answers.keys():
        print("Try Again!")
        letter = input("Enter your answer: ")

    return answers[letter]