import sys
from time import sleep
import time

# Warna ANSI
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

def print_lyrics():
    lines = [
        (CYAN, "Think I'll miss you forever", 0.07),
        (MAGENTA, "Like the stars miss the sun in the morning sky", 0.08),
        (YELLOW, "Later's better than never", 0.08),
        (GREEN, "Even if you're gone, I'm gonna drive", 0.09),
        (RED, "I just wanted you to know", 0.09),
        (CYAN, "That baby, you're the best", 0.09),
    ]

    delays = [1.3, 1.3, 1.3, 1.5, 1.2, 3]

    for i, (color, line, char_delay) in enumerate(lines):
        for char in line:
            print(color + char + RESET, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')  

print_lyrics()
