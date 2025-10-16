import sys;
import time;

'''
TODO: 
- figure out a way to have differnt line_delay for every line without breaking formatting
'''

def lyrics():
    lines = [
        ('i know that this could hurt me bad', 0.06, 0.7),  #illegal formatting
        ('i know that this could feel like that', 0.06, 0.2),
        ('but i just can\'t stop', 0.06, 2),
        ('let my defences drop', 0.06, 2),
        ('i know that i was born to kill', 0.06, 0.7),
        ('any angel on my windowsill', 0.06, 0.2),
        ('but it\'s so dark inside', 0.06, 2),
        ('i throw the windows wide', 0.06, 2),

        # pre-chorus
        ('i know,', 0.06, 1.5),
        ('la-la-la-la-la-la-la-la-la', 0.07, 0.5)
        ('i know,', 0.06, 1.5),
        ('la-la-la-la-la-la-la-la', 0.07, 0.08)
        ('still, i don\'t let go', 0.06, 2),
        ('and fields of flowers grow', 0.06),

        # chorus
        ('oh, it feels like', 0.09, 1),
        ('i\'m fallin\' in love', 0.06, 1),
        ('maybe for the first time', 0.07, 1),
        ('baby it\'s my mind you blow', 0.12, 1),
        ('it feels like', 0.09, 1),
        ('i\'m fallin\' in love', 0.06, 1),
        ('you\'re throwin\' me a lifeline', 0.07, 1),
        ('and this is for a lifetime, i know', 0.12, 1),
    ]

    # loops through each line, then each character in the current line
    for i, (line, char_delay, line_delay) in enumerate(lines):
        for char in line:
            print(char, end="", flush=True)         #
            time.sleep(char_delay)
        print()
        time.sleep(line_delay)

lyrics()