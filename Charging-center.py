import tkinter as tk
import time
import random
WIDTH = 800
HEIGHT = 480
root = tk.Tk()
root.title("AERO Charging Center")
root.geometry("800x480")
# Background canvas
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, highlightthickness=0)
canvas.place(x=0, y=0)
# Sky/water
canvas.create_rectangle(
    0, 0, WIDTH, HEIGHT,
    fill="#87CEFA",
    outline=""
)
# Underwater hill
canvas.create_arc(
    -200, 250,
    1000, 900,
    start=0,
    extent=180,
    fill="#33CC66",
    outline="#33CC66"
)
# Coral
canvas.create_text(
    100, 420,
    text="Y Y Y",
    font=("Arial", 28, "bold"),
    fill="#FF7F50"
)
canvas.create_text(
    700, 420,
    text="W W W",
    font=("Arial", 26, "bold"),
    fill="#FF6347"
)
canvas.create_text(
    250, 440,
    text="Y W Y",
    font=("Arial", 20, "bold"),
    fill="#FF8C69"
)
# Lots of bubbles
bubbles = []
for i in range(50):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    size = random.randint(10, 35)
    bubble = canvas.create_oval(
        x, y,
        x + size,
        y + size,
        outline="white",
        width=2
    )
    bubbles.append((bubble, random.uniform(0.5, 2)))
# Fish
fish1 = canvas.create_text(-50, 280, text="><(((°>", fill="white", font=("Arial", 18))
fish2 = canvas.create_text(850, 340, text="<°)))><", fill="white", font=("Arial", 18))
fish3 = canvas.create_text(-100, 220, text="><(((°>", fill="#E0FFFF", font=("Arial", 16))
fish4 = canvas.create_text(900, 390, text="<°)))><", fill="#B0E0E6", font=("Arial", 22))
fish5 = canvas.create_text(-150, 170, text="><(((°>", fill="white", font=("Arial", 14))
# Title
canvas.create_text(
    400,
    50,
    text="AERO CHARGING CENTER",
    fill="white",
    font=("Arial", 24, "bold")
)
# Clock
clock_text = canvas.create_text(
    400,
    100,
    text="",
    fill="white",
    font=("Arial", 32, "bold")
)
# Status
status_text = canvas.create_text(
    400,
    220,
    text="Select Devices",
    fill="#CCFFCC",
    font=("Arial", 18, "bold"),
    justify="center"
)
# Charging list
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
    canvas.itemconfig(
        status_text,
        text=display
    )
# LEFT BUTTONS
tk.Button(
    root,
    text="Apple Watch",
    width=15,
    command=lambda: set_device("Apple Watch")
).place(x=20, y=120)
tk.Button(
    root,
    text="AirPods",
    width=15,
    command=lambda: set_device("AirPods")
).place(x=20, y=170)
tk.Button(
    root,
    text="iPhone",
    width=15,
    command=lambda: set_device("iPhone")
).place(x=20, y=220)
# RIGHT BUTTONS
tk.Button(
    root,
    text="Cyberdeck",
    width=15,
    command=lambda: set_device("Cyberdeck")
).place(x=620, y=120)
tk.Button(
    root,
    text="iPad",
    width=15,
    command=lambda: set_device("iPad")
).place(x=620, y=170)
tk.Button(
    root,
    text="MacBook",
    width=15,
    command=lambda: set_device("MacBook")
).place(x=620, y=220)
# Footer
canvas.create_text(
    400,
    455,
    text="AERO-OS Charging Hub",
    fill="white",
    font=("Arial", 12)
)
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
            canvas.coords(
                bubble,
                random.randint(0, WIDTH),
                HEIGHT,
                random.randint(0, WIDTH) + size,
                HEIGHT + size
            )
    # Fish movement
    canvas.move(fish1, 2, 0)
    canvas.move(fish2, -2, 0)
    canvas.move(fish3, 1, 0)
    canvas.move(fish4, -3, 0)
    canvas.move(fish5, 0.7, 0)
    root.after(30, update)
update()
root.mainloop()
