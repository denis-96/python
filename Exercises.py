# ГЛАВА 1

# №1
# name = 'Denis'
# address = 'Pandurilo 21'
# print(f'Имя: {name}, адрес: {address} ')

# №2
# name = input()
# print('Hello,', name)

# №3
# lenght = float(input('Введите длину (м): '))
# width = float(input('Введите ширину (м): '))
# A = lenght * width
# print(f'Периметр равен {A} м')

# №4
# lenght = float(input('Введите длину (ft): '))
# width = float(input('Введите ширину (ft): '))
# A = (lenght * width) / 43560
# print('Периметр равен %.3f акров' % A)

# №5
# type1 = int(input())
# type2 = int(input())
# s = type1 * 0.10 + type2 * 0.25
# print('%.2f$' %s)

# №6
# price = float(input('Введите сумму заказа: '))
# tax = price * 0.05
# tips = price * 0.18
# total = price + tax + tips
# print('Налог: %.2f$\nЧаевые: %.2f$\nИтог: %.2f$' %(tax, tips, total))

# №7
# n = int(input())
# sm = n * (n + 1) / 2
# print(sm)

# №8
# souvenir = int(input())
# bauble = int(input())
# total_weight = souvenir * 75 + bauble * 112
# print(total_weight)

# №9
# percent = 0.04
# while True:
#     contribution = float(input('Введите сумму: '))
#     years = int(input('Введите количество лет: '))
#     for i in range(1, years + 1):
#         contribution += contribution * percent
#         print(i, 'год: %.2f' % contribution)

# №10
# import math
# a = float(input('Введите первое число: '))
# b = float(input('Введите второе число: '))
# print(math.fsum((a, b)))
# print(math.fabs(a - b))
# print(a * b)
# print(a / b)
# print(math.fmod(a, b))
# print(math.log10(a))
# print(math.pow(a, b))

# №11
# mpg = float(input('Введите потребление топлива: '))
# lpk = (100 * 3.785) / (mpg * 1.609)
# print('%.2f' % lpk)

# №12
# import math
# t1 = math.radians(float(input()))
# g1 = math.radians(float(input()))
# t2 = math.radians(float(input()))
# g2 = math.radians(float(input()))
# distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
# print('%.2f' % distance)

# №13
# cents = int(input())
# monets = (200, 100, 25, 10, 5, 1)
# for i in monets:
#     print(cents // i)
#     cents = cents % i

# №14
# ft = int(input())
# dm = int(input())
# dm = dm + ft * 12
# sm = dm * 2.54
# print(round(sm))

# №15
# ft = float(input())
# print(ft * 12, 'дюймов')
# print(ft / 3, 'ярдов')
# print(ft / 5280, 'миль')

# №16
# import math
# p = math.pi
# r = float(input('Введите радиус: '))
# A = p * (r ** 2)
# V = (4/3) * p * (r ** 3)
# print('%.2f, %.2f' % (A, V))

# №17
# m = float(input('Масса: '))
# dt = int(input('Разница температур: '))
# q = m * 4.186 * dt
# print(q, 'Дж')

# №18
# import math
# p = math.pi
# r = float(input('Введите радиус: '))
# h = float(input('Введите высоту цилиндра: '))
# A = p * (r ** 2)
# V = A * h
# print('%.1f' % V)

# №19
# from math import sqrt
# GRAVITY = 9.8
# d = float(input("Высота отпускания объекта (в метрах): "))
# vf = sqrt(2 * GRAVITY * d)
# print("Объект достигнет земли на скорости %.2f м/с." % vf)

# №20

# №21

# №22

# №23

# №24
# time = input('Введите время: ')
# timelist = time.split(':', maxsplit=3)
# seconds = int(timelist[0]) * 86400 + int(timelist[1]) * 3600 + int(timelist[2]) * 60 + int(timelist[3])
# print(seconds)

# №25
# seconds = int(input('Количество секунд: '))
# days = seconds / 86400
# seconds = seconds % 86400
# hours = seconds / 3600
# seconds = seconds % 3600
# minutes = seconds / 60
# seconds = seconds % 60
# print("%d:%02d:%02d:%02d" % (days, hours, minutes, seconds))

# №26
# from time import asctime
# print(asctime())

# №27
# import math
# year = int(input('Введите год: '))
# a = math.fmod(year, 19)
# b = math.floor(year / 100)
# c = math.fmod(year, 100)
# d = math.floor(b / 4)
# e = math.fmod(b, 4)
# f = math.floor((b + 8) / 25)
# g = math.floor((b - f + 1) / 3)
# h = (19 * a + b - d - g + 15) % 30
# i = math.floor(c / 4)
# k = math.fmod(c, 4)
# l = (32 + 2 * e + 2 * i - h - k) % 7
# m = math.floor((a + 11 * h + 22 * l) / 451)
# month = math.floor((h + l + 7 * m + 114) / 31)
# day = int(((h + l - 7 * m + 114) % 31) + 1)
# print(month, day)

# №28
# height = float(input('Введите свой рост в метрах: '))
# wieght = int(input('Введите свой вес в килограммах: '))
# bmi = wieght / (height ** 2)
# print(bmi)

# №29
# T = int(input('Введите температуру воздуха: '))
# V = float(input('Введите скорость ветра: '))
# WCI = 13.12 + 0.6215 * T - 11.37 * (V ** 0.16) + 0.3965 * T * (V ** 0.16)
# print(WCI)

# №30
# num = input('Введите четырёх значное число число: ')
# amount = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])
# print(amount)

# №31

# №32

# №33
# num = input('Введите три числа: ')
# nums = num.split(sep=' ', maxsplit=2)
# def integer_list(list_name):
#     list2 = []
#     for item in list_name:
#         list2.append(int(item))
#     return list2
#
# nums = integer_list(nums)
# nums.sort()
# for i in nums:
#     print(i, end=', ')

# №34


# ГЛАВА 2

# №35
# num = int(input())
# if num % 2 == 0:
#     print('Чётное')
# else:
#     print('Нечётное')

# №36
# age = int(input())
# if age < 3:
#     if age < 0:
#         print('Неправильный возраст')
#     else:
#         print(age * 10.5)
# elif age > 2:
#     print((age - 2) * 4 + 2 * 10.5)

# №37
# letter = input()
# if letter in 'aeiou':
#     print('Гласная')
# elif letter == 'y':
#     print('И гласная и согласная')
# else:
#     print('Согласная')

# №38
# №39
# №40
# №41
# №42
# №43
# №44
# №45
# №46
# №47
# №48
# №49
# №50
# №51
# №52
# №53
# №54
# №55
# №56
# №57
# №58
# №59
# №60
# №61
# №62
import random
nums = list(range(1, 37)) + [0, '00']
num = random.choice(nums)
print('Выпавший номер:', num)
print('Выигравшая ставка:', num)
if num in range(1, 37):
    if num in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
        print('Красное')
    else:
        print('Чёрное')
    if num % 2 == 0:
        print('Чётное')
    else:
        print('Нечётное')
    if num in range(1, 19):
        print('От 1 до 18')
    else:
        print('От 19 до 36')
