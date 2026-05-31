import tkinter as tk
import time
import random

WIDTH = 800
HEIGHT = 480

root = tk.Tk()
root.title("AERO Charging Center")
root.geometry("800x480")

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    highlightthickness=0
)

canvas.pack(fill="both", expand=True)

# Background
canvas.create_rectangle(
    0, 0,
    WIDTH, HEIGHT,
    fill="#87CEFA",
    outline=""
)

# Hill
canvas.create_arc(
    -200, 250,
    1000, 900,
    start=0,
    extent=180,
    fill="#33CC66",
    outline="#33CC66"
)

# Bubbles
bubbles = []

for i in range(25):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    size = random.randint(15, 45)

    bubble = canvas.create_oval(
        x,
        y,
        x + size,
        y + size,
        outline="white",
        width=2
    )

    bubbles.append((bubble, random.uniform(0.5, 2)))

# Fish
fish1 = canvas.create_text(
    -50,
    320,
    text="><(((°>",
    font=("Arial", 18),
    fill="white"
)

fish2 = canvas.create_text(
    WIDTH + 50,
    380,
    text="<°)))><",
    font=("Arial", 18),
    fill="white"
)

# Title
canvas.create_text(
    400,
    50,
    text="AERO CHARGING CENTER",
    font=("Arial", 24, "bold"),
    fill="white"
)

# Clock
clock_text = canvas.create_text(
    400,
    110,
    text="",
    font=("Arial", 34, "bold"),
    fill="white"
)

# Status
status_text = canvas.create_text(
    400,
    220,
    text="Select a Device",
    font=("Arial", 18, "bold"),
    fill="#CCFFCC",
    justify="center"
)

# Footer
canvas.create_text(
    400,
    450,
    text="AERO-OS Charging Hub",
    font=("Arial", 12),
    fill="white"
)

# Charging list
charging_devices = []

def set_device(device):

    if device in charging_devices:
        charging_devices.remove(device)
    else:
        charging_devices.append(device)

    if len(charging_devices) == 0:
        display_text = "Select a Device"
    else:
        display_text = "CURRENTLY CHARGING\n\n"

        for item in charging_devices:
            display_text += "• " + item + "\n"

    canvas.itemconfig(
        status_text,
        text=display_text
    )

# Left Buttons
left_frame = tk.Frame(root, bg="#87CEFA")
canvas.create_window(110, 190, window=left_frame)

tk.Button(
    left_frame,
    text="Apple Watch",
    width=15,
    command=lambda: set_device("Apple Watch")
).pack(pady=5)

tk.Button(
    left_frame,
    text="AirPods",
    width=15,
    command=lambda: set_device("AirPods")
).pack(pady=5)

tk.Button(
    left_frame,
    text="iPhone",
    width=15,
    command=lambda: set_device("iPhone")
).pack(pady=5)

# Right Buttons
right_frame = tk.Frame(root, bg="#87CEFA")
canvas.create_window(690, 190, window=right_frame)

tk.Button(
    right_frame,
    text="Cyberdeck",
    width=15,
    command=lambda: set_device("Cyberdeck")
).pack(pady=5)

tk.Button(
    right_frame,
    text="iPad",
    width=15,
    command=lambda: set_device("iPad")
).pack(pady=5)

tk.Button(
    right_frame,
    text="MacBook",
    width=15,
    command=lambda: set_device("MacBook")
).pack(pady=5)

# Animation
def update():

    canvas.itemconfig(
        clock_text,
        text=time.strftime("%H:%M:%S")
    )

    # Move bubbles
    for bubble, speed in bubbles:

        canvas.move(
            bubble,
            0,
            -speed
        )

        x1, y1, x2, y2 = canvas.coords(bubble)

        if y2 < 0:

            size = x2 - x1
            new_x = random.randint(0, WIDTH)

            canvas.coords(
                bubble,
                new_x,
                HEIGHT,
                new_x + size,
                HEIGHT + size
            )

    # Move fish
    canvas.move(fish1, 2, 0)
    canvas.move(fish2, -1.5, 0)

    x1, y1 = canvas.coords(fish1)
    x2, y2 = canvas.coords(fish2)

    if x1 > WIDTH + 50:
        canvas.coords(fish1, -50, y1)

    if x2 < -50:
        canvas.coords(fish2, WIDTH + 50, y2)

    root.after(30, update)

update()

root.mainloop()
