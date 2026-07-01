import tkinter as tk
import time

WIDTH = 800
HEIGHT = 480

root = tk.Tk()
root.title("AERO-OS")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.attributes("-fullscreen", True)

# ---------- LOCK SCREEN ----------

lock = tk.Frame(root, bg="#74D8FF")
lock.pack(fill="both", expand=True)

title = tk.Label(
    lock,
    text="AERO-OS",
    bg="#74D8FF",
    fg="white",
    font=("Arial",30,"bold")
)
title.pack(pady=40)

clock_label = tk.Label(
    lock,
    bg="#74D8FF",
    fg="white",
    font=("Arial",24)
)
clock_label.pack()

subtitle = tk.Label(
    lock,
    text="Slide into AERO",
    bg="#74D8FF",
    fg="white",
    font=("Arial",18,"bold")
)
subtitle.pack(pady=35)

track = tk.Canvas(
    lock,
    width=500,
    height=60,
    bg="#74D8FF",
    highlightthickness=0
)
track.pack()

track.create_rectangle(
    20,
    20,
    480,
    45,
    fill="#DDF9FF",
    outline="white"
)

slider = track.create_oval(
    20,
    10,
    70,
    55,
    fill="#00AAFF",
    outline="white",
    width=2
)

dragging = False

desktop = tk.Frame(root,bg="#74D8FF")

def update_clock():
    clock_label.config(
        text=time.strftime("%I:%M %p")
    )
    root.after(1000,update_clock)

update_clock()

def unlock():
    lock.pack_forget()
    desktop.pack(fill="both",expand=True)

def press(event):
    global dragging

    print("Pressed!")

    x1, y1, x2, y2 = track.coords(slider)

    if x1 <= event.x <= x2:
        dragging = True
        print("Dragging Started")
        
def drag(event):

    global dragging

    if not dragging:
        return

    x=event.x

    if x<20:
        x=20

    if x>430:
        x=430

    track.coords(
        slider,
        x,
        10,
        x+50,
        55
    )

def release(event):

    global dragging
    dragging=False

    x1,y1,x2,y2=track.coords(slider)

    if x1>=425:

        unlock()

    else:

        track.coords(
            slider,
            20,
            10,
            70,
            55
        )

track.bind("<ButtonPress-1>", press)
track.bind("<ButtonRelease-1>", release)
track.bind("<B1-Motion>", drag)

# -----------------------
# DESKTOP
# -----------------------

top=tk.Frame(
    desktop,
    bg="#DDF9FF",
    height=40
)

top.pack(fill="x")

logo=tk.Label(
    top,
    text="AERO-OS",
    bg="#DDF9FF",
    fg="#0077AA",
    font=("Arial",18,"bold")
)

logo.pack(
    side="left",
    padx=15
)

desktop_clock=tk.Label(
    top,
    bg="#DDF9FF",
    fg="#0077AA",
    font=("Arial",14,"bold")
)

desktop_clock.pack(
    side="right",
    padx=15
)

def update_desktop_clock():

    desktop_clock.config(
        text=time.strftime("%I:%M %p")
    )

    root.after(
        1000,
        update_desktop_clock
    )

update_desktop_clock()

def open_app(name):

    app=tk.Toplevel(root)

    app.title(name)

    app.geometry("350x220")

    tk.Label(
        app,
        text=name,
        font=("Arial",20,"bold")
    ).pack(
        pady=20
    )

    tk.Label(
        app,
        text="AERO-OS Application",
        font=("Arial",14)
    ).pack()

apps=[
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
("🎮","Games"),
] 
start_x = 90
start_y = 90
spacing_x = 170
spacing_y = 110

for i, (icon, name) in enumerate(apps):

    row = i // 4
    col = i % 4

    x = start_x + col * spacing_x
    y = start_y + row * spacing_y

    btn = tk.Button(
        desktop,
        text=f"{icon}\n{name}",
        width=12,
        height=3,
        bg="#EFFFFF",
        fg="#006699",
        relief="raised",
        command=lambda n=name: open_app(n)
    )

    btn.place(
        x=x-45,
        y=y
    )

# -----------------------
# TASKBAR
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

start_button = tk.Button(
    taskbar,
    text="🟢 START",
    bg="#CFF8FF",
    fg="#006699",
    font=("Arial", 11, "bold")
)

start_button.pack(
    side="left",
    padx=10,
    pady=5
)

exit_button = tk.Button(
    taskbar,
    text="Exit",
    bg="#FFDDDD",
    command=root.destroy
)

exit_button.pack(
    side="right",
    padx=10,
    pady=5
)

status = tk.Label(
    taskbar,
    text="Welcome to AERO-OS",
    bg="#DDF9FF",
    fg="#006699",
    font=("Arial", 10)
)

status.pack(
    side="left",
    padx=20
)

root.mainloop()
