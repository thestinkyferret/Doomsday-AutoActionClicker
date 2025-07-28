import time
from auto_farm_base import click_in_window

def execute():
    """Execute a sequence of clicks to collect resources."""
    # Sequence of (x, y, delay_seconds) relative to game window
    click_sequence = [
        (300, 400, 0.5),  # Click resource node/button (e.g., "Collect")
        (600, 500, 0.8),  # Click confirm button (e.g., "OK" or "Collect")
        (100, 100, 0.6),  # Click back to main screen (e.g., "Back" button)
    ]

    print("Executing collect resources action")
    for x, y, delay in click_sequence:
        if click_in_window(x, y):
            print(f"Clicked at ({x}, {y}), waiting {delay}s")
            time.sleep(delay)
        else:
            print(f"Skipped click at ({x}, {y}) due to window error")