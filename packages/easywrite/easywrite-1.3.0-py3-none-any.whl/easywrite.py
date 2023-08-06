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
      ORANGE = '\033[38;5;202m'
    PINK = '\033[38;5;219m'
    BROWN = '\033[38;5;130m'  
    GRAY = '\033[38;5;244m'  
    LIME = '\033[38;5;118m'  


def easywrite(example_text, color=Color.NORMAL):
    # Map color to the corresponding color code
    color_code = color.value
    print(f"{color_code}{example_text}{Color.NORMAL.value}")
