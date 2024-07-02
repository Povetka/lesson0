import tkinter as tk

def add():
    """отвечает за сложение,
    срабатывает при нажатии на конопку"""
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def get_values():
    """отвечает за сбор инфы с полей"""
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(value):
    """отвечает за очистку поля вывода и вывод результата"""
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

def sub():
    """отвечает за вычитание"""
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def div():
    """отвечает за деление"""
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

def mul():
    """отвечает за умножение"""
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


window = tk.Tk()
window.title('Калькулятор')
window.geometry("350x350")
window.resizable(False, False)

button_add = tk.Button(window, text='+', width=2, height=2, command=add)
button_add.place(x=100, y=200)
button_sub = tk.Button(window, text="-", width=2, height=2, command=sub)
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, text="*", width=2, height=2, command=mul)
button_mul.place(x=200, y=200)
button_div = tk.Button(window, text="/", width=2, height=2, command=div)
button_div.place(x=250, y=200)
number1_entry = tk.Entry(window, width=28)
number1_entry.place(x=100, y=75)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=300)
number1 = tk.Label(window, text="Введите первое число:")
number1.place(x=100, y=50)
number2 = tk.Label(window, text="Введите второе число:")
number2.place(x=100, y=125)
answer = tk.Label(window, text="Ответ:")
answer.place(x=100, y=275)
window.mainloop()
