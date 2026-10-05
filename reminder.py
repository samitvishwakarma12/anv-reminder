import tkinter as tk
from tkinter import ttk


def build_reminder_window(root: tk.Tk, message: str):
    window = tk.Toplevel(root)
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


def set_reminder(root: tk.Tk, message: str, duration: int):
    """
    Schedule a reminder.

    Parameters:
    - root: Main Tkinter application.
    - message: Message to be displayed upon alarm trigger.
    - duration: Time in milliseconds until the alarm triggers.
    """

    print("Alarm set to trigger in", duration)

    root.after(
        duration,
        build_reminder_window,
        root,
        message
    )