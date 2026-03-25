from functions.dialogue import dialogue
from functions.narration import narration
from functions.ending import ending
from functions.quit import quit
from rich.console import Console
import json
import os

console = Console()

def get_endings(storyline_array):
    return [
        index
        for index, node in storyline_array.items()
        if node["type"] == "ending"
    ]

with open('storyline.json', 'r', encoding="utf-8") as file:
    storyline = json.load(file)

# array of which endings we have completed
endings_completed = []
total_endings = get_endings(storyline)

# TODO: implement parser function, parses JSON file and runs game
def parser():
    index_at = 1
    while True:
        os.system("cls")

        current = storyline[f"{index_at}"]

        if current["type"] == "table":
            answer = dialogue(current["character"], current["sprite"], current["text"], current["answers"])
            index_at = int(answer["leads_to"])
        elif current["type"] == "narration":
            narration(current["text"], int(current["delay"]))
            index_at = int(current["leads_to"])
        elif current["type"] == "ending":
            endings_completed.append(str(index_at))

            result = ending(current["ending_name"])

            if result == "quit":
                os.system("cls")

                return quit(endings_completed, total_endings)
            elif result == "restart":
                index_at = 1

parser()