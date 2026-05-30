import tkinter as tk

root = tk.Tk()
root.title("AERO Notes")
root.geometry("800x480")
root.configure(bg="#7fdfff")

# Header
header = tk.Frame(root, bg="#0057d8", height=60)
header.pack(fill="x")

title = tk.Label(
    header,
    text="📝 AERO Notes",
    font=("Arial", 24, "bold"),
    bg="#0057d8",
    fg="white"
)
title.pack(pady=10)

# Subtitle
subtitle = tk.Label(
    root,
    text="Write. Save. Remember.",
    font=("Arial", 14),
    bg="#7fdfff",
    fg="#003366"
)
subtitle.pack(pady=5)

# Main note box
text = tk.Text(
    root,
    font=("Courier New", 18),
    bd=0
)
text.pack(
    padx=30,
    pady=20,
    fill="both",
    expand=True
)

# Buttons
button_frame = tk.Frame(root, bg="#7fdfff")
button_frame.pack(pady=10)

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

save_btn = tk.Button(
    button_frame,
    text="💾 Save",
    font=("Arial", 14, "bold"),
    bg="#0066ff",
    fg="white",
    width=12,
    command=save_note
)
save_btn.pack(side="left", padx=20)

load_btn = tk.Button(
    button_frame,
    text="📂 Load",
    font=("Arial", 14, "bold"),
    bg="#d9e8ff",
    width=12,
    command=load_note
)
load_btn.pack(side="left", padx=20)

load_note()

root.mainloop()
