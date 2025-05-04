import tkinter as tk

FONT = ('Poppins', 18)
ENTRY_COLOR_LIGHT = "#bbdefb"
ENTRY_COLOR_DARK = "#333333"
BG_COLOR_LIGHT = "#e3f2fd"
BG_COLOR_DARK = "#121212"
BUTTON_COLOR_LIGHT = '#c0c0c0'
BUTTON_COLOR_DARK = '#444444'
BUTTON_TEXT_COLOR_LIGHT = 'black'
BUTTON_TEXT_COLOR_DARK = 'white'

# Neutral colors for buttons
neutral_colors = [
    ['#d3d3d3', '#e0e0e0', '#f5f5f5', '#c0c0c0'],
    ['#f0f0f0', '#dcdcdc', '#f8f8ff', '#b0b0b0'],
    ['#fafafa', '#e8e8e8', '#fdfdfd', '#a9a9a9'],
    ['#fefefe', '#eeeeee', '#ffffff', '#808080']
]

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("360x520")
root.resizable(False, False)

# Initial theme set to light mode
current_theme = 'light'

# Entry field
entry = tk.Entry(root, font=FONT, bd=0, bg=ENTRY_COLOR_LIGHT, justify="right", relief="flat")
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

def toggle_theme():
    global current_theme

    if current_theme == 'light':
        current_theme = 'dark'
        root.configure(bg=BG_COLOR_DARK)
        entry.configure(bg=ENTRY_COLOR_DARK, fg=BUTTON_TEXT_COLOR_DARK)
        toggle_button.configure(bg=BUTTON_COLOR_DARK, fg=BUTTON_TEXT_COLOR_DARK)

        for i, row in enumerate(buttons):
            for j, char in enumerate(row):
                buttons[i][j].configure(bg=BUTTON_COLOR_DARK, fg=BUTTON_TEXT_COLOR_DARK)

    else:
        current_theme = 'light'
        root.configure(bg=BG_COLOR_LIGHT)
        entry.configure(bg=ENTRY_COLOR_LIGHT, fg=BUTTON_TEXT_COLOR_LIGHT)
        toggle_button.configure(bg=BUTTON_COLOR_LIGHT, fg=BUTTON_TEXT_COLOR_LIGHT)

        for i, row in enumerate(buttons):
            for j, char in enumerate(row):
                buttons[i][j].configure(bg=neutral_colors[i][j], fg=BUTTON_TEXT_COLOR_LIGHT)

# Button labels
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Create grid buttons with neutral colors
button_widgets = []
for i, row in enumerate(buttons):
    button_row = []
    for j, char in enumerate(row):
        action = calculate if char == '=' else lambda ch=char: click(ch)
        btn = tk.Button(
            root, text=char, font=FONT, bg=neutral_colors[i][j], fg="#000000",
            activebackground="#bdbdbd", relief="flat", width=5, height=2,
            command=action
        )
        btn.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
        button_row.append(btn)
    button_widgets.append(button_row)

# Clear button (bottom full-width)
tk.Button(
    root, text='Clear', font=FONT, bg="#bdbdbd", fg="black",
    activebackground="#9e9e9e", relief="flat", height=2,
    command=clear
).grid(row=5, column=0, columnspan=4, padx=20, pady=10, sticky="nsew")

# Dark mode toggle button
toggle_button = tk.Button(
    root, text="Toggle Dark Mode", font=FONT, bg=BUTTON_COLOR_LIGHT, fg=BUTTON_TEXT_COLOR_LIGHT,
    activebackground="#9e9e9e", relief="flat", height=2, command=toggle_theme
)
toggle_button.grid(row=6, column=0, columnspan=4, padx=20, pady=10, sticky="nsew")

# Make grid responsive
for i in range(6): root.grid_rowconfigure(i, weight=1)
for j in range(4): root.grid_columnconfigure(j, weight=1)

root.mainloop()
