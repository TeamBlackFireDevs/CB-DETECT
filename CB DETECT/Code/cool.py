import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def detect_cyberbullying(text):
    return "cyberbullying" in text.lower()

def classify_text():
    user_text = text_input.get("1.0", tk.END).strip()
    if not user_text:
        messagebox.showinfo("Input Error", "Please enter some text to analyze.")
        return

    result = detect_cyberbullying(user_text)
    if result:
        result_label.config(text="Cyberbullying Detected", foreground="red")
    else:
        result_label.config(text="Cyberbullying Detected", foreground="green")

root = tk.Tk()
root.title("Cyberbullying Detector")
root.geometry("400x300")
root.resizable(False, False)

style = ttk.Style(root)
style.theme_use("clam")
style.configure("TButton", font=("Helvetica", 12))
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TFrame", background="#f0f0f0")

frame = ttk.Frame(root, padding="20 20 20 20", style="TFrame")
frame.pack(fill=tk.BOTH, expand=True)

title_label = ttk.Label(frame, text="Cyberbullying Detection", font=("Helvetica", 16, "bold"))
title_label.pack(pady=(0, 10))

text_input = tk.Text(frame, height=5, font=("Helvetica", 12))
text_input.pack(fill=tk.X, pady=10)

analyze_button = ttk.Button(frame, text="Analyze", command=classify_text)
analyze_button.pack(pady=(10, 5))

result_label = ttk.Label(frame, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()
