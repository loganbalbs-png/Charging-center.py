import tkinter as tk

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

root = tk.Tk()
root.title("AERO Notes")
root.geometry("800x480")

title = tk.Label(
    root,
    text="📝 AERO Notes",
    font=("Arial", 24, "bold")
)
title.pack(pady=10)

text = tk.Text(
    root,
    font=("Arial", 14)
)
text.pack(fill="both", expand=True)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

save_button = tk.Button(
    button_frame,
    text="Save",
    command=save_note
)
save_button.pack(side="left", padx=10)

load_button = tk.Button(
    button_frame,
    text="Load",
    command=load_note
)
load_button.pack(side="left", padx=10)

load_note()

root.mainloop()
