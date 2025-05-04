import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry widget to display the input/output
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=10, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Function to handle button click
def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Buttons layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
]

for i, row in enumerate(buttons):
    for j, char in enumerate(row):
        if char == '=':
            btn = tk.Button(root, text=char, width=5, height=2, font=('Arial', 18),
                            command=calculate)
        else:
            btn = tk.Button(root, text=char, width=5, height=2, font=('Arial', 18),
                            command=lambda ch=char: click_button(ch))
        btn.grid(row=i+1, column=j)

# Clear button
clear_btn = tk.Button(root, text='C', width=22, height=2, font=('Arial', 18), command=clear)
clear_btn.grid(row=5, column=0, columnspan=4)

# Run the application
root.mainloop()
