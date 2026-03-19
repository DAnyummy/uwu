from rich.console import Console
from rich.table import Table
from rich_pixels import Pixels
from PIL import Image
from pathlib import Path

def print_sprite(name, ver):
    console = Console()
    img = Image.open(Path(__file__).parent / "images" / name / f"{name}_{ver}.png") #Förkortade from previous if-statement for each one
    new_height = 60  #height by pixels
    new_width = int(new_height * (img.width / img.height))
    img = img.resize((new_width, new_height))
    console.print(Pixels.from_image(img))


