from rich import print
from rich.layout import Layout
from rich.panel import Panel
from rich.align import Align
import keyboard

def ending(ending_name):
    dialogue = Panel(Align.center(f"You reached the {ending_name}!", vertical="middle"), padding=(0,2))

    answer_panel = Layout(name="answer_wrapper")

    answer_panel.split_row(
        Panel(
                Align.center("Play again and unlock other endings", vertical="middle"), 
                title="R",
                style="rgb(255,182,193)",
            ),
        Panel(
                Align.center("Quit", vertical="middle"), 
                title="Q",
                style="rgb(255,182,193)"
            )
        ),

    layout = Layout()
    layout.split_column(
        Layout(dialogue, name="dialogue", ratio=2),
        Layout(answer_panel, name="answers")
    )

    print(layout)
    
    while True: 
        if keyboard.is_pressed("r"):
            while True:
                if not keyboard.is_pressed("r"):
                    return "restart"
        elif keyboard.is_pressed("q"):
            while True:
                if not keyboard.is_pressed("q"):
                    return "quit"