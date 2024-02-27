import tkinter as tk
root=tk.Tk()
root.geometry("500x500")
root.title("My UI")

label_converter=tk.Label(root,text="Temperature Converter: Celcius to Fahrenheit",font=('Arial',10))
label_converter.pack(padx=10,pady=10)

def MyCalculateFunction():
    temperature=float(box_temperature.get())
    result= ((temperature*1.8)+32)

    label_result.config("Farenheit",(temperature,result))

box_temperature=tk.Entry(root)
box_temperature.pack()

button_calculate=tk.Button(root,text="Calculate", command=MyCalculateFunction)
button_calculate.pack()

label_result = tk.Label(root)
label_result.pack()

root.mainloop()

