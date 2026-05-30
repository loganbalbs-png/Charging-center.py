import tkinter as tk
import time
import random

root = tk.Tk()
root.title("AERO Charging Center")
root.geometry("800x480")
root.attributes("-fullscreen", True)

canvas = tk.Canvas(root, width=800, height=480, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Frutiger Aero colors
top_color = "#8EEFFF"
bottom_color = "#0078D7"

# Draw gradient
for i in range(480):
    r1, g1, b1 = root.winfo_rgb(top_color)
    r2, g2, b2 = root.winfo_rgb(bottom_color)

    r = int(r1 + (r2 - r1) * i / 480) >> 8
    g = int(g1 + (g2 - g1) * i / 480) >> 8
    b = int(b1 + (b2 - b1) * i / 480) >> 8

    color = f"#{r:02x}{g:02x}{b:02x}"
    canvas.create_line(0, i, 800, i, fill=color)

# Create bubbles
bubbles = []

for _ in range(25):
    x = random.randint(0, 800)
    y = random.randint(0, 480)
    size = random.randint(15, 50)

    bubble = canvas.create_oval(
        x,
        y,
        x + size,
        y + size,
        outline="white"
    )

    bubbles.append((bubble, random.uniform(0.5, 2)))

# Main title
canvas.create_text(
    400,
    70,
    text="⚡ AERO CHARGING CENTER ⚡",
    fill="white",
    font=("Helvetica", 26, "bold")
)

# Cyberdeck text
canvas.create_text(
    400,
    120,
    text="Frutiger Aero Cyberdeck",
    fill="#DFFFFF",
    font=("Helvetica", 14)
)

clock_text = canvas.create_text(
    400,
    230,
    text="",
    fill="white",
    font=("Helvetica", 48, "bold")
)

status_text = canvas.create_text(
    400,
    310,
    text="Charging...",
    fill="#A8FFB0",
    font=("Helvetica", 24)
)

battery_text = canvas.create_text(
    400,
    360,
    text="Battery Connected",
    fill="white",
    font=("Helvetica", 18)
)

canvas.create_text(
    400,
    430,
    text="AERO-OS v1.0",
    fill="#DFFFFF",
    font=("Helvetica", 12)
)

def animate():
    for bubble, speed in bubbles:
        canvas.move(bubble, 0, -speed)

        coords = canvas.coords(bubble)

        if coords[3] < 0:
            size = coords[2] - coords[0]
            x = random.randint(0, 800)

            canvas.coords(
                bubble,
                x,
                500,
                x + size,
                500 + size
            )

    current_time = time.strftime("%H:%M:%S")
    canvas.itemconfig(clock_text, text=current_time)

    root.after(30, animate)

animate()

root.mainloop()
