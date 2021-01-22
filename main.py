from tkinter import *

window=Tk()
window.title("Calculator")
window.geometry("300x330")
window.configure(bg="grey")
window.resizable(False,False)

def btn_click(item):
    global expression
    expression=expression + str(item)
    input_string.set(expression)

def btn_equals():
    try:
        global expression
        result=str(eval(expression))
        input_string.set(result)
        expression = ""
    except:
        input_string.set('Error')
        expression=""

def clear():
    global expression
    expression=""
    input_string.set(expression)

input_string=StringVar()
expression=""

input_frame = Frame(window, width=300, height=50, bd=0, highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)

input_text=Entry(input_frame,textvariable=input_string, state=DISABLED, justify=RIGHT, width=250, font=('arial', 18, 'bold'))
input_text.pack(ipady=10)

button_frame=Frame(window, width=312, height=350, bg="grey")
button_frame.pack()

button_clear=Button(button_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda : clear())
button_clear.grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)

button_division=Button(button_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda : btn_click('/'))
button_division.grid(row = 0, column = 3, padx = 1, pady = 1)

button_7=Button(button_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda : btn_click('7'))
button_7.grid(row = 1, column = 0, padx = 1, pady = 1)

button_8=Button(button_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda : btn_click('8'))
button_8.grid(row = 1, column = 1, padx = 1, pady = 1)

button_9=Button(button_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda : btn_click('9'))
button_9.grid(row = 1, column = 2, padx = 1, pady = 1)

button_multiply=Button(button_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda : btn_click('*'))
button_multiply.grid(row = 1, column = 3, padx = 1, pady = 1)

button_4=Button(button_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda : btn_click('4'))
button_4.grid(row = 2, column = 0, padx = 1, pady = 1)

button_5=Button(button_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda : btn_click('5'))
button_5.grid(row = 2, column = 1, padx = 1, pady = 1)

button_6=Button(button_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda : btn_click('6'))
button_6.grid(row = 2, column = 2, padx = 1, pady = 1)

button_minus=Button(button_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda : btn_click('-'))
button_minus.grid(row = 2, column = 3, padx = 1, pady = 1)

button_1=Button(button_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda : btn_click('1'))
button_1.grid(row = 3, column = 0, padx = 1, pady = 1)

button_2=Button(button_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda : btn_click('2'))
button_2.grid(row = 3, column = 1, padx = 1, pady = 1)

button_3=Button(button_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda : btn_click('3'))
button_3.grid(row = 3, column = 2, padx = 1, pady = 1)

button_addition=Button(button_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda : btn_click('+'))
button_addition.grid(row = 3, column = 3, padx = 1, pady = 1)

button_sign=Button(button_frame, text = "+/-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda : btn_click('-'))
button_sign.grid(row = 4, column = 0, padx = 1, pady = 1)

button_zero=Button(button_frame, text = "0", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda : btn_click('0'))
button_zero.grid(row = 4, column = 1, padx = 1, pady = 1)

button_decimal=Button(button_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda : btn_click('.'))
button_decimal.grid(row = 4, column = 2, padx = 1, pady = 1)

button_equal=Button(button_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda : btn_equals())
button_equal.grid(row = 4, column = 3, padx = 1, pady = 1)

window.mainloop()
