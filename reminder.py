import time
import tkinter as tk
from tkinter import ttk


def build_reminder_window(message: str):
    root = tk.Tk()
    root.title("ANVReminder")
    root.geometry("400x200")

    frame = ttk.Frame(root, padding=20)
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
        command=root.destroy
    )
    button.pack()

    root.mainloop()


def set_reminder(message: str, duration: int):
    """
    Set a reminder.

    Parameters:
    - message: Message to be displayed upon alarm trigger.
    - duration: Time in milliseconds until the alarm triggers.
    """

    print("Alarm set to trigger in", duration)
    time.sleep(duration / 1000)
    build_reminder_window(message)