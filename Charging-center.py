import tkinter as tk
import time

WIDTH = 800
HEIGHT = 480

root = tk.Tk()
root.title("AERO-OS")
root.geometry("800x480")
root.attributes("-fullscreen", True)
root.configure(bg="#66CCFF")

# -----------------------
# Desktop Background
# -----------------------

desktop = tk.Frame(root, bg="#66CCFF")
desktop.pack(fill="both", expand=True)

# -----------------------
# Top Bar
# -----------------------

topbar = tk.Frame(
    desktop,
    bg="#DDF9FF",
    height=45
)

topbar.pack(fill="x")

title = tk.Label(
    topbar,
    text="AERO-OS",
    bg="#DDF9FF",
    fg="#0077AA",
    font=("Arial",18,"bold")
)

title.pack(
    side="left",
    padx=15
)

clock = tk.Label(
    topbar,
    bg="#DDF9FF",
    fg="#0077AA",
    font=("Arial",14,"bold")
)

clock.pack(
    side="right",
    padx=15
)

def update_clock():

    clock.config(
        text=time.strftime("%I:%M %p")
    )

    root.after(
        1000,
        update_clock
    )

update_clock()

# -----------------------
# Desktop Area
# -----------------------

icons = tk.Frame(
    desktop,
    bg="#66CCFF"
)

icons.pack(
    expand=True,
    fill="both",
    pady=20
)

def open_app(name):

    app = tk.Toplevel(root)

    app.title(name)

    app.geometry("400x300")

    app.configure(bg="#DDF9FF")

    tk.Label(
        app,
        text=name,
        bg="#DDF9FF",
        fg="#0077AA",
        font=("Arial",22,"bold")
    ).pack(
        pady=25
    )

    tk.Label(
        app,
        text="Coming Soon",
        bg="#DDF9FF",
        font=("Arial",14)
    ).pack()

apps = [

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
# -----------------------
# Desktop Icons
# -----------------------

rows = 3
cols = 4

for i, (icon, name) in enumerate(apps):

    row = i // cols
    col = i % cols

    button = tk.Button(
        icons,
        text=f"{icon}\n{name}",
        font=("Arial", 13, "bold"),
        width=12,
        height=4,
        bg="#EFFFFF",
        fg="#0077AA",
        activebackground="#C8F4FF",
        relief="raised",
        bd=3,
        command=lambda n=name: open_app(n)
    )

    button.grid(
        row=row,
        column=col,
        padx=20,
        pady=15
    )

# -----------------------
# Bottom Taskbar
# -----------------------

taskbar = tk.Frame(
    desktop,
    bg="#DDF9FF",
    height=45
)

taskbar.pack(
    side="bottom",
    fill="x"
)

# Start Menu

def start_menu():

    menu = tk.Toplevel(root)

    menu.title("Start")

    menu.geometry("250x320")

    menu.configure(bg="#DDF9FF")

    tk.Label(
        menu,
        text="AERO-OS",
        bg="#DDF9FF",
        fg="#0077AA",
        font=("Arial",20,"bold")
    ).pack(pady=15)

    options = [
        "🌐 AeroNet",
        "📝 AeroNotes",
        "📁 AeroFiles",
        "📷 AeroCam",
        "🎮 Games",
        "⚙️ Settings"
    ]

    for item in options:

        tk.Button(
            menu,
            text=item,
            width=22,
            bg="#EFFFFF"
        ).pack(pady=4)

    tk.Button(
        menu,
        text="Exit AERO-OS",
        bg="#FFCCCC",
        command=root.destroy
    ).pack(pady=20)

start = tk.Button(
    taskbar,
    text="🟢 START",
    bg="#EFFFFF",
    fg="#0077AA",
    font=("Arial",12,"bold"),
    command=start_menu
)

start.pack(
    side="left",
    padx=10,
    pady=5
)

status = tk.Label(
    taskbar,
    text="Welcome to AERO-OS",
    bg="#DDF9FF",
    fg="#0077AA",
    font=("Arial",10)
)

status.pack(
    side="left",
    padx=20
)

exit_button = tk.Button(
    taskbar,
    text="❌ Exit",
    bg="#FFCCCC",
    command=root.destroy
)

exit_button.pack(
    side="right",
    padx=10,
    pady=5
)

root.mainloop()
