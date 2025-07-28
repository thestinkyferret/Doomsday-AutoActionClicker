import os
import time
import random
from pynput import mouse, keyboard
import pyautogui

coords = []
recording = True

def get_action_name():
    name = input("Enter action name (no spaces, snake_case recommended): ").strip()
    if not name:
        print("Invalid name. Try again.")
        return get_action_name()
    return name

def on_press(key):
    global recording
    try:
        if key.char.lower() == 'c':
            x, y = pyautogui.position()
            coords.append((x, y))
            print(f"Recorded position {len(coords)} at ({x}, {y})")
            print("Press 'C' again to record next location or 'Q' to quit and save.")
    except AttributeError:
        # Handle special keys
        if key == keyboard.Key.esc:
            print("ESC pressed, exiting without saving.")
            recording = False
            return False

    # Stop if user presses 'q'
    if key == keyboard.KeyCode.from_char('q'):
        print("Q pressed, finishing recording.")
        recording = False
        return False

def create_action_file(action_name, coords):
    actions_dir = "actions"
    os.makedirs(actions_dir, exist_ok=True)

    filename = os.path.join(actions_dir, f"action_{action_name}.py")
    if os.path.exists(filename):
        print(f"Warning: {filename} already exists and will be overwritten.")

    with open(filename, "w") as f:
        f.write("import time\n")
        f.write("import random\n")
        f.write("from auto_farm_base import click_in_window\n\n")
        f.write("def execute():\n")
        f.write(f"    print('Executing action_{action_name}')\n\n")
        f.write("    click_sequence = [\n")
        for x, y in coords:
            f.write(f"        ({x}, {y}, 1.0),  # Adjust delay if needed\n")
        f.write("    ]\n\n")
        f.write("    for x, y, delay in click_sequence:\n")
        f.write("        if click_in_window(x, y):\n")
        f.write("            print(f\"Clicked at ({x}, {y}), waiting {delay:.2f}s\")\n")
        f.write("            time.sleep(random.uniform(delay * 0.8, delay * 1.2))\n")
        f.write("        else:\n")
        f.write("            print(f\"Skipped click at ({x}, {y}) due to window error\")\n")

    print(f"Action script created at: {filename}")

def main():
    print("=== Action Creator for AutoClickAction Framework ===")
    print("Instructions:")
    print(" - Move your mouse to the desired position and press 'C' to record the location.")
    print(" - Press 'Q' when you are done to save and exit.")
    print(" - Press ESC at any time to cancel without saving.\n")

    action_name = get_action_name()

    global coords, recording
    coords = []
    recording = True

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    if coords:
        create_action_file(action_name, coords)
    else:
        print("No positions recorded. Exiting.")

if __name__ == "__main__":
    main()
