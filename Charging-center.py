import tkinter as tk
import time

WIDTH = 800
HEIGHT = 480

root = tk.Tk()
root.title("AERO-OS")
root.geometry("800x480")
root.configure(bg="#6FD6FF")
root.attributes("-fullscreen", True)

# =========================
# Background
# =========================

bg = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg="#6FD6FF",
    highlightthickness=0
)
bg.pack(fill="both", expand=True)

# Top Bar
bg.create_rectangle(
    0,0,
    WIDTH,45,
    fill="#D9F7FF",
    outline=""
)

bg.create_text(
    20,
    22,
    anchor="w",
    text="AERO-OS",
    fill="#0077AA",
    font=("Arial",20,"bold")
)

clock = bg.create_text(
    780,
    22,
    anchor="e",
    text="",
    fill="#0077AA",
    font=("Arial",14,"bold")
)

def update_clock():
    bg.itemconfig(
        clock,
        text=time.strftime("%I:%M %p")
    )
    root.after(
        1000,
        update_clock
    )

update_clock()

# Bottom Taskbar

bg.create_rectangle(
    0,
    435,
    WIDTH,
    HEIGHT,
    fill="#D9F7FF",
    outline=""
)

# Desktop title

bg.create_text(
    400,
    70,
    text="Welcome to AERO-OS",
    fill="white",
    font=("Arial",24,"bold")
)

def open_app(name):

    app=tk.Toplevel(root)
    app.title(name)
    app.geometry("400x300")

    tk.Label(
        app,
        text=name,
        font=("Arial",22,"bold")
    ).pack(pady=20)

    tk.Label(
        app,
        text="Coming Soon",
        font=("Arial",14)
    ).pack()

apps=[
("🌐","AeroNet"),
("📝","AeroNotes"),
("📁","AeroFiles"),
("📷","AeroCam"),
("🖼️","Gallery"),
("🎵","Music"),
("⚡","Charge"),
("⚙️","Settings"),
("🤖","AeroAI"),
("🛒","Store"),
("🎮","Games"),
("💻","Terminal")
]

# =========================
# Desktop Icons
# =========================

start_x = 90
start_y = 110
spacing_x = 170
spacing_y = 110

for i, (icon, name) in enumerate(apps):

    row = i // 4
    col = i % 4

    x = start_x + (col * spacing_x)
    y = start_y + (row * spacing_y)

    btn = tk.Button(
        root,
        text=f"{icon}\n{name}",
        width=12,
        height=3,
        bg="#EFFFFF",
        fg="#0077AA",
        activebackground="#BFEFFF",
        relief="raised",
        bd=2,
        command=lambda n=name: open_app(n)
    )

    btn.place
    x=x-45,
    y=y


btn.lift()
    

# =========================
# Start Button
# =========================

def start_menu():

    menu = tk.Toplevel(root)

    menu.title("Start")

    menu.geometry("240x300+0+180")

    menu.configure(bg="#DDF9FF")

    tk.Label(
        menu,
        text="AERO-OS",
        bg="#DDF9FF",
        fg="#0077AA",
        font=("Arial",18,"bold")
    ).pack(pady=10)

    items = [
        "🌐 AeroNet",
        "📝 AeroNotes",
        "📁 AeroFiles",
        "🎮 Games",
        "⚙️ Settings"
    ]

    for item in items:

        tk.Button(
            menu,
            text=item,
            width=20
        ).pack(pady=4)

    tk.Button(
        menu,
        text="Exit AERO-OS",
        bg="#FFCCCC",
        command=root.destroy
    ).pack(pady=20)

start = tk.Button(
    root,
    text="🟢 START",
    bg="#DDF9FF",
    fg="#0077AA",
    font=("Arial",12,"bold"),
    command=start_menu
)

start.place(
    x=10,
    y=440
)

start.lift()


exit_btn = tk.Button(
    root,
    text="❌",
    bg="#FFAAAA",
    command=root.destroy
)

exit_btn.place(
    x=760,
    y=440
)

exit_btn.lift()
)

bg.create_text(
    400,
    456,
    text="AERO-OS Version 0.2",
    fill="#0077AA",
    font=("Arial",10)
)

root.mainloop()
