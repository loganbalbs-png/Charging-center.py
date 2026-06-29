import tkinter as tk
import time

WIDTH = 800
HEIGHT = 480

root = tk.Tk()
root.title("AERO-OS")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.attributes("-fullscreen", True)

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# ---------- Background ----------
canvas.create_rectangle(
    0, 0,
    WIDTH, HEIGHT,
    fill="#74D8FF",
    outline=""
)

# Top Bar
canvas.create_rectangle(
    0, 0,
    WIDTH, 40,
    fill="#CFF8FF",
    outline=""
)

canvas.create_text(
    20,
    20,
    text="AERO-OS",
    anchor="w",
    font=("Arial",18,"bold"),
    fill="#0077AA"
)

clock = canvas.create_text(
    WIDTH-20,
    20,
    text="",
    anchor="e",
    font=("Arial",14,"bold"),
    fill="#0077AA"
)

# Bottom Taskbar
canvas.create_rectangle(
    0,
    HEIGHT-45,
    WIDTH,
    HEIGHT,
    fill="#DDF9FF",
    outline=""
)

canvas.create_text(
    50,
    HEIGHT-22,
    text="START",
    font=("Arial",14,"bold"),
    fill="#0077AA"
)

def update_clock():
    canvas.itemconfig(
        clock,
        text=time.strftime("%I:%M %p")
    )
    root.after(1000, update_clock)

def open_app(name):
    win = tk.Toplevel(root)
    win.title(name)
    win.geometry("350x220")

    tk.Label(
        win,
        text=name,
        font=("Arial",20,"bold")
    ).pack(pady=20)

    tk.Label(
        win,
        text="Coming Soon!",
        font=("Arial",14)
    ).pack()

# ---------- Apps ----------

apps = [
    ("🌐","AeroNet"),
    ("📝","AeroNotes"),
    ("📁","AeroFiles"),
    ("📷","AeroCam"),
    ("🖼","Gallery"),
    ("🎵","Music"),
    ("⚡","Charge"),
    ("🌈","AeroAI"),
    ("🛒","Store"),
    ("⚙","Settings"),
    ("💻","Terminal"),
    ("🎮","Games")
]

start_x = 90
start_y = 90
spacing_x = 170
spacing_y = 110

for i,(icon,name) in enumerate(apps):

    row = i // 4
    col = i % 4

    x = start_x + col*spacing_x
    y = start_y + row*spacing_y

    btn = tk.Button(
        root,
        text=f"{icon}\n{name}",
        width=12,
        height=3,
        bg="#EFFFFF",
        command=lambda n=name: open_app(n)
    )

    btn.place(x=x-45,y=y-20)

update_clock()

root.mainloop()
