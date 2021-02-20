# Создаем калькулятор

import tkinter as tk
from tkinter import messagebox


def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)


def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)


def calculate():
    value = calc.get()
    if value[-1] in '+-/*':
        value = value + value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание!!!', 'Вы ввели недопустимый символ!')
        calc.insert(0, 0)
    except (ZeroDivisionError):
        messagebox.showinfo('Внимание!!!', 'Вы пытаетесь делить на 0 !')
        calc.insert(0, 0)


def clear():
    calc.delete(0, tk.END)
    calc.insert(0, '0')


def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 13), command=lambda: add_digit(digit))


def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=calculate)


def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=clear)


def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',
                     command=lambda: add_operation(operation))


def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-/*':
        add_operation(event.char)
    elif event.char == '\r' or '=':
        calculate()
    elif event.char == '\x08':
        clear()


win = tk.Tk()
win.geometry(f"240x280+100+200")
win['bg'] = '#33ffe6'
win.title('Калькулятор')
win.bind('<Key>', press_key)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, padx=5, pady=5, stick='we')

make_digit_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)  # первая клавиша в 1 ряд и 0 колонку
make_digit_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)  # вторая клавиша в 1 ряд и 1 колонку
make_digit_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)  # третья клавиша в 1 ряд и 2 колонку
make_digit_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)  # четвертая клавиша в 2 ряд и 0 колонку
make_digit_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)  # пятая клавиша в 2 ряд и 1 колонку
make_digit_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)  # шестая клавиша в 2 ряд и 2 колонку
make_digit_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)  # седьмая клавиша в 3 ряд и 0 колонку
make_digit_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)  # восьмая клавиша в 3 ряд и 1 колонку
make_digit_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)  # девятая клавиша в 3 ряд и 2 колонку
make_digit_button('0').grid(row=4, column=1, stick='wens', padx=5, pady=5)  # десятая клавиша в 4 ряд и 1 колонку

make_calc_button('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_clear_button('C').grid(row=4, column=0, stick='wens', padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_button('/').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=4, column=3, stick='wens', padx=5, pady=5)
# make_operation_button('%').grid(row=4, column=0, stick='wens', padx=5, pady=5)


win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)
win.mainloop()
