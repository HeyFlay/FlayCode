import tkinter as tk 
from tkinter import ttk
import customtkinter

calculation = ''
def add_to_calc(symbol):
    global calculation
    calculation += str(symbol)
    label.delete(1.0, 'end')
    label.insert(1.0, calculation)
    
def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        label.delete(1.0, "end")
        label.insert(1.0, calculation)
    except:
        clear_field()
        label.insert(1.0, "Error")
        pass

def clear_field():
    global calculation
    calculation = ""
    label.delete(1.0, "end")
    
    
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
    
app = customtkinter.CTk()
app.geometry('400x600')
app.title("Calulator")

# widgets
label = tk.Text(app, height= 2, width=20, font=('Maven Pro', 56))
button1 = customtkinter.CTkButton(app, text= "1", command= lambda: add_to_calc(1))
button2 = customtkinter.CTkButton(app, text= "2", command= lambda: add_to_calc(2))
button3 = customtkinter.CTkButton(app, text= "3", command= lambda: add_to_calc(3))
button4 = customtkinter.CTkButton(app, text= "4", command= lambda: add_to_calc(4))
button5 = customtkinter.CTkButton(app, text= "5", command= lambda: add_to_calc(5))
button6 = customtkinter.CTkButton(app, text= "6", command= lambda: add_to_calc(6))
button7 = customtkinter.CTkButton(app, text= "7", command= lambda: add_to_calc(7))
button8 = customtkinter.CTkButton(app, text= "8", command= lambda: add_to_calc(8))
button9 = customtkinter.CTkButton(app, text= "9", command= lambda: add_to_calc(9))
button0 = customtkinter.CTkButton(app, text= "0", command= lambda: add_to_calc(0))
button_plus = customtkinter.CTkButton(app, text= "+", command= lambda: add_to_calc('+'))
button_minus = customtkinter.CTkButton(app, text= "-", command= lambda: add_to_calc('-'))
button_mul = customtkinter.CTkButton(app, text= "X", command= lambda: add_to_calc('*'))
button_div = customtkinter.CTkButton(app, text= "/", command= lambda: add_to_calc('/'))
button_clear = customtkinter.CTkButton(app, text= "C", command=clear_field)
button_equals = customtkinter.CTkButton(app, text= "=", command=evaluate_calculation)
open_p = customtkinter.CTkButton(app, text= "(", command= lambda: add_to_calc('('))
close_p = customtkinter.CTkButton(app, text= ")", command= lambda: add_to_calc(')'))
dec = customtkinter.CTkButton(app, text= ".", command= lambda: add_to_calc('.'))



# making grid
app.columnconfigure(0, weight= 1)
app.columnconfigure(1, weight= 1)
app.columnconfigure(2, weight= 1)
app.columnconfigure(3, weight= 1)
app.rowconfigure(0, weight= 1)
app.rowconfigure(1, weight= 1)
app.rowconfigure(2, weight= 1)
app.rowconfigure(3, weight= 1)
app.rowconfigure(4, weight= 1)
app.rowconfigure(5, weight= 1)

# assigning widgets on cols and rows
label.grid(column= 0, row=0, columnspan=4, sticky='nesw')
button1.grid(column=0, row=3, padx=5, pady=5, sticky='nesw')
button2.grid(column= 1, row= 3, padx= 5, pady=5, sticky='nesw')
button3.grid(column= 2, row= 3, padx= 5, pady=5, sticky='nesw')
button4.grid(column= 0, row= 2, padx= 5, pady=5, sticky='nesw')
button5.grid(column= 1, row= 2, padx= 5, pady=5, sticky='nesw')
button6.grid(column= 2, row= 2, padx= 5, pady=5, sticky='nesw')
button7.grid(column= 0, row= 1, padx= 5, pady=5, sticky='nesw')
button8.grid(column= 1, row= 1, padx= 5, pady=5, sticky='nesw')
button9.grid(column= 2, row= 1, padx= 5, pady=5, sticky='nesw')
button0.grid(column=1, row=4, padx=5, pady=5, sticky='nesw')
button_plus.grid(column= 3, row= 4, padx= 5, pady=5, sticky='nesw')
button_minus.grid(column= 3, row= 3, padx= 5, pady=5, sticky='nesw')
button_mul.grid(column= 3, row= 2, padx= 5, pady=5, sticky='nesw')
button_div.grid(column= 3, row= 1, padx= 5, pady=5, sticky='nesw')
button_clear.grid(column= 0, row= 4, padx= 5, pady=5, sticky='nesw')
button_equals.grid(column= 2, row= 4, padx= 5, pady=5, sticky='nesw')
open_p.grid(column= 0, row= 5, padx= 5, pady=5, sticky='nesw')
close_p.grid(column= 1, row= 5, padx= 5, pady=5, sticky='nesw')
dec.grid(column= 2, row= 5, padx= 5, pady=5, sticky='nesw')








# run
app.mainloop()