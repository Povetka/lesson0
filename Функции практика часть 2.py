import tkinter as tk # 1 import tkinter – импортируем библиотеку графического дизайна
# as tk – обращаться будем к ней так.

# нужно созддать графическое окно и наполнить его интерфейсом

window = tk.Tk()  # для создания окна, созд переменную, берем библиотеку и используем от туда класс .Tk()
window.title('Калькулятор') # меняем название окна методом .title
window.geometry("350x350") # размер окна
window.resizable(False, False) # для того чтобы нельзя было изменить размер окна
# тк из-за .place при изменении размера будет выглядеть не ок

button_add = tk.Button(window, text='+', width=2, height=2) # создание виджета. Кнопка.
# width= ширина кнопки, height= высота
button_add.place(x=100, y=200) # размещение элемента в окне.
# Отсчет с левого верхнего угла. Слева на право увеличиваем х
# Сверху вниз увеличиваем у
# (вообще, еще можно в процентном соотношении координаты указывать, но нам пока не показали как)
# есть 3 способа размещать элем на экране метод плейс, пак, грид
# чтобы изучить их подробнее, можно зажать контрл и нажать на tkinter
button_sub = tk.Button(window, text="-", width=2, height=2)
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, text="*", width=2, height=2)
button_mul.place(x=200, y=200)
button_div = tk.Button(window, text="/", width=2, height=2)
button_div.place(x=250, y=200)
number1_entry = tk.Entry(window, width=28) # .Entry создание однострочного поля для ввода текста
number1_entry.place(x=100, y=75)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=300)
number1 = tk.Label(window, text="Введите первое число:") # .Label для использования надписей
number1.place(x=100, y=50)
number2 = tk.Label(window, text="Введите второе число:")
number2.place(x=100, y=125)
answer = tk.Label(window, text="Ответ:")
answer.place(x=100, y=275)
# работа с внешним видом окончена
window.mainloop() # запуск цикла обновления событий .mainloop() обновляет инфу происходящую на экране
# весь код отвечающий за наполнение окна пишем между строчками window = tk.Tk() // window.mainloop()