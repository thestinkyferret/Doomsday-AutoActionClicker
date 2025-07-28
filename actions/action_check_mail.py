import time
import random
from main import click_in_window

def execute():
    print('Executing action_check_mail')

    click_sequence = [
        (1877, 625, 1.0),  # Adjust delay if needed
        (771, 715, 1.0),  # Adjust delay if needed
        (1085, 661, 1.0),  # Adjust delay if needed
        (1082, 75, 1.0),  # Adjust delay if needed
        (736, 717, 1.0),  # Adjust delay if needed
        (1074, 668, 1.0),  # Adjust delay if needed
        (1223, 71, 1.0),  # Adjust delay if needed
        (718, 712, 1.0),  # Adjust delay if needed
        (1079, 666, 1.0),  # Adjust delay if needed
        (1869, 77, 1.0),  # Adjust delay if needed
    ]

    for x, y, delay in click_sequence:
        if click_in_window(x, y):
            print(f"Clicked at ({x}, {y}), waiting {delay:.2f}s")
            time.sleep(random.uniform(delay * 0.8, delay * 1.2))
        else:
            print(f"Skipped click at ({x}, {y}) due to window error")
