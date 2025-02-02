import time
import sys
import subprocess
import random
import signal
import tkinter as tk

def handle_ctrl_h(signum, frame):
    print("\nExiting...")
    root.quit()
    sys.exit(0)

def close_on_ctrl_h(event):
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
    scr = [sys.argv[1], sys.argv[2]]
else:
    xr = [s for s in subprocess.check_output("xrandr").decode("utf-8").split() if "+0+" in s]
    scr = [str(int(n)/2) for n in xr[0].split("+")[0].split("x")]

# Create window
root = tk.Tk()
root.attributes('-fullscreen', True)
root.config(cursor="none")
text = ""
#text = "System Update in Progress. Please do not power off this machine\n\nLinux PAUL-f3Ar4s3 5.15.0-130-generic #140-Ubuntu SMP Wed Dec 18 17:59:53 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux"
#text = "Locked by abergman: a few minuts ago...\n\n\n\n░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░       ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓███████▓▒░ \n░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░        \n░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░        \n░▒▓████████▓▒░░▒▓██████▓▒░       ░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓██████▓▒░  \n       ░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░ \n       ░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░ \n       ░▒▓█▓▒░▒▓████████▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓███████▓▒░  \n"

label = tk.Label(root, text=text, font=('mono', 10), fg='#909090', bg='black')
label.pack(expand=True, fill='both')


def move_cursor():
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
            time.sleep(55)
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)

def prevent_sleep():
    root.after(1000, prevent_sleep)
    root.update_idletasks()
    root.update()
    subprocess.run(["xset", "-display", ":0.0", "dpms", "force", "off"])

# Start cursor movement in a separate thread
import threading
cursor_thread = threading.Thread(target=move_cursor)
cursor_thread.daemon = True
cursor_thread.start()

prevent_sleep()

# Bind Ctrl+H to close and disable Home key
root.bind('<Key>', close_on_ctrl_h)
root.bind('<Super_L>', handle_home)
root.bind('<Super_R>', handle_home)

root.mainloop()
