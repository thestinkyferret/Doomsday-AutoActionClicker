# AutoClickAction Framework

## Overview

The `AutoClickAction Framework` is a Python-based automation tool designed to perform repetitive UI interactions (mouse clicks) within a specified application window. It locks onto the target window, uses coordinates relative to the window’s top-left corner, and executes modular action scripts in a randomized order with variable delays to mimic human behavior. The framework is ideal for automating repetitive tasks in applications with consistent UI layouts, such as games or software with clickable interfaces.

## Features

- **Window Locking**: Automatically detects and focuses the target application window, ensuring clicks are confined to its bounds, even if the window moves.
- **Relative Coordinates**: Uses coordinates relative to the window’s top-left corner for consistent click placement across different screen positions.
- **Modular Actions**: Supports user-defined action scripts in a dedicated `/actions` directory, allowing easy addition of new tasks.
- **Randomized Execution**: Shuffles action order and introduces random delays to reduce detectability by anti-automation systems.
- **Error Handling**: Skips invalid clicks (e.g., outside window bounds) and provides debugging output.
- **Safety Features**: Includes a failsafe (move mouse to top-left corner to stop) and graceful error recovery.

## Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **Libraries**:
  - `pyautogui`: For mouse click automation. Install with `pip install pyautogui`.
  - `pygetwindow`: For window detection and focus (Windows-focused; limited on macOS/Linux). Install with `pip install pygetwindow`.
- **Target Application**: The application must run in a window with a consistent title and UI layout. Use windowed mode for best results.

## Installation

1. **Clone or Create the Project Directory**:
   - Create a directory for the framework (e.g., `AutoClickAction_Framework`).
   - Place the main script (`auto_farm_base.py`) in the root directory.
2. **Install Dependencies**:

   ```bash
   pip install pyautogui pygetwindow
   ```
3. **Create the Actions Directory**:
   - Create a subdirectory named `actions` in the project root.
   - Place action scripts (e.g., `action_example.py`) in the `actions` folder.
4. **Verify Window Title**:
   - Run the target application and note its window title (visible in the title bar).
   - Alternatively, use the following Python code to list open window titles:

     ```python
     import pygetwindow as gw
     print(gw.getAllTitles())
     ```

## Usage

1. **Configure the Main Script**:
   - Open `auto_farm_base.py` and update the `WINDOW_TITLE` variable to match the target application’s window title (e.g., `"My Application"`).
   - Adjust `MIN_DELAY` and `MAX_DELAY` for random delays between actions (in seconds).
2. **Create Action Scripts**:
   - In the `actions` directory, create Python scripts (e.g., `action_example.py`) with an `execute()` function.
   - Define a `click_sequence` list of `(x, y, delay)` tuples, where:
     - `x, y`: Coordinates relative to the window’s top-left corner.
     - `delay`: Time to wait after the click (in seconds).
   - Example action script:

     ```python
     import time
     from auto_farm_base import click_in_window
     
     def execute():
         click_sequence = [
             (300, 400, 0.5),  # Click button 1, wait 0.5s
             (600, 500, 0.8),  # Click button 2, wait 0.8s
         ]
         print("Executing example action")
         for x, y, delay in click_sequence:
             if click_in_window(x, y):
                 print(f"Clicked at ({x}, {y}), waiting {delay}s")
                 time.sleep(delay)
             else:
                 print(f"Skipped click at ({x}, {y}) due to window error")
     ```
3. **Find Coordinates**:
   - Run the target application in windowed mode.
   - Use `pyautogui.displayMousePosition()` to find coordinates relative to the window’s top-left corner:

     ```python
     import pyautogui
     pyautogui.displayMousePosition()
     ```
   - Update action scripts with these coordinates.
4. **Run the Framework**:
   - Ensure the target application is open.
   - Run the main script:

     ```bash
     python main.py
     ```
   - The framework loads all `.py` files in `/actions` (excluding `__init__.py`), executes their `execute()` functions in random order, and applies random delays.
5. **Stop the Script**:
   - Move the mouse to the top-left corner of the screen (PyAutoGUI failsafe).
   - Or press `Ctrl+C` in the terminal.

## Directory Structure

```
AutoClickAction_Framework/
├── main.py      # Main script
├── actions/               # Directory for action scripts
│   ├── action_collect_resources.py  # Example action script
│   ├── action_task1.py    # Additional action scripts
│   └── ...
```

## Customization

- **Add New Actions**:
  - Create new `.py` files in `/actions` with an `execute()` function following the structure above.
  - The framework automatically loads all valid action scripts.
- **Adjust Delays**:
  - Modify `MIN_DELAY` and `MAX_DELAY` in `auto_farm_base.py` for action-to-action delays.
  - Use per-click delays in action scripts for task-specific timing.
- **Enhance Obfuscation**:
  - Add random mouse movements or variable per-click delays in action scripts to further mimic human behavior.
  - Example:

    ```python
    import random
    time.sleep(random.uniform(delay * 0.8, delay * 1.2))
    ```
- **Error Handling**:
  - The framework skips clicks outside the window and logs errors for debugging.
  - Add custom checks (e.g., pixel color validation) in action scripts for robustness.

## Limitations

- **Platform**: `pygetwindow` works best on Windows. On macOS/Linux, window focus and detection may be unreliable; consider using an emulator for consistency.
- **Coordinate Accuracy**: Coordinates must match the application’s window resolution. Resizing the window may shift UI elements, requiring coordinate updates.
- **Detectability**: Automation may be detected by applications with anti-cheat or monitoring systems. Use with caution and test in a safe environment.
- **Application-Specific**: The framework assumes a consistent UI. Dynamic or frequently updated interfaces may require frequent coordinate adjustments.

## Risks

- **Terms of Service**: Automating UI interactions may violate the target application’s terms, risking account bans or restrictions.
- **Security**: Avoid untrusted third-party tools or scripts to prevent malware.
- **Testing**: Use a secondary account or test environment to avoid impacting primary accounts.

## Troubleshooting

- **Window Not Found**:
  - Verify `WINDOW_TITLE` matches the application’s exact title.
  - Check if the application is running in windowed mode.
- **Clicks Misaligned**:
  - Recalibrate coordinates using `pyautogui.displayMousePosition()`.
  - Ensure the window resolution is consistent.
- **Script Stops Unexpectedly**:
  - Check terminal output for error messages.
  - Ensure action scripts have a valid `execute()` function and are in `/actions`.

## Contributing

To extend the framework:

- Add new action scripts for specific tasks.
- Enhance `main.py` with features like pixel color checks, logging to a file, or advanced randomization.
- Share improvements or bug fixes via pull requests (if hosted in a repository).
- Create forks for different applications with actions specific to that application.

## License

This framework is provided as-is for educational purposes. Use responsibly and respect the target application’s terms of service.