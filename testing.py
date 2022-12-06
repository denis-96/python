# import pandas
# columns = ['a', 'b', 'c', 'd']
# data = [(20, 21, 23, 24),
#         (25, 26, 27, 28),
#         (29, 30, 31, 32)]
# index = [10, 20, 30]
# df = pandas.DataFrame(data= data, columns= columns, index= index)
# print(df)


# cents = int(input())
# monets = (200, 100, 25, 10, 5, 1)
# for i in monets:
#     print(cents // i)
#     cents = cents % i

# num = input()
# nums = list(num)
# def integer_list(list_name):
#     list2 = []
#     for item in list_name:
#         list2.append(int(item))
#     return list
# for i in sorted(integer_list(nums)):
#     print(i, end=', ')
# print(sum(integer_list(nums)))


# def remove_spaces(string):
#     new_string = ''
#     for letter in string:
#         if letter == ' ':
#             continue
#         new_string += letter
#     return new_string
#
# with open(r'D:\text.txt', 'r') as f:
#     text = f.read()
# print(remove_spaces(text))
# characters = len(remove_spaces(text))
# print(characters)

# mylist = {'a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'g7'}
# print(set(enumerate(mylist)))

# st = 'Print only the words that start with s in this sentence'
# for word in st.split():
#     if word.startswith('s'):
#         print(word)

# lst = [num for num in range(1, 51) if num%3 == 0]
# print(lst)

# st = 'Print every word in this sentence that has an even number of letters'
# for word in st.split():
#     if len(word) % 2 == 0:
#         print(f'Слово {word} имеет чётную длину')

# for num in range(1, 100):
#     if num % 3 == 0 and num % 5 == 0:
#         print(num, 'FizzBuzz')
#     elif num % 3 == 0:
#         print(num, 'Fizz')
#     elif num % 5 == 0:
#         print(num, 'Buzz')
#     else:
#         print(num)

# st = 'Create a list of the first letters of every word in this string'
# letters_lst = [word[0] for word in st.split()]
# print(letters_lst)

# for i in range(35, 63):
#     print(f'№{i}')
# while True:
#     x = input()
#     print('0' <= x <= '9')

# def min_max(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         print(min(a, b))
#     else:
#         print(max(a, b))
#
# def first_letters(string):
#     lst = string.split()
#     return lst[0][0].lower() == lst[1][0].lower()
#
# def makes_twenty(a, b):
#     return  a + b == 20 or a == 20 or b == 20
#
# def register(name):
#     a = name[0:3].capitalize()
#     b = name[3:].capitalize()
#     newname = a + b
#     return newname
#
# def reverse(phrase):
#     return ' '.join(phrase.split()[::-1])
#
# def almost_there(n):
#     return abs(100 - n) <= 10 or abs(200 - n) <= 10
#
# def has_33(lst):
#     return lst.index(3) == lst.index(3, lst.index(3) + 1) - 1
#
# def paper_doll(string):
#     newstring = ''
#     for i in string:
#         newstring += i * 3
#     return newstring
#
#
# def blackjack(a, b, c):
#     if sum((a, b, c)) <= 21:
#         return sum((a, b, c))
#     elif sum((a, b, c)) <= 31 and 11 in (a, b, c):
#         return sum((a, b, c)) - 10
#     else:
#         return 'BUST'
#
# def summer_69(arr):
#     if 6 in arr:
#         return sum(arr) - sum(arr[arr.index(6):arr.index(9) + 1])
#     else:
#         return sum(arr)
#
# def spy_game(nums):
#     zerozeroseven = []
#     for num in nums:
#         if num == 0 or num == 7:
#             zerozeroseven.append(num)
#     return zerozeroseven == [0, 0, 7]
#
# def count_primes(num):
#     counter = 0
#     for number in range(2, num + 1):
#         for n in range(2, number):
#             if number % n == 0:
#                 break
#         else:
#             counter += 1
#     return counter

# import math
# def vol(rad):
#     return (4/3) * math.pi * math.pow(rad, 3)
# print(vol(2))

# def ran_check(num,low,high):
#     if num in range(low, high + 1):
#         return f'{num} is in the range between {low} and {high}'
# print(ran_check(5, 2, 7))

# def up_low(s):
#     up = len(list(filter(lambda letter: letter.isupper(), s)))
#     low = len(list(filter(lambda letter: letter.islower(), s)))
#     print(f'No. of Upper case characters: {up}')
#     print(f'No. of Lower case Characters: {low}')
# up_low('Hello Mr. Rogers, how are you this fine Tuesday?')

# def unique_list(lst): return list(set(lst))
# print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

# def multiply(numbers):
#     result = 1
#     for num in numbers:
#         result *= num
#     return result
# print(multiply([1,2,3,-4]))

# def palindrome(s):
#     s = s.replace(' ', '')
#     return s == s[::-1]
# print(palindrome('helleh '))

# import string
# def ispangram(str1, alphabet=string.ascii_lowercase):
#     return set(str1) & set(alphabet) == set(alphabet)
# print(type(ispangram('grtg')))

