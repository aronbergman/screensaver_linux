import time  # Import time module for sleep functionality
import sys  # Import sys module for system-specific parameters and functions
import subprocess  # Import subprocess module to execute system commands
import random  # Import random module to generate random numbers
import signal  # Import signal module to handle signals
import tkinter as tk  # Import tkinter module for creating GUI applications

def handle_ctrl_h(signum, frame):
    # Handle Ctrl+H signal (SIGQUIT)
    print("\nExiting...")
    root.quit()
    sys.exit(0)

def close_on_ctrl_h(event):
    # Close application when Ctrl+H is pressed
    if event.keysym == 'h' and event.state & 0x4:
        root.quit()
        sys.exit(0)

def handle_home(event):
    # Ignore Home button press
    print("\nHome")
    return "break"

# Register Ctrl+H signal handler
signal.signal(signal.SIGQUIT, handle_ctrl_h)

# Get screen dimensions
if sys.argv[1:]:
    # Use provided screen dimensions if available
    scr = [sys.argv[1], sys.argv[2]]
else:
    # Get screen dimensions using xrandr command
    xr = [s for s in subprocess.check_output("xrandr").decode("utf-8").split() if "+0+" in s]
    scr = [str(int(n)/2) for n in xr[0].split("+")[0].split("x")]

# Create window
root = tk.Tk()
root.attributes('-fullscreen', True)  # Set window to fullscreen mode
root.config(cursor="none")  # Hide cursor
text = ""
#text = "System Update in Progress. Please do not power off this machine\n\nLinux PAUL-f3Ar4s3 5.15.0-130-generic #140-Ubuntu SMP Wed Dec 18 17:59:53 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux"
#text = "Locked by abergman: a few minuts ago...\n\n\n\n░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░       ░▒▓███████▓▒░ ░▒▓███�[...]

label = tk.Label(root, text=text, font=('mono', 10), fg='#909090', bg='black')  # Create label with custom text and styling
label.pack(expand=True, fill='both')  # Pack label to fill the window

def move_cursor():
    # Function to move cursor to random positions
    counter = 0
    while True:
        try:
            counter += 1
            # Generate random x,y coordinates within screen bounds
            x = random.randint(0, int(float(scr[0])))
            y = random.randint(0, int(float(scr[1])))
            
            # Move cursor to random position
            subprocess.Popen(["xdotool", "mousemove", str(x), str(y)])
            
            print(f"Iteration {counter}: Moved cursor to position {x}, {y}")
            time.sleep(55)  # Wait for 55 seconds before next move
        except KeyboardInterrupt:
            # Handle keyboard interrupt
            print("\nExiting...")
            sys.exit(0)

def prevent_sleep():
    # Prevent system from sleeping
    root.after(1000, prevent_sleep)
    root.update_idletasks()
    root.update()
    subprocess.run(["xset", "-display", ":0.0", "dpms", "force", "off"])

# Start cursor movement in a separate thread
import threading  # Import threading module to handle threads
cursor_thread = threading.Thread(target=move_cursor)  # Create a thread for cursor movement
cursor_thread.daemon = True  # Set thread as daemon
cursor_thread.start()  # Start the thread

prevent_sleep()  # Call prevent_sleep function

# Bind Ctrl+H to close and disable Home key
root.bind('<Key>', close_on_ctrl_h)
root.bind('<Super_L>', handle_home)
root.bind('<Super_R>', handle_home)

root.mainloop()  # Start Tkinter event loop
