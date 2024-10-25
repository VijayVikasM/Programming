import tkinter as tk
from math import *

# Function to evaluate the calculator expression
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Error")
        screen.update()
    elif text == "CE":
        screen_var.set("")
        screen.update()
    elif text == "π":
        screen_var.set(screen_var.get() + str(pi))
        screen.update()
    elif text == "e":
        screen_var.set(screen_var.get() + str(e))
        screen.update()
    elif text == "√":
        try:
            value = eval(screen.get())
            screen_var.set(sqrt(value))
        except Exception as e:
            screen_var.set("Error")
        screen.update()
    elif text == "x²":
        try:
            value = eval(screen.get())
            screen_var.set(pow(value, 2))
        except Exception as e:
            screen_var.set("Error")
        screen.update()
    elif text == "x³":
        try:
            value = eval(screen.get())
            screen_var.set(pow(value, 3))
        except Exception as e:
            screen_var.set("Error")
        screen.update()
    elif text == "sin":
        try:
            value = eval(screen.get())
            screen_var.set(sin(value))
        except Exception as e:
            screen_var.set("Error")
        screen.update()
    elif text == "cos":
        try:
            value = eval(screen.get())
            screen_var.set(cos(value))
        except Exception as e:
            screen_var.set("Error")
        screen.update()
    elif text == "tan":
        try:
            value = eval(screen.get())
            screen_var.set(tan(value))
        except Exception as e:
            screen_var.set("Error")
        screen.update()
    elif text == "ln":
        try:
            value = eval(screen.get())
            screen_var.set(log(value))
        except Exception as e:
            screen_var.set("Error")
        screen.update()
    elif text == "log10":
        try:
            value = eval(screen.get())
            screen_var.set(log10(value))
        except Exception as e:
            screen_var.set("Error")
        screen.update()
    elif text == "log2":
        try:
            value = eval(screen.get())
            screen_var.set(log2(value))
        except Exception as e:
            screen_var.set("Error")
        screen.update()
    elif text == "Exp":
        screen_var.set(screen_var.get() + "*10**")
        screen.update()
    elif text == "x!":
        try:
            value = eval(screen.get())
            screen_var.set(factorial(value))
        except Exception as e:
            screen_var.set("Error")
        screen.update()
    elif text == "1/x":
        try:
            value = eval(screen.get())
            screen_var.set(1 / value)
        except Exception as e:
            screen_var.set("Error")
        screen.update()
    elif text == "Deg":
        try:
            value = eval(screen.get())
            screen_var.set(degrees(value))
        except Exception as e:
            screen_var.set("Error")
        screen.update()
    elif text == "Rad":
        try:
            value = eval(screen.get())
            screen_var.set(radians(value))
        except Exception as e:
            screen_var.set("Error")
        screen.update()
    elif text == "Abs":
        try:
            value = eval(screen.get())
            screen_var.set(abs(value))
        except Exception as e:
            screen_var.set("Error")
        screen.update()
    else:
        screen_var.set(screen_var.get() + text)
        screen.update()

# Main application window
root = tk.Tk()
root.geometry("450x700")
root.title("Scientific Calculator")

# Screen to display the entered expression or result
screen_var = tk.StringVar()
screen_var.set("")
screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold", bd=10, relief=tk.SUNKEN, justify="right", bg='darkblue', fg='yellow')
screen.grid(row=0, column=0, columnspan=5, ipadx=8, pady=10, padx=10)

# Updated Button layout with brackets at the last row
buttons = [
    ["CE", "√", "+", "π", "e"],
    ["7", "8", "9", "-", "Exp"],
    ["4", "5", "6", "*", "x!"],
    ["1", "2", "3", "/", "Deg"],
    ["0", ".", "=", "Rad", "x²"],
    ["sin", "cos", "tan", "10ⁿ", "x³"],
    ["sinh", "cosh", "tanh", "1/x", "Abs"],
    ["ln", "log2", "log10", "(", ")"]
]

# Create and place buttons using grid layout
for i, row in enumerate(buttons):
    for j, button_text in enumerate(row):
        button = tk.Button(root, text=button_text, font="lucida 15 bold", relief=tk.RAISED, bd=8)
        button.grid(row=i+1, column=j, sticky="nsew", padx=5, pady=5)
        button.bind("<Button-1>", click)

# Make the buttons responsive to window resizing
for i in range(8):  # 8 rows of buttons
    root.grid_rowconfigure(i+1, weight=1)
for j in range(5):  # 5 columns of buttons
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
