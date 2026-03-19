from functions.dialogue import dialogue
from functions.narration import narration
import json
import os

# TODO: implement parser function, parses JSON file and runs game
def parser():
    with open('storyline.json', 'r') as file:
        gamefile = json.load(file)

        index_at = 1
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            current = gamefile[f"{index_at}"]

            if current["type"] == "table":
                answer = dialogue(current["character"], current["sprite"], current["text"], current["answers"])
                index_at = int(answer["leads_to"])
            elif current["type"] == "narration":
                narration(current["text"], int(current["delay"]))
                index_at = int(current["leads_to"])

parser()