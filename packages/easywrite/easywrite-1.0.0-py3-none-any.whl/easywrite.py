# easywrite.py

from enum import Enum

class Color(Enum):
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

def easy_write_command(example_text, color=Color.RESET):
    # Map color to the corresponding color code
    color_code = color.value
    print(f"{color_code}{example_text}{Color.RESET.value}")
