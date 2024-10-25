#imports
import tkinter as tk
from tkinter import messagebox

#main window setup
root = tk.Tk()
root.title("Basic Calculator with GUI")
root.geometry("300x400")

# Define the input field (display)
input_text = tk.StringVar()  # Holds the current input

# Create an Entry widget for the display
display = tk.Entry(root, textvariable=input_text, font=('Courier', 24), bd=10, insertwidth=4, width=14, borderwidth=4, bg='darkblue', fg='yellow')
display.grid(row=0, column=0, columnspan=4, sticky="nsew")  # Position the display on the grid

# Function to update the input field when a button is pressed
def button_click(item):
    current = input_text.get()
    input_text.set(current + str(item))

# Function to clear the display
def button_clear():
    input_text.set("")

# Function to calculate the result
def button_equal():
    try:
        result = str(eval(input_text.get()))  # eval will evaluate the string as Python expression
        input_text.set(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")  # Show error message
        input_text.set("")

# Define numeric buttons
button_1 = tk.Button(root, text='1', font = ('Arial', 15), command=lambda: button_click(1), bd=8)
button_2 = tk.Button(root, text='2', font = ('Arial', 15), command=lambda: button_click(2), bd=8)
button_3 = tk.Button(root, text='3', font = ('Arial', 15), command=lambda: button_click(3), bd=8)
button_4 = tk.Button(root, text='4', font = ('Arial', 15), command=lambda: button_click(4), bd=8)
button_5 = tk.Button(root, text='5', font = ('Arial', 15), command=lambda: button_click(5), bd=8)
button_6 = tk.Button(root, text='6', font = ('Arial', 15), command=lambda: button_click(6), bd=8)
button_7 = tk.Button(root, text='7', font = ('Arial', 15), command=lambda: button_click(7), bd=8)
button_8 = tk.Button(root, text='8', font = ('Arial', 15), command=lambda: button_click(8), bd=8)
button_9 = tk.Button(root, text='9', font = ('Arial', 15), command=lambda: button_click(9), bd=8)
button_0 = tk.Button(root, text='0', font = ('Arial', 15), command=lambda: button_click(0), bd=8)

#Define arithmetic Buttons
button_add = tk.Button(root, text='+', font = ('Arial', 20), command=lambda: button_click('+'), bd=8)
button_subtract = tk.Button(root, text='-', font = ('Arial', 20), command=lambda: button_click('-'), bd=8)
button_multiply = tk.Button(root, text='*', font = ('Arial', 20), command=lambda: button_click('*'), bd=8)
button_divide = tk.Button(root, text='/', font = ('Arial', 20), command=lambda: button_click('/'), bd=8)
button_equal = tk.Button(root, text='=', font = ('Arial', 20), command=button_equal, bd=8)
button_clear = tk.Button(root, text='C', font = ('Arial', 20, 'bold'), command=button_clear, bd=8, fg='red')

# Position the buttons on the grid
button_1.grid(row=3, column=0, sticky="nsew")
button_2.grid(row=3, column=1, sticky="nsew")
button_3.grid(row=3, column=2, sticky="nsew")
button_4.grid(row=2, column=0, sticky="nsew")
button_5.grid(row=2, column=1, sticky="nsew")
button_6.grid(row=2, column=2, sticky="nsew")
button_7.grid(row=1, column=0, sticky="nsew")
button_8.grid(row=1, column=1, sticky="nsew")
button_9.grid(row=1, column=2, sticky="nsew")
button_0.grid(row=4, column=1, sticky="nsew")
button_add.grid(row=1, column=3, sticky="nsew")
button_subtract.grid(row=2, column=3, sticky="nsew")
button_multiply.grid(row=3, column=3, sticky="nsew")
button_divide.grid(row=4, column=3, sticky="nsew")
button_equal.grid(row=4, column=2, sticky="nsew")
button_clear.grid(row=4, column=0, sticky="nsew")

# Configure the grid rows and columns to be resizable
for i in range(5):  # There are 5 rows
    root.grid_rowconfigure(i, weight=1)
for j in range(4):  # There are 4 columns
    root.grid_columnconfigure(j, weight=1)

# Main loop
root.mainloop()