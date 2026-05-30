import tkinter as tk

root = tk.Tk()
root.geometry("800x480")

label = tk.Label(root, text="Not Clicked", font=("Arial", 30))
label.pack(pady=50)

def clicked():
    label.config(text="Clicked!")

button = tk.Button(
    root,
    text="TEST BUTTON",
    font=("Arial", 20),
    command=clicked
)

button.pack(pady=50)

root.mainloop()
