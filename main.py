import pyautogui
import random
import time
import importlib
import os
import keyboard

# Configuration
pyautogui.FAILSAFE = True  # Move mouse to top-left to stop script
pyautogui.PAUSE = 0.5      # Base delay for each pyautogui action
MIN_DELAY = 1              # Minimum delay between actions (seconds)
MAX_DELAY = 5              # Maximum delay between actions (seconds)

# Directory for action scripts
ACTION_DIR = "actions"

def click_in_window(x, y):
    """Click at absolute screen coordinates (no window logic)."""
    try:
        pyautogui.click(x, y)
        return True
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
    print("Starting script. Move mouse to top-left or press ESC to stop.")
    actions = load_action_modules()

    if not actions:
        print("No valid action modules loaded. Exiting.")
        return

    while True:
        if keyboard.is_pressed("esc"):
            print("ESC pressed. Stopping script.")
            break

        random.shuffle(actions)
        for action in actions:
            if keyboard.is_pressed("esc"):
                print("ESC pressed. Stopping script.")
                return
            try:
                action()
                time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))
            except Exception as e:
                print(f"Error executing action: {e}")

        time.sleep(random.uniform(10, 30))  # Delay between cycles

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Script stopped by user.")
