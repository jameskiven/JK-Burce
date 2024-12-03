import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("i'll imagine", 0.07),
        ("we fell inlove", 0.08),
        ("i'll nap under moonlight", 0.05),
        ("skies with you", 0.06),
        ("i think i'll", 0.06),
        ("picture us, you with the waves", 0.07),
        ("the ocean's colors", 0.07),
        ("on your face", 0.07),
        ("i'll leave my heart with your air", 0.10),
        ("so let me fly with you", 0.13),
        ("will you be forever with me?", 0.10)
    ]

    delays = [0.3, 0.4, 0.5, 0.5, 0.5, 0.5, 0.7, 0.5, 0.13, 0.14, 0.5]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()

