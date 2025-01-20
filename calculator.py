import tkinter as tk

# Function to update the display
def append_to_display(value):
    current = display_var.get()
    display_var.set(current + value)

# Function to clear the display
def clear_display():
    display_var.set("")

# Function to evaluate the expression
def calculate():
    try:
        expression = display_var.get()
        result = eval(expression)
        display_var.set(str(result))
    except Exception:
        display_var.set("Error")

# Create the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Variable to store the display content
display_var = tk.StringVar()

# Display entry widget
display = tk.Entry(root, textvariable=display_var, font=("Arial", 20), bd=10, relief="ridge", justify="right")
display.pack(fill="both", padx=10, pady=10)

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

# Create buttons dynamically
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for button_text in row:
        if button_text == "C":
            button = tk.Button(frame, text=button_text, font=("Arial", 18), bg="#FF4136", fg="white",
                               command=clear_display)
        elif button_text == "=":
            button = tk.Button(frame, text=button_text, font=("Arial", 18), bg="#28A745", fg="white",
                               command=calculate)
        else:
            button = tk.Button(frame, text=button_text, font=("Arial", 18), bg="#007BFF", fg="white",
                               command=lambda bt=button_text: append_to_display(bt))
        button.pack(side="left", expand=True, fill="both", padx=5, pady=5)

# Run the main application loop
root.mainloop()
