# МНОЖЕСТВА

# Множества – это неупорядоченные наборы уникальных простых объектов. Во множестве не может быть одинаковых объектов.
my_set = set()  # создание пустого множества
my_set.add('book')  # добавление нового элемента в множество

my_list = [1, 1, 1, 2, 2, 3, 1, 1, 5, 5, 4, 6, 6]
set1 = set(my_list)  # превращение списка во множество. Вывод: {1, 2, 3, 4, 5, 6}

countries = {'Бразилия', 'Россия', 'Индия'}
print('Индия' in countries)  # проверка: находится ли объект 'Индия' во множестве countries
print('США' in countries)  # проверка: находится ли объект 'США' во множестве countries
countries_copy = countries.copy()  # копируем множество countries во множество countries_copy
countries_copy.add('Китай')  # добавляем во множество countries_copy объект 'Китая'
# (множество countries остаётся неизменным)
print(countries_copy.issuperset(countries))   # является ли множество countries подмножеством множество countries_copy
# (countries_copy - надмножество)
countries.remove('Россия')  # удаляем объект 'Россия' из множеств countries
print(countries & countries_copy)  # OR countries.intersection(countries_copy) #countries в пересечении c countries_copy
