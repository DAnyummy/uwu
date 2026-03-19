from rich.console import Console
from rich_pixels import Pixels
from PIL import Image

console = Console()

# Open image with Pillow
img = Image.open("kaicho_chan.png")

new_width = 40  # adjust for desired size
aspect_ratio = img.height / img.width
new_height = int(new_width * aspect_ratio)
img = img.resize((new_width, new_height))

# Create Pixels object from resized image
pixels = Pixels.from_image(img)

# Print in terminal
console.print(pixels)
