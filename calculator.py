import tkinter as tk
from tkinter import messagebox

def click_button(value):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate_result():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input! {e}")

# Create main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="#dcdcdc")  # Light gray background

# Entry widget
entry = tk.Entry(root, width=15, font=('Arial', 24), borderwidth=5, relief="ridge", bg="#fff", fg="#000")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button definitions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0, 4)
]

# Create buttons with a realistic design
for (text, row, col, *args) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, padx=40, pady=20, command=clear_entry, bg="#ff7f7f", fg="#fff", font=('Arial', 18), borderwidth=3, relief="raised")
        button.grid(row=row, column=col, columnspan=4, sticky="nsew")
    elif text == '=':
        button = tk.Button(root, text=text, padx=40, pady=20, command=calculate_result, bg="#4caf50", fg="#fff", font=('Arial', 18), borderwidth=3, relief="raised")
        button.grid(row=row, column=col)
    else:
        button = tk.Button(root, text=text, padx=40, pady=20, command=lambda t=text: click_button(t), bg="#f0f0f0", fg="#000", font=('Arial', 18), borderwidth=3, relief="raised")
        button.grid(row=row, column=col)

# Adjust column and row weights
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

# Run the application
root.mainloop()