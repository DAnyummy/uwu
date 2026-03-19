from functions.sprites import print_sprite
import os
from time import sleep
import sys
from rich.console import Console

console = Console()

def narration(text, delay):
    for n in text:
        console.print(n, style="italic bold underline bright_white", end="")
        sleep(0.05)

    sleep(int(delay))

narration('mfhaowifhioasfnohfiwe hsafioh fioha', 2)

'''
for e in b:
    print_sprite('tsun', e)
    a = input('a: ')
    os.system('cls')

for e in b:
    print_sprite('separi', e)
    a = input('a: ')
    os.system('cls')

for e in b:
    print_sprite('uwa', e)
    a = input('a: ')
    os.system('cls')
'''