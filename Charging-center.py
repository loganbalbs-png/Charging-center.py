import tkinter as tk
import time

root = tk.Tk()
root.title("AERO-OS")
root.geometry("800x480")

# Frutiger Aero colors
BG = "#7fdfff"
TASKBAR = "#0057d8"

root.configure(bg=BG)

# ---------- TOP BAR ----------

top = tk.Frame(root, bg=TASKBAR, height=40)
top.pack(fill="x")

clock = tk.Label(
    top,
    text="",
    bg=TASKBAR,
    fg="white",
    font=("Arial", 12)
)

clock.pack(side="right", padx=10)

title = tk.Label(
    top,
    text="🌊 AERO-OS",
    bg=TASKBAR,
    fg="white",
    font=("Arial", 16, "bold")
)

title.pack(side="left", padx=10)

# ---------- DESKTOP ----------

desktop = tk.Frame(root, bg=BG)
desktop.pack(fill="both", expand=True)

apps = [
    "📝 Notes",
    "🧮 Calculator",
    "📷 Camera",
    "🖼 Photos",
    "🎵 Music",
    "📁 Files",
    "⚙️ Settings",
    "🌈 AI",
    "🛒 Store",
    "🌦 Weather"
]

row = 0
col = 0

for app in apps:

    btn = tk.Button(
        desktop,
        text=app,
        width=15,
        height=4,
        font=("Arial", 12)
    )

    btn.grid(
        row=row,
        column=col,
        padx=10,
        pady=10
    )

    col += 1

    if col > 2:
        col = 0
        row += 1

# ---------- TASKBAR ----------

bottom = tk.Frame(root, bg=TASKBAR, height=40)
bottom.pack(fill="x")

start = tk.Button(
    bottom,
    text="Start"
)

start.pack(side="left", padx=5)

wifi = tk.Label(
    bottom,
    text="📶",
    bg=TASKBAR,
    fg="white"
)

wifi.pack(side="right", padx=5)

battery = tk.Label(
    bottom,
    text="🔋",
    bg=TASKBAR,
    fg="white"
)

battery.pack(side="right", padx=5)

volume = tk.Label(
    bottom,
    text="🔊",
    bg=TASKBAR,
    fg="white"
)

volume.pack(side="right", padx=5)

# ---------- CLOCK ----------

def update_clock():
    clock.config(
        text=time.strftime("%I:%M %p")
    )

    root.after(
        1000,
        update_clock
    )

update_clock()

root.mainloop()
