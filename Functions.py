'''
Функции – это многократно используемые фрагменты программы.
Они позволяют дать имя определённому блоку команд с тем,
чтобы впоследствии запускать этот блок по указанному имени
в любом месте программы сколь угодно много раз.
'''
def say_hello(): # def (зарезервированное слово для создания функции), имя функции, в скобках параметры функции, необходимые для работы функции.
    """
    Function that says hello
    """
    print('Привет, Мир!') # блок, принадлежащий функции
# Конец функции
say_hello() # вызов функции

# ПАРАМЕТРЫ ФУНКЦИЙ
def print_max(a, b):
    """
    Function that prints max
    """
    if a > b:
        print(a, 'больше', b)
    elif a == b:
        print(a, 'равно', b)
    else:
        print(b, 'больше', a)
print_max(3, 4) # прямая передача значений
X = 5
Y = 7
print_max(X, Y) # передача переменных в качестве аргументов

# ЛОКАЛЬНЫЕ ПЕРЕМЕННЫЕ
# При объявлении переменных внутри определения функции,
# они никоим образом не связаны с другими переменными с таким же именем за пределами функции.
x = 50
def func(x):
    """
    A function
    """
    print('x равен', x)
    x = 2
    print('Локальный x равен', x)
func(x)
print('Глобальный x равен', x)

# Зарезервированое слово 'global'
x = 50
def func1():
    """
    Also a function
    """
    global x
    print('x равно', x)
    x = 2
    print('Заменяем глобальное значение x на', x)
func1()
print('Значение x составляет', x)

# Зарезервированное слово nonlocal
# Область видимости, которая представляет собой нечто среднее между первыми двумя.
# Нелокальные области видимости встречаются, когда вы определяете функции внутри функций
def func_outer():
    """
    Function outer
    """
    x = 2
    print('x равно', x)
    def func_inner():
        nonlocal x
        x = 5
    func_inner()
    print('Локальное x сменилось на', x)
func_outer()

# ЗНАЧЕНИЯ АРГУМЕНТОВ ПО УМОЛЧАНИЮ
def say(message, times = 1): # message - обязательный аргумент, times - необязательный (если он не введён его значение равно 1)
    """
    Function that prints max
    """
    # Важно: сначала вводить обязательные аргументы
    print(message * times)
say('Привет')
say('Мир', 5)

# КЛЮЧЕВЫЕ АРГУМЕНТЫ
# Если имеется некоторая функция с большим числом параметров,
# и при её вызове требуется указать только некоторые из них,
# значения этих параметров могут задаваться по их имени – это называется ключевые параметры.
# В этом случае для передачи аргументов функции используется имя (ключ) вместо позиции
# (как было до сих пор).
def func2(a, b=5, c=10):
    """
    Function that prints max
    """
    print('a равно', a, ', b равно', b, ', а c равно', c)
func2(3, 7)
func2(25, c=24)
func2(c=50, a=100)

# ОПЕРАТОР «return»
# Оператор return используется для возврата из функции, т.е. для прекращения её работы
# и выхода из неё. При этом можно также вернуть некоторое значение из функции.
def maximum(x, y):
    """
    Function that returns max value
    """
    if x > y:
        return x
    elif x == y:
        return 'Числа равны.'
    else:
        return y
print(maximum(2, 3))

# Строки документации (docstrings)
def print_max_docs(x, y):
    '''
    Выводит максимальное из двух чисел.
    Оба значения должны быть целыми числами.
    '''
    x = int(x) # конвертируем в целые, если возможно
    y = int(y)
    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')
print_max_docs(3, 5)
print(print_max_docs.__doc__)

# *args и **kwargs (arguments и key word arguments)
# позволяют передавать в функцию произвольное количество параметров (аргументов)
# *args позволяет пользователю передавать произвольное количество ПОЗИЦИОННЫХ параметров
def myfunc(*args):  # все введённые пользователем аргументы функции записываются в кортеж
    """
    Function named 'myfunc'
    """
    return sum(args) # далее можно выполнять различные манипуляции с этим кортежем
    # (например посчитать их сумму)
print(myfunc(1, 6, 7, 3, 8, 1)) # вывод: 26

# **kwargs позволяет пользователю передавать произвольное количество ИМЕННОВАНЫХ параметров
def myfunc2(**kwargs): # все введённые пользователем аргументы функции записываются в словарь
    """
    Function named 'myfunc'
    """
    # список kwargs будет равен: {'fruits': ('apple', 'banana', 'orange', 'peach'),
    #                             'vegetables': ('tomato', 'potato', 'garlic', 'carrot')}
    print('Введённые значения:')
    for key in kwargs:
        print(f'{key} - {kwargs[key]}')

myfunc2(fruits= ('apple', 'banana', 'orange', 'peach'), 
        vegetables= ('tomato', 'potato', 'garlic', 'carrot'))
# вывод:
# Введённые значения:
# fruits - ('apple', 'banana', 'orange', 'peach')
# vegetables - ('tomato', 'potato', 'garlic', 'carrot')

# *args и **kwargs можно использовать вместе:
def args_n_kwargs(*args, **kwargs):
    """
    Function named 'args_n_kwargs'
    """
    print(args)
    print(kwargs)
args_n_kwargs('one', 'two', 'three', fruit='orange', food='egg', animal='dog')
# Важно: нельзя при вводе перемешивать параметры между собой
# args_n_kwargs('one', fruit='orange', 'three', food='egg', 'two', animal='dog')   -   так делать нельзя!!!

def myfunc3(*args, **kwargs):
    """
    Function named 'myfunc3'
    """
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
myfunc3('eggs', 'spam', fruit='cherries', juice='orange')
