# -*- coding: utf-8 -*-

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

canvas.place(x=0, y=0)

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

for i in range(20):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    size = random.randint(20, 50)

    bubble = canvas.create_oval(
        x,
        y,
        x + size,
        y + size,
        outline="white",
        width=2
    )

    bubbles.append((bubble, random.uniform(0.5, 2)))

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
    120,
    text="",
    font=("Arial", 40, "bold"),
    fill="white"
)

# Status
status_text = canvas.create_text(
    400,
    190,
    text="Select a Device",
    font=("Arial", 22, "bold"),
    fill="#CCFFCC"
)

# Footer
canvas.create_text(
    400,
    450,
    text="AERO-OS Charging Hub",
    font=("Arial", 12),
    fill="white"
)

# Device Selection
def set_device(device):
    canvas.itemconfig(
        status_text,
        text="Charging " + device
    )

# Buttons
devices = [
    ("Apple Watch", 20, 120),
    ("AirPods", 20, 170),
    ("iPhone", 20, 220),
    ("Cyberdeck", 620, 120),
    ("iPad", 620, 170),
    ("MacBook", 620, 220)
]

for name, x, y in devices:

    button = tk.Button(
        root,
        text=name,
        width=15,
        command=lambda d=name: set_device(d)
    )

    button.place(
        x=x,
        y=y
    )

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
