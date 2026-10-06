import tkinter as tk
from tkinter import ttk

class GUI:



    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()



    def set_reminder(self, message, duration):
        self.root.after(
            duration,
            self.build_reminder_window,
            message
        )



    def build_reminder_window(self, message: str):
        window = tk.Toplevel(self.root)
        window.title("ANVReminder")
        window.geometry("400x200")

        frame = ttk.Frame(window, padding=20)
        frame.pack(fill="both", expand=True)

        label = ttk.Label(
            frame,
            text=message,
            font=("Arial", 16),
            wraplength=350
        )
        label.pack(expand=True)

        button = ttk.Button(
            frame,
            text="Dismiss",
            command=window.destroy
        )
        button.pack()



    def run(self):
        self.root.mainloop()



    def destroy(self):
        self.root.destroy()