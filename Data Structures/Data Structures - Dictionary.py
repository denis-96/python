# СЛОВАРЬ

# 'ab' - сокращение от address book
ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}
print("Адрес Swaroop'а:", ab['Swaroop'])

# Удаление пары ключ-значение
del ab['Spammer']
print(f'\nВ адресной книге {len(ab)} контакта\n')
for name, address in ab.items():
    print(f'Контакт {name} с адресом {address}')

# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'])

ab.keys()  # ключи словаря ab
ab.values()  # значения ключей словаря ab
ab.items()  # элементы словаря ab

d = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d:   # выведет только ключи списка k1 k2 k3
    print(item, end=' ')
print('')

for item in d.items():  # выведет и ключи и значения ('k1', 1) ('k2', 2) ('k3', 3)
    print(item, end=' ')
print('')

for item in d.values():  # выведет только значения 1 2 3
    print(item, end=' ')
