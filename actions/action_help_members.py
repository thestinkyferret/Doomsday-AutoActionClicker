import time
import random
from main import click_in_window

def execute():
    print('Executing action_help_members')

    click_sequence = [
        (1881, 553, 1.0),  # Adjust delay if needed
    ]

    for x, y, delay in click_sequence:
        if click_in_window(x, y):
            print(f"Clicked at ({x}, {y}), waiting {delay:.2f}s")
            time.sleep(random.uniform(delay * 0.8, delay * 1.2))
        else:
            print(f"Skipped click at ({x}, {y}) due to window error")
