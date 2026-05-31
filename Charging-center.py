import tkinter as tk
import time
import random

WIDTH = 800
HEIGHT = 480

root = tk.Tk()
root.title("AERO Charging Center")
root.geometry("800x480")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#87CEFA")
canvas.place(x=0, y=0)

# Hill
canvas.create_arc(
    -200, 250, 1000, 900,
    start=0,
    extent=180,
    fill="#33CC66",
    outline="#33CC66"
)

# Coral
canvas.create_text(100, 420, text="Y Y Y", fill="coral", font=("Arial", 28, "bold"))
canvas.create_text(700, 420, text="W W W", fill="tomato", font=("Arial", 28, "bold"))

# Seaweed
canvas.create_text(180, 430, text="))) ))) )))", fill="green", font=("Arial", 22, "bold"))
canvas.create_text(620, 430, text="((( ((( (((", fill="darkgreen", font=("Arial", 22, "bold"))

# Bubbles
bubbles = []
for i in range(40):
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

# Fish
fish1 = canvas.create_text(-50, 250, text="><(((°>", fill="white", font=("Arial", 18))
fish2 = canvas.create_text(850, 320, text="<°)))><", fill="white", font=("Arial", 18))
fish3 = canvas.create_text(-100, 180, text="><(((°>", fill="lightcyan", font=("Arial", 16))

# Clock
clock_text = canvas.create_text(
    400,
    60,
    text="",
    fill="white",
    font=("Arial", 28, "bold")
)

# Charging Status
status_text = canvas.create_text(
    400,
    220,
    text="Select Devices",
    fill="white",
    font=("Arial", 18, "bold"),
    justify="center"
)

charging_devices = []

def set_device(device):

    if device in charging_devices:
        charging_devices.remove(device)
    else:
        charging_devices.append(device)

    if len(charging_devices) == 0:
        display = "Select Devices"
    else:
        display = "CURRENTLY CHARGING\n\n"

        for item in charging_devices:
            display += "• " + item + "\n"

    canvas.itemconfig(status_text, text=display)

# Buttons
tk.Button(root, text="Apple Watch",
          command=lambda: set_device("Apple Watch")).place(x=20, y=120)

tk.Button(root, text="AirPods",
          command=lambda: set_device("AirPods")).place(x=20, y=170)

tk.Button(root, text="iPhone",
          command=lambda: set_device("iPhone")).place(x=20, y=220)

tk.Button(root, text="Cyberdeck",
          command=lambda: set_device("Cyberdeck")).place(x=650, y=120)

tk.Button(root, text="iPad",
          command=lambda: set_device("iPad")).place(x=650, y=170)

tk.Button(root, text="MacBook",
          command=lambda: set_device("MacBook")).place(x=650, y=220)

def update():

    canvas.itemconfig(
        clock_text,
        text=time.strftime("%H:%M:%S")
    )

    # Bubbles
    for bubble, speed in bubbles:

        canvas.move(bubble, 0, -speed)

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

    # Fish
    canvas.move(fish1, 1, 0)
    canvas.move(fish2, -1, 0)
    canvas.move(fish3, 0.5, 0)

    x1, y1 = canvas.coords(fish1)
    x2, y2 = canvas.coords(fish2)
    x3, y3 = canvas.coords(fish3)

    if x1 > WIDTH + 50:
        canvas.coords(fish1, -50, y1)

    if x2 < -50:
        canvas.coords(fish2, WIDTH + 50, y2)

    if x3 > WIDTH + 100:
        canvas.coords(fish3, -100, y3)

    root.after(30, update)

update()

root.mainloop()
