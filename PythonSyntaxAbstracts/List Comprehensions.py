# ГЕНЕРАТОРЫ СПИСКОВ

# Использование нового синтаксиса для создания списка (list comprehension)
# letter - переменная с которой будут производиться манипуляции (название может быть любым)
mylist = [letter for letter in 'Hello world']
# for letter in 'Hello world' - цикл при каждой итерации которого переменная num принимает значение одной буквы из строки 'Hello world'
# перед циклом записывается то что нужно добавлять в список при каждой итерации, то есть letter
print(mylist)

# Нерациональный вариант создания списка (но результат одинаковый)
mylist1 = []
for num in 'Hello world':
    mylist1.append(num)
print(mylist1)

# Более сложные примеры использования нового синтаксиса
# во время каждой итерации цикла, переменная num будет по очереди принимать значения промежутка от 1 до 11
newlist = [num**2 for num in range(1, 11)]
# потом значение переменной будет возводиться в квадрат и добавляться в списко
print(newlist)

# добавляем условный оператор if
newlist1 = [num for num in range(1, 11) if num % 2 == 0]
# если num делится на 2 без остатка, то добавить его список
# ещё пример: newlist1 = [num ** 2 for num in range(1, 11) if num % 2 == 0]
# если num делится на 2 без остатка, то возвести его в квадрат и добавить его список
print(newlist1)

# перевод градусов цельсия в фаренгейты
celsius = [0, 5, 7, 10, 15, 22.5]
fahrenheit = [(9/5) * temp + 32 for temp in celsius]
# производит манипуляции с каждым значением из списка celsius и добавляет значения список fahrenheit
print(fahrenheit)

# добавляем оператор else
example_list = [num if num % 2 == 0 else 'ODD' for num in range(1, 11)]
# if и else в этом случае уже ставятся перед циклом, а не после
print(example_list)

# вложенный цикл
example_list1 = [x * y for x in [2, 4, 6] for y in [10, 20, 30]]
print(example_list1)

# второй вариант
example_list1 = []
for x in [2, 4, 6]:
    for y in [10, 20, 30]:
        example_list1.append(x * y)
# результат один и тот же: [20, 40, 60, 40, 80, 120, 60, 120, 180]

# вложенный генератор списков
lst = [x**2 for x in [x**2 for x in range(11)]]
print(lst)