# class Dog:
#     def __init__(self, breed, name, spots):
#         self.breed = breed
#         self.name = name
#         self.spots = spots
#
# my_dog = Dog('Huskie', spots=False, name='bob')
# print(my_dog.breed, my_dog.name, my_dog.spots)

# class Music:
#     all_frequencies = {'C': 16.35, 'D': 18.35, 'E': 20.60, 'F': 21.83, 'G': 24.50, 'A': 27.50, 'H': 30.87}
#     def __init__(self, name, octave):
#         self.name = name.upper()
#         self.octave = octave
#         self.frequency = Music.all_frequencies[self.name] * (2 ** self.octave)
#
#     def set_octave(self, new_octave):
#         self.octave = new_octave
#         self.frequency = Music.all_frequencies[self.name] * (2 ** self.octave)
#
#     def set_name(self, new_name):
#         self.name = new_name.upper()
#         self.frequency = Music.all_frequencies[self.name] * (2 ** self.octave)


# class Line:
#
#     def __init__(self, coor1, coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2
#
#     def distance(self):
#         x1 = self.coor1[0]
#         y1 = self.coor1[1]
#         x2, y2 = self.coor2
#         return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#
#     def slope(self):
#         x1, y1 = self.coor1
#         x2, y2 = self.coor2
#         return (y2 - y1) / (x2 - x1)
#
# coordinate1 = (3, 2)
# coordinate2 = (8, 10)
#
# li = Line(coordinate1,coordinate2)
# print(li.distance())
# # 9.433981132056603
# print(li.slope())
# # 1.6

# from math import pi, pow
#
#
# class Cylinder:
#
#     def __init__(self, height=1, radius=1):
#         self.height = height
#         self.radius = radius
#
#     def volume(self):
#         return pi * pow(self.radius, 2) * self.height
#
#     def surface_area(self):
#         return 2 * pi * self.radius * (self.height + self.radius)
#
#
# c = Cylinder(2,3)
# print(c.volume())
# # 56.52
# print(c.surface_area())
# # 94.2

#
# class Account:
#
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, sum_of_money):
#         self.balance += sum_of_money
#         print('Внесение выполнено')
#
#     def withdraw(self, sum_of_money):
#         if sum_of_money <= self.balance:
#             self.balance -= sum_of_money
#             print('Снятие вполнено')
#         else:
#             print('Недостаточно средств')
#
#     def __str__(self):
#         return f'Владелец счёта: {self.owner}\nБаланс счёта: ${self.balance}'
#

# try:
#     for i in ['a', 'b', 'c']:
#         print(i ** 2)
# except TypeError:
#     print('Нельзя умножать строки')
#
# x = 5
# y = 0
# try:
#     z = x/y
# except ZeroDivisionError:
#     print('На ноль делить нельзя!!!')
# finally:
#     print('Обработка исключений выполнена')
#
# def ask():
#     while True:
#         try:
#             number = int(input('Введите число:'))
#         except ValueError:
#             print('Произошла ошибка! Попробуйте снова!')
#             continue
#         else:
#             print(f'Квадрат числа {number} равен {number ** 2}')
#             break
#
# ask()

# name = 1
#
# def wrapper(func):
#     def wrap(name):
#         print('Я робот, а вы кто?')
#         func(name)
#         print('Я рад с вами познакомиться')
#     return wrap
#
# @wrapper
# def func(name):
#     print(f'Здравствуйте {name}')
#
# func(name)

# def gensquares(n):
#     for i in range(n):
#         yield pow(i, 2)
# for x in gensquares:
#     print(x)



# import random
# def rand_num(low,high,n):
#     for i in range(n):
#         yield random.randint(low, high)
#
#
# for num in rand_num(1,10,12):
#     print(num)

#
# def get_fibon(n):
#     array = tuple(gen_fibon(n))
#     return(array[-1])
#
# print(get_fibon(20))
#
# def fib_mod(n, m):
#     a = 0
#     b = 1
#     for i in range(n):
#         a, b = b, (a+b) % (10**5)
#     return a % m
# print(fib_mod(20, 10))

# def gcd(a, b):
#
#     while 1:
#         if a == 0:
#             return b
#         elif b == 0:
#             return a
#         elif a > b:
#             a %= b
#         else:
#             b %= a


# class Counter:
#
#     def start_from(self, start=0):
#         self.value = start
#
#     def increment(self):
#         self.value += 1
#
#     def display(self):
#         print(f'Текущее значение стчётчика = {self.value}')
#
#     def reset(self):
#         self.value = 0


# class Point:
#
#     def set_coordinates(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_distance(self, second_point):
#         if isinstance(second_point, Point):
#             return ((second_point.x - self.x)**2 + (second_point.y - self.y)**2)**0.5
#         else:
#             print('Передана не точка')
#             return None


# class Laptop:
#
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.nodel = model
#         self.price = price
#         self.laptop_name = f'{brand} {model}'

num = int(5)
print(num.__add__(2))