# easywrite.py
import sys
from enum import Enum

class Color(Enum):
    NORMAL = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    ORANGE = '\033[91m'
    PINK = '\033[95m'
    BROWN = '\033[33m'
    GRAY = '\033[37m'
    LIME = '\033[92m'

def easywrite(example_text, color=Color.NORMAL):
    # Map color to the corresponding color code
    color_code = color.value
    print(f"{color_code}{example_text}{Color.NORMAL.value}")
