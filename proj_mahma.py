import tkinter as tk
root=tk.Tk()
root.geometry("500x500")
root.title("My UI")

label_converter=tk.Label(root,text="Temprature Converter: Celcius to Fahrenheit",font=('Arial',10))
label_converter.pack(padx=10,pady=10)

def MyCalculateFunction():
    
    temprature=float(box_temprature.get())
    result=(temprature*1.8)+32.0
  

    label_result.config(text="%f * 1.8%+32.0%=%f"% (temprature, result))


box_temprature=tk.Entry(root)
box_temprature.pack()

button_calculate=tk.Button(root,text="Calculate", command=MyCalculateFunction)
button_calculate.pack()

label_result = tk.Label(root)
label_result.pack()

root.mainloop()

