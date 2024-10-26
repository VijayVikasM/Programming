import tkinter as tk

# Conversion functions
def celsius_to_fahrenheit(c):
    return 32 + (9 * c) / 5

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def kelvin_to_celsius(k):
    return k - 273.15

# Update functions for each scale
def update_celsius(val):
    celsius = float(val)
    fahrenheit = celsius_to_fahrenheit(celsius)
    kelvin = celsius_to_kelvin(celsius)
    
    fahrenheit_slider.set(fahrenheit)
    kelvin_slider.set(kelvin)

def update_fahrenheit(val):
    fahrenheit = float(val)
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius_to_kelvin(celsius)
    
    celsius_slider.set(celsius)
    kelvin_slider.set(kelvin)

def update_kelvin(val):
    kelvin = float(val)
    celsius = kelvin_to_celsius(kelvin)
    fahrenheit = celsius_to_fahrenheit(celsius)
    
    celsius_slider.set(celsius)
    fahrenheit_slider.set(fahrenheit)

# Set up the GUI window
root = tk.Tk()
root.title("Thermometer GUI")
root.geometry("300x400")

# Labels for each scale
tk.Label(root, text="Celsius (°C)").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Fahrenheit (°F)").grid(row=0, column=1, padx=10, pady=5)
tk.Label(root, text="Kelvin (°K)").grid(row=0, column=2, padx=10, pady=5)

# Celsius Slider
celsius_slider = tk.Scale(root, from_=-100, to=100, orient="vertical", length=300,
                          command=update_celsius)
celsius_slider.grid(row=1, column=0, padx=10, pady=5)

# Fahrenheit Slider
fahrenheit_slider = tk.Scale(root, from_=-148, to=212, orient="vertical", length=300,
                             command=update_fahrenheit)
fahrenheit_slider.grid(row=1, column=1, padx=10, pady=5)

# Kelvin Slider
kelvin_slider = tk.Scale(root, from_=173.15, to=373.15, orient="vertical", length=300,
                         command=update_kelvin)
kelvin_slider.grid(row=1, column=2, padx=10, pady=5)

# Initialize sliders to a neutral temperature (0°C, 32°F, 273.15K)
celsius_slider.set(0)
fahrenheit_slider.set(celsius_to_fahrenheit(0))
kelvin_slider.set(celsius_to_kelvin(0))

# Run the main loop
root.mainloop()
