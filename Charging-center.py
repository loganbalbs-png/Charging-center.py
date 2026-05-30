import tkinter as tk

root = tk.Tk()
root.title("AERO-OS")
root.geometry("800x480")
root.configure(bg="#87CEFA")

title = tk.Label(
    root,
    text="🌊 AERO-OS 🌊",
    font=("Arial", 24, "bold"),
    bg="#87CEFA"
)
title.pack(pady=20)

def open_app(name):
    app = tk.Toplevel(root)
    app.title(name)
    app.geometry("500x300")

    tk.Label(
        app,
        text=name,
        font=("Arial", 20, "bold")
    ).pack(pady=30)

    tk.Label(
        app,
        text=f"Welcome to {name}",
        font=("Arial", 14)
    ).pack()

apps = [
    "📝 Notes",
    "🧮 Calculator",
    "📷 Camera",
    "🖼 Photos",
    "🎵 Music",
    "📁 Files",
    "⚙️ Settings",
    "🌈 AI",
    "🛒 Store"
]

frame = tk.Frame(root, bg="#87CEFA")
frame.pack()

row = 0
col = 0

for app in apps:
    btn = tk.Button(
        frame,
        text=app,
        width=15,
        height=4,
        font=("Arial", 12),
        command=lambda a=app: open_app(a)
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

root.mainloop()
