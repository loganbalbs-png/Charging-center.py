import tkinter as tk
import time
import random

WIDTH = 800
HEIGHT = 480

root = tk.Tk()
root.title("AERO Charging Center")
root.geometry("800x480")

# Canvas
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Background
canvas.create_rectangle(
    0, 0, WIDTH, HEIGHT,
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

for i in range(20):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    size = random.randint(20, 50)

    bubble = canvas.create_oval(
        x, y,
        x + size, y + size,
        outline="white",
        width=2
    )

    bubbles.append((bubble, random.uniform(0.5, 2)))

# Title
canvas.create_text(
    400, 50,
    text="AERO CHARGING CENTER",
    font=("Arial", 24, "bold"),
    fill="white"
)

# Clock
clock_text = canvas.create_text(
    400, 120,
    text="",
    font=("Arial", 36, "bold"),
    fill="white"
)

# Status
status_text = canvas.create_text(
    400, 190,
    text="Select a Device",
    font=("Arial", 22, "bold"),
    fill="#CCFFCC"
)

# Footer
canvas.create_text(
    400, 450,
    text="AERO-OS Charging Hub",
    font=("Arial", 12),
    fill="white"
)

# Device selector
def set_device(device):
    canvas.itemconfig(
        status_text,
        text=f"Charging {device}"
    )

# LEFT BUTTONS
left_frame = tk.Frame(root, bg="#87CEFA")
canvas.create_window(
    110,
    180,
    window=left_frame
)

# RIGHT BUTTONS
right_frame = tk.Frame(root, bg="#87CEFA")
canvas.create_window(
    690,
    180,
    window=right_frame
)

# Buttons
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

    root.after(30, update)

update()

root.mainloop()
