from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

choices = [f"{action.name}[{action.value}]" for action in Action]
print (choices)
