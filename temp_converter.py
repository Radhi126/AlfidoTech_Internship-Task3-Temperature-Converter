from tkinter import *

def c_to_f():
    c = float(entry.get())
    f = (c * 9/5) + 32
    result.config(text=f"{c} °C = {f:.2f} °F")

def c_to_k():
    c = float(entry.get())
    k = c + 273.15
    result.config(text=f"{c} °C = {k:.2f} K")

def f_to_c():
    f = float(entry.get())
    c = (f - 32) * 5/9
    result.config(text=f"{f} °F = {c:.2f} °C")

def f_to_k():
    f = float(entry.get())
    k = (f - 32) * 5/9 + 273.15
    result.config(text=f"{f} °F = {k:.2f} K")

def k_to_c():
    k = float(entry.get())
    c = k - 273.15
    result.config(text=f"{k} K = {c:.2f} °C")

def k_to_f():
    k = float(entry.get())
    f = (k - 273.15) * 9/5 + 32
    result.config(text=f"{k} K = {f:.2f} °F")

# Main window
window = Tk()
window.title("Temperature Converter")
window.geometry("400x350")

Label(window, text="Enter Temperature:", font=("Arial", 12)).pack(pady=5)
entry = Entry(window, font=("Arial", 12), width=12, justify="center")
entry.pack(pady=5)

# Buttons for 6 conversions
Button(window, text="Celsius → Fahrenheit", command=c_to_f, width=25).pack(pady=3)
Button(window, text="Celsius → Kelvin", command=c_to_k, width=25).pack(pady=3)
Button(window, text="Fahrenheit → Celsius", command=f_to_c, width=25).pack(pady=3)
Button(window, text="Fahrenheit → Kelvin", command=f_to_k, width=25).pack(pady=3)
Button(window, text="Kelvin → Celsius", command=k_to_c, width=25).pack(pady=3)
Button(window, text="Kelvin → Fahrenheit", command=k_to_f, width=25).pack(pady=3)

# Result label
result = Label(window, text="", font=("Arial", 14, "bold"), fg="blue")
result.pack(pady=15)

window.mainloop()
