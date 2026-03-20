from functions.sprites import get_sprite
from rich import print
from rich.layout import Layout
from rich.panel import Panel
from rich.live import Live
from rich.align import Align
from rich.console import Group
from time import sleep
import keyboard

def dialogue(character, sprite, text, answers):
    # fetch character sprite, return in printable text
    sprite = get_sprite(character, sprite)

    dialogue = Panel(Align.center(text, vertical="middle"), style="rgb(255,105,180)")

    answer_panel = Layout(name="answer_wrapper")

    answer_panel.split_row()

    for letter, answer in answers.items():
        answer_panel.add_split(
            Layout(
                Panel(
                        Align.center(f"{answer["text"]}", vertical="middle"), 
                        title=f"{letter.upper()}:",
                        style="rgb(255,182,193)"
                    )
                )
        )

    layout = Layout()
    layout.split_column(
        Layout(Panel(Align.center(sprite), title=character, style="rgb(255,20,147)"), name="character_sprite", ratio=2),
        Layout(name="dialogue_wrapper")
    )

    layout["dialogue_wrapper"].split_column(
        Layout(dialogue, name="dialogue"),
        Layout(answer_panel, name="answers")
    )

    print(layout)
    
    while True: 
        for letter in answers.keys():
            if keyboard.is_pressed(letter):
                while True:
                    if not keyboard.is_pressed(letter):
                        break
                return answers[letter]