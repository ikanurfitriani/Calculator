# Copyright (c) 2024 Ika Nurfitriani

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import tkinter as Calculator

calculation=""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ''
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, 'Error')

def clear_field():
    global  calculation
    calculation = ''
    text_result.delete(1.0, 'end')

root = Calculator.Tk()
# Mengubah ukuran jendela Tkinter menjadi persegi panjang
root.geometry('300x400') 

# Mengubah jenis huruf menjadi 'Helvetica' dan ukurannya menjadi 24
text_result = Calculator.Text(root, height=5, width=16, font=('Helvetica', 24))
text_result.grid(columnspan=5)

btn_1 = Calculator.Button(root, text='1', command=lambda: add_to_calculation(1), width=5, font=('Arial', 14))
btn_1.grid(row=2, column=1 )
btn_2 = Calculator.Button(root, text='2', command=lambda: add_to_calculation(2), width=5, font=('Arial', 14))
btn_2.grid(row=2, column=2 )
btn_3 = Calculator.Button(root, text='3', command=lambda: add_to_calculation(3), width=5, font=('Arial', 14))
btn_3.grid(row=2, column=3 )
btn_4=Calculator.Button(root, text='4', command=lambda: add_to_calculation(4), width=5, font=('Arial', 14))
btn_4.grid(row=3, column=1 )
btn_5 = Calculator.Button(root, text='5', command=lambda: add_to_calculation(5), width=5, font=('Arial', 14))
btn_5.grid(row=3, column=2 )
btn_6 = Calculator.Button(root, text='6', command=lambda: add_to_calculation(6), width=5, font=('Arial', 14))
btn_6.grid(row=3, column=3 )
btn_7 = Calculator.Button(root, text='7', command=lambda: add_to_calculation(7), width=5, font=('Arial', 14))
btn_7.grid(row=4, column=1 )
btn_8 = Calculator.Button(root, text='8', command=lambda: add_to_calculation(8), width=5, font=('Arial', 14))
btn_8.grid(row=4, column=2 )
btn_9 = Calculator.Button(root, text='9', command=lambda: add_to_calculation(9), width=5, font=('Arial', 14))
btn_9.grid(row=4, column=3 )
btn_0 = Calculator.Button(root, text='0', command=lambda: add_to_calculation(0), width=5, font=('Arial', 14))
btn_0.grid(row=5, column=2 )
btn_plus = Calculator.Button(root, text='+', command=lambda: add_to_calculation('+'), width=5, font=('Arial', 14))
btn_plus.grid(row=2, column=4 )
btn_minus = Calculator.Button(root, text='-', command=lambda: add_to_calculation('-'), width=5, font=('Arial', 14))
btn_minus.grid(row=3, column=4 )
btn_mul = Calculator.Button(root, text='x', command=lambda: add_to_calculation('*'), width=5, font=('Arial', 14))
btn_mul.grid(row=4, column=4 )
btn_div = Calculator.Button(root, text=':', command=lambda: add_to_calculation('/'), width=5, font=('Arial', 14))
btn_div.grid(row=5, column=4 )
btn_open = Calculator.Button(root, text='(', command=lambda: add_to_calculation('('), width=5, font=('Arial', 14))
btn_open.grid(row=5, column=1 )
btn_close = Calculator.Button(root, text=')', command=lambda: add_to_calculation(')'), width=5, font=('Arial', 14))
btn_close.grid(row=5, column=3 )
btn_clear = Calculator.Button(root, text='c', command= clear_field, width=11, font=('Arial', 14))
btn_clear.grid(row=6, column=3, columnspan=2 )
btn_equals = Calculator.Button(root, text='=', command=evaluate_calculation, width=11, font=('Arial', 14))
btn_equals.grid(row=6, column=1, columnspan=2 )
root.mainloop()