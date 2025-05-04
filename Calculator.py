import tkinter as tk

# Font and colors
FONT = ('Poppins', 18)
BG_COLOR = "#e3f2fd"  # Light blue
ENTRY_COLOR = "#bbdefb"
BTN_COLOR = "#90caf9"
BTN_TEXT_COLOR = "#0d47a1"
BTN_ACTIVE_COLOR = "#64b5f6"
CLR_BTN_COLOR = "#42a5f5"
CLR_BTN_ACTIVE = "#1e88e5"

# Create main window
root = tk.Tk()
root.title("Blue Calculator")
root.configure(bg=BG_COLOR)

# Set window size and make it non-resizable
root.geometry("360x520")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, font=FONT, bd=0, bg=ENTRY_COLOR, justify="right", relief="flat")
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20, ipady=20, sticky="nsew")

# Button functions
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Create buttons using grid
for i, row in enumerate(buttons):
    for j, char in enumerate(row):
        action = calculate if char == '=' else lambda ch=char: click(ch)
        tk.Button(
            root, text=char, font=FONT, bg=BTN_COLOR, fg=BTN_TEXT_COLOR,
            activebackground=BTN_ACTIVE_COLOR, relief="flat", width=5, height=2,
            command=action
        ).grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")

# Clear button (spanning all columns)
tk.Button(
    root, text='Clear', font=FONT, bg=CLR_BTN_COLOR, fg="white",
    activebackground=CLR_BTN_ACTIVE, relief="flat", height=2,
    command=clear
).grid(row=5, column=0, columnspan=4, padx=20, pady=10, sticky="nsew")

# Configure grid weights to ensure resizing behavior
for i in range(6):  # 0–5 rows
    root.grid_rowconfigure(i, weight=1)
for j in range(4):  # 0–3 columns
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
