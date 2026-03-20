from time import sleep
from rich import print
from rich.live import Live
from rich.layout import Layout
from rich.panel import Panel
from rich.align import Align
import keyboard

def narration(text, delay):
    layout = Layout(
        Panel("")
    )

    with Live(layout, refresh_per_second=32) as live:
        for i in range(1,len(text)):
            sleep(0.04)
            live.update(Panel(Align.center(text[:i], vertical="middle"), style="italic"))

    sleep(int(delay))

    print(Panel(Align.center("Press F to continue: "), style="bold"))

    while True:
        if keyboard.is_pressed("f"):
            #wait till user stops pressing f to move on
            while True:
                if not keyboard.is_pressed("f"):
                    break
            return
    