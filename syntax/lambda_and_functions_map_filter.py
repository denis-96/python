# ФУНКЦИЯ MAP


# Функция map позволяет Вам сделать "маппинг" между функцией и итерируемым объектом.
# То есть, Вы можете запустить одну и ту же функцию для любого элемента в итерируемом объекте, например в списке. Например:

def square(num):  # создаём функцию
    """
    Square
    """
    return num**2

my_nums = [1, 2, 3, 4, 5]  # задаём список

# Используем map для того, чтобы применить функцию square для каждого элемента в списке.
# Чтобы получить результаты, либо выполняйте итерации по map() c помощью цикла
# либо просто сделайте приведение к списку
# записываем каждое значение генерируемое функцией map в список и выводим этот список

print(list(map(square, my_nums)))
# вывод: [1, 4, 9, 16, 25]
for item in map(square, my_nums):
    print(item)


# функции могут быть сложнее:

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]


mynames = ['John', 'Cindy', 'Sarah', 'Kelly', 'Mike']
print(list(map(splicer, mynames)))

# вывод: ['even', 'C', 'S', 'K', 'even']
# Важно: чтобы использовать map() функция должна принимать параметр на вход и возвращать какое-то значение


# ФУНКЦИЯ FILTER

# Похожа на map(). Тоже применяет функцию для каждого элемента списка
# Но filter() возвращаёт тот или иной элемент исходного списка,
# только если функция которую нужно применить к списку вернёт True для этого элемента.
# То есть, мы отфильтровываем элементы с помощью функции, которая возвращает либо True, либо False.
# Эта функция и итерируемый объект передаются в функцию filter, и Вы получаете только те результаты,
# которые вернут True, если их передать в указанную функцию.

# Важно: функция обязательно должна возвращать True либо False
def check_even(num):
    return num % 2 == 0

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# И опять таки, чтобы получить результаты нужно либо использовать циклы, либо привести к списку
print(list(filter(check_even, nums)))
# вывод: [0, 2, 4, 6, 8, 10]


# ВЫРАЖЕНИЯ LAMBDA

# Выражения lambda позволяют нам создавать "анонимные" функции.
# По сути это означает, что мы можем создавать функции на лету,
# без необходимости создавать функцию обычным способом с помощью def.

# Объекты-функции, которые возвращают выражения lambda, работают точно так же,
# как и функции, созданные с помощью def.
# Но есть ключевое отличие, которое делает lambda полезными в определенных случаях:
# >   содержимое lambda - это единое выражение, а не набор команд.

#     Содержимое lambda похоже на то, что мы можем поместить в команде return для def.
#     Мы можем указать результат в виде выражения, вместо того чтобы явно вернуть результат.
#     Поскольку мы ограничены выражением, lambda обладает меньшими возможностями, чем def.
#     Так мы можем только уменьшить вложенность программ.
#     Lambda предназначены для реализации простых функций, а def реализуют более сложные задачи.

# Создадим обычную функцию с помощью def
# def square(num):
#     return num**2
# Запишем её в одной строке
# def square(num): return num ** 2

# Теперь превратим эту функцию в lambda функцию:
# убираем слово def и название заменяем на lambda, также справа убираем return
# lambda num: num ** 2

# lambda выражение удобно использовать в сочетании с другими функциями, такими как map() и filter()
example1 = list(map(lambda num: num ** 2, my_nums))
print(example1)
example2 = list(filter(lambda n: n % 2 == 0, nums))
print(example2)
# Ещё примеры:
# Выражение Lambda, чтобы получить первый символ строки:
# lambda s: s[0]
print(list(map(lambda s: s[0], ['John', 'Cindy', 'Sarah', 'Kelly', 'Mike'])))
# Выражение Lambda для инверсии строки:
# lambda s: s[::-1]
print(
    list(map(lambda s: s[::-1], ['John', 'Cindy', 'Sarah', 'Kelly', 'Mike'])))
# Также можно передать несколько параметров в функцию lambda
# lambda x,y : x + y
print(list(map(lambda x, y: x + y, [1, 2, 3], [2, 4, 6])))
