# ИТЕРАТОРЫ И ГЕНЕРАТОРЫ

# Генераторы позволяют генерировать данные на ходу, без необходимости хранить всё в памяти.
# Функции-генераторы позволяют нам написать функцию, которая возвращает значение,
# и затем продолжает с того места, где остановилась раньше.
# Когда эта функция компилируется, она становится объектом, который поддерживает протокол итераций.
# Это значит, что когда такая функция вызывается в Вашем коде, она не просто возвращает значение и завершает работу.
# Вместо этого, функция-генератор ставит своё выполнение на паузу,
# и возобновляет выполнение с последней точки генерации значений.
# Такая особенность работы называется state suspension.
# При использовании генераторов нет необходимости сразу вычислить всю серию значений.
# Основное отличие синтаксиса - это использование команды yield.

# Функция-генератор, которая возводит числа в куб (степень 3)
def gen_cubes(n):
    for num in range(n):
        yield num**3

for x in gen_cubes(10):
    print(x)

# Пример генератора, который вычисляет числа Фибоначчи:
def gen_fibon(n):
    """
    Generate a Fibonacci sequence up to n
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

for num in gen_fibon(10):
    print(num)

# Пример генератора таблицы умножения
def gen_multiplication_table():
    for a in range(2, 10):
        for b in range(2, 10):
            yield f'{a} x {b} = {a*b}'
        yield ' '

for i in gen_multiplication_table():
    print(i)

# Встроенные функции next() и iter()

# Функция next() позволяет нам получить следующий элемент в последовательность:
def simple_gen():
    for x in range(3):
        yield x

# Assign simple_gen
g = simple_gen()
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 2
# print(next(g)) - ещё одно использование функции next приведёт к ошибке так как мы уже получили все значения

# Функцию iter()

# (вводная часть)
# Cтроки позволяют выполнять итерации:
s = 'hello'
# выполняем итерации по строке
for let in s:
    print(let)
# Но строка сама по себе является итератором! Мы можем это проверить с помощью функции next():
# next(s) - выдаст ошибку - 'str' object is not an iterator

# Cтрока поддерживает итерации, но мы не можем явно выполнять итерации по аналогии с тем,
# как это можно делать для функции-генератора.
# Но это можно сделать с помощью функции iter()!
s_iter = iter(s)
print(next(s_iter))  # h
print(next(s_iter))  # e

# Generator comprehension

# Конструкция:
# (<expression> for <var> in <iterable> if <condition>)
# Эквивалент:
# for <var> in <iterable>:
#     if bool(<condition>):
#         yield <expression>

# Примеры:
even_gen = (i for i in range(100) if i % 2 == 0)
print(list(even_gen)) # выведет все чётные чила от 1 до 100

example_gen = (i/2 for i in [0, 9, 21, 32])
for item in example_gen:
    print(item)  # 0.0  4.5  10.5  16.0

print(tuple((i, i**2, i**3) for i in range(10)))

print(tuple("apple" if i < 3 else "pie" for i in range(6)))
