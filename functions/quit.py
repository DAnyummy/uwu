from rich import print
from rich.layout import Layout
from rich.panel import Panel
from rich.align import Align
from time import sleep

def quit(endings_reached, total_endings):
    bye = Panel(Align.center(f"Thank you for playing our game!", vertical="middle"), style="bold", padding=(0,2))

    endings_reached = list(set(endings_reached))
    endings_text = Panel(
        Align.center(
            f"You've reached [bold]{len(endings_reached)}[/bold] out of [bold]{len(total_endings)}[/bold] endings!", vertical="middle"
        ),
        padding=(0,2)
    )

    layout = Layout()
    layout.split_column(
        Layout(bye, name="dialogue", ratio=2),
        Layout(endings_text, name="answers")
    )

    print(layout)