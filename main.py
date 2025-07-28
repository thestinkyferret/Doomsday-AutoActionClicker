import pyautogui
import random
import time
import importlib
import os
import pygetwindow as gw

# Configuration
pyautogui.FAILSAFE = True  # Move mouse to top-left to stop script
pyautogui.PAUSE = 0.5  # Base delay for each pyautogui action
MIN_DELAY = 1  # Minimum delay between actions (seconds)
MAX_DELAY = 5  # Maximum delay between actions (seconds)
WINDOW_TITLE = "Doomsday: Last Survivors"  # Adjust to match your game's window title

# Directory for action scripts
ACTION_DIR = "actions"

def get_game_window():
    """Find and return the game window, or None if not found."""
    try:
        windows = gw.getWindowsWithTitle(WINDOW_TITLE)
        if windows:
            window = windows[0]
            window.activate()  # Focus the window
            return window
        print(f"Error: Window '{WINDOW_TITLE}' not found.")
        return None
    except Exception as e:
        print(f"Error finding window: {e}")
        return None

def click_in_window(x, y):
    """Click at coordinates relative to the game window's top-left corner."""
    window = get_game_window()
    if not window:
        return False
    try:
        # Adjust coordinates to window's client area
        abs_x = window.left + x
        abs_y = window.top + y
        # Check if coordinates are within window bounds
        if (window.left <= abs_x <= window.right and
                window.top <= abs_y <= window.bottom):
            pyautogui.click(abs_x, abs_y)
            return True
        else:
            print(f"Warning: Click at ({x}, {y}) is outside window bounds.")
            return False
    except Exception as e:
        print(f"Error clicking at ({x}, {y}): {e}")
        return False

def load_action_modules():
    """Dynamically load action modules from the /actions directory."""
    actions = []
    if not os.path.exists(ACTION_DIR):
        print(f"Error: Directory '{ACTION_DIR}' not found.")
        return actions

    for filename in os.listdir(ACTION_DIR):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]  # Remove .py extension
            try:
                module = importlib.import_module(f"{ACTION_DIR}.{module_name}")
                if hasattr(module, "execute"):
                    actions.append(module.execute)
                else:
                    print(f"Warning: Module {module_name} has no execute function.")
            except ImportError as e:
                print(f"Error: Could not load module {module_name}: {e}")
    return actions

def main():
    print("Starting auto-farm script. Move mouse to top-left to stop.")
    actions = load_action_modules()

    if not actions:
        print("No valid action modules loaded. Exiting.")
        return

    while True:
        # Shuffle actions for random order
        random.shuffle(actions)
        for action in actions:
            try:
                action()  # Execute the action
                # Random delay to mimic human behavior
                time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))
            except Exception as e:
                print(f"Error executing action: {e}")
        # Longer delay between full cycles
        time.sleep(random.uniform(10, 30))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Script stopped by user.")