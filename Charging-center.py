import tkinter as tk
import time

root = tk.Tk()
root.title("AERO Charging Center")
root.geometry("800x480")
root.attributes("-fullscreen", True)

root.configure(bg="black")

title = tk.Label(
    root,
    text="⚡ AERO CHARGING CENTER ⚡",
    font=("Arial", 28, "bold"),
    bg="black",
    fg="cyan"
)
title.pack(pady=20)

battery = tk.Label(
    root,
    text="Battery: Charging...",
    font=("Arial", 22),
    bg="black",
    fg="lime"
)
battery.pack(pady=20)

clock = tk.Label(
    root,
    font=("Arial", 48),
    bg="black",
    fg="white"
)
clock.pack(pady=30)

status = tk.Label(
    root,
    text="Cyberdeck Docked",
    font=("Arial", 20),
    bg="black",
    fg="cyan"
)
status.pack()

def update_time():
    clock.config(text=time.strftime("%H:%M:%S"))
    root.after(1000, update_time)

update_time()

root.mainloop()
