# строки и индексация строк

name = 'Nikolay'        # создаём переменную name типа str
print('Hello ' + name)  # печатаем текст и к нему добавляем строковую переменную
print('Hello ' * 5)     # печатаем текст 5 раз
print(name[0])          # выводым первый символ строки
print(name[-2])         # выводим второй символ с конца
print(name[1:3])        # выводим начиная со второго символа до 4 символа
print(name[1:6:2])      # выводим начиная со второго символа до 7 символа c шагом 2
print(name[:3])         # выводим с начала до 4 символа
print(name[3:])         # выводим начиная с 4 символа до конца
print(name[::-1])       # выводим все элементы с конца в обратном порядке

# домашнее задание по уроку №1

print("Lesson 1")       # печатаем название урока
exampe = 'Топинамбур'   # задаём строковую переменную с именем example и значением 'Топинамбур'
print(exampe[0])        # выводим первый символ строки
print(exampe[-1])       # выводим последний символ строки
print(exampe[5:])       # выводим с шестого символа и до конца
print(exampe[::-1])     # выводим строку в обратном порядке
print(exampe[1::2])     # выводим строку начиная со второго символа до конца с шагом 2
