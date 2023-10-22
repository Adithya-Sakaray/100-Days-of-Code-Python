import tkinter as tk
from tkinter import messagebox
import threading
import time

root = tk.Tk()
root.title("Dangerous Writing App")

text = tk.Text(root, height=10, width=40)
text.pack()
timer_seconds = 10
timer_running = False

def start_timer():
    global timer_running
    if not timer_running:
        timer_running = True
        timer_thread = threading.Thread(target=countdown)
        timer_thread.start()

def reset_timer():
    global timer_seconds, timer_running
    timer_running = False
    timer_seconds = 10
    text.delete('1.0', tk.END)

def countdown():
    global timer_seconds, timer_running
    while timer_seconds > 0 and timer_running:
        timer_seconds -= 1
        time.sleep(1)
    if timer_running:
        root.after(0, delete_text)

def delete_text():
    global timer_running
    text.delete('1.0', tk.END)
    timer_running = False
    messagebox.showwarning("Text Deleted", "You didn't write for too long!")

def on_text_change(event):
    global timer_seconds
    text_content = text.get('1.0', tk.END)
    if text_content.strip():
        timer_seconds = 10  # Reset the timer when the user starts typing
        if not timer_running:
            start_timer()

text.bind("<KeyRelease>", on_text_change)

start_timer()  # Start the timer automatically

reset_button = tk.Button(root, text="Reset", command=reset_timer)
reset_button.pack()

root.mainloop()
