# Locker Screensaver

This Python program creates a screensaver that locks the screen and prevents the system from going to sleep. It also moves the cursor to random positions on the screen at regular intervals.

## Features
- Saves display resources and elecctricity by turning off the backlight and screen
- Fullscreen mode with hidden cursor
- Customizable text display
- Cursor movement to random positions at regular intervals
- Prevents system from sleeping
- Handles Ctrl+H to exit the application
- Ignores Home button press

## Requirements
- Python 3.x
- `tkinter` module
- `xdotool` utility
- `xset` utility

## Installation
1. Install Python 3.x if not already installed.
2. Ensure `tkinter`, `xdotool`, and `xset` are installed on your system.

## Usage
1. Clone the repository:
   ```
   git clone https://github.com/aronbergman/screensaver_42.git
   cd screensaver_42
   ```
2. Run the program:
   ```
   python locker.py
   ```
   If screen dimensions are not provided, the program will detect them automatically.

## How It Works
- The program creates a fullscreen Tkinter window with a hidden cursor.
- A label with custom text (currently empty) is displayed.
- The cursor is moved to random positions on the screen every 55 seconds.
- The system is prevented from sleeping by calling `xset` regularly.
- The program handles Ctrl+H to exit and ignores Home button presses.

## Customization
- To customize the displayed text, modify the `text` variable in the `locker.py` file.
- Adjust the cursor movement interval by changing the `time.sleep(55)` value in the `move_cursor` function.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
Special thanks to the contributors and maintainers of the libraries and utilities used in this project.

Feel free to update and expand this README as necessary.
