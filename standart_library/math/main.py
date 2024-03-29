# МОДУЛЬ MATH - Mathematical functions
import math
X = 4
Y = 2

math.ceil(X)   # – округление до ближайшего большего числа.
math.floor(X)  # - округление вниз.
math.trunc(X)  # - усекает значение X до целого.

math.fmod(X, Y)  # - остаток от деления X на Y.

math.fabs(X)  # - модуль X.

# - возвращает число, имеющее модуль такой же, как и у числа X, а знак - как у числа Y.
math.copysign(X, Y)

# - возвращает дробную и целую часть числа X. Оба числа имеют тот же знак, что и X.
math.modf(X)

math.pow(X, Y)  # - X в степени Y.
math.sqrt(X)  # - квадратный корень из X.

# Эквивалент встроенной функции sum(), но math.fsum() более точна для чисел с плавающей точкой.
sequence = (1, 0.98, 1.26, 10, 235.45)
# - сумма всех членов sequence (sequence может быть список, множесто, кортеж).
math.fsum(sequence)

# - вычисляет гипотенузу треугольника с катетами X и Y (math.sqrt(x * x + y * y))
math.hypot(X, Y)

# Число pi и e
pi = math.pi  # - pi = 3,1415926...
e = math.e  # - e = 2,718281...

# Является ли X ...
math.isfinite(X)  # - является ли X числом.
math.isinf(X)  # - является ли X бесконечностью.
math.isnan(X)  # - является ли X NaN (Not a Number - не число).

# Логарифмы
base = 5

# - логарифм X по основанию base. Если base не указан, вычисляется натуральный логарифм.
math.log(X, base)

# - натуральный логарифм (1 + X). При X → 0 точнее, чем math.log(1+X).
math.log1p(X)

math.log10(X)  # - логарифм X по основанию 10.
math.log2(X)  # - логарифм X по основанию 2.

# Тригонометрия
math.cos(X)  # - косинус X (X указывается в радианах).
math.sin(X)  # - синус X (X указывается в радианах).
math.tan(X)  # - тангенс X (X указывается в радианах).
