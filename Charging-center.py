import tkinter as tk

root = tk.Tk()
root.title("AERO-OS")
root.geometry("800x480")
root.configure(bg="#87CEFA")

# ---------- NOTES ----------

def open_notes():

    app = tk.Toplevel(root)
    app.title("AERO Notes")
    app.geometry("600x400")

    title = tk.Label(
        app,
        text="📝 AERO Notes",
        font=("Arial", 20, "bold")
    )
    title.pack()

    text = tk.Text(
        app,
        font=("Arial", 14)
    )
    text.pack(fill="both", expand=True)

    def save_note():
        with open("notes.txt", "w") as file:
            file.write(text.get("1.0", tk.END))

    def load_note():
        try:
            with open("notes.txt", "r") as file:
                text.delete("1.0", tk.END)
                text.insert(tk.END, file.read())
        except:
            pass

    buttons = tk.Frame(app)
    buttons.pack()

    tk.Button(
        buttons,
        text="💾 Save",
        command=save_note
    ).pack(side="left", padx=10)

    tk.Button(
        buttons,
        text="📂 Load",
        command=load_note
    ).pack(side="left", padx=10)

    load_note()

# ---------- CALCULATOR ----------

def open_calculator():

    app = tk.Toplevel(root)
    app.title("Calculator")
    app.geometry("350x450")

    entry = tk.Entry(
        app,
        font=("Arial", 20)
    )

    entry.pack(fill="x")

    def press(value):
        entry.insert(tk.END, value)

    def equals():
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")

    buttons = [
        "7","8","9","+",
        "4","5","6","-",
        "1","2","3","*",
        "0",".","=","/"
    ]

    frame = tk.Frame(app)
    frame.pack()

    r = 0
    c = 0

    for b in buttons:

        if b == "=":
            cmd = equals
        else:
            cmd = lambda x=b: press(x)

        tk.Button(
            frame,
            text=b,
            width=5,
            height=2,
            font=("Arial", 14),
            command=cmd
        ).grid(row=r,column=c)

        c += 1

        if c > 3:
            c = 0
            r += 1

# ---------- PLACEHOLDER APPS ----------

def make_app(name):

    app = tk.Toplevel(root)
    app.title(name)
    app.geometry("500x300")

    tk.Label(
        app,
        text=name,
        font=("Arial", 24, "bold")
    ).pack(pady=50)

    tk.Label(
        app,
        text="Coming Soon",
        font=("Arial", 16)
    ).pack()

# ---------- HOME SCREEN ----------

title = tk.Label(
    root,
    text="🌊 AERO-OS 🌊",
    font=("Arial", 24, "bold"),
    bg="#87CEFA"
)
title.pack(pady=10)

frame = tk.Frame(root,bg="#87CEFA")
frame.pack()

apps = [

    ("📝 Notes", open_notes),
    ("🧮 Calculator", open_calculator),

    ("📷 Camera",
     lambda: make_app("📷 Camera")),

    ("🖼 Photos",
     lambda: make_app("🖼 Photos")),

    ("🎵 Music",
     lambda: make_app("🎵 Music")),

    ("📁 Files",
     lambda: make_app("📁 Files")),

    ("⚙️ Settings",
     lambda: make_app("⚙️ Settings")),

    ("🌈 AERO AI",
     lambda: make_app("🌈 AERO AI")),

    ("🛒 Store",
     lambda: make_app("🛒 Store"))
]

row = 0
col = 0

for text, command in apps:

    btn = tk.Button(
        frame,
        text=text,
        width=15,
        height=4,
        font=("Arial",12),
        command=command
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
