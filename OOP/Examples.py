class Counter:

    def start_from(self, start=0):
        self.value = start

    def increment(self):
        self.value += 1

    def display(self):
        print(f'Текущее значение стчётчика = {self.value}')

    def reset(self):
        self.value = 0


class Point:

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, second_point):
        if isinstance(second_point, Point):
            return ((second_point.x - self.x)**2 + (second_point.y - self.y)**2)**0.5
        else:
            print('Передана не точка')
            return None


class Laptop:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.nodel = model
        self.price = price
        self.laptop_name = f'{brand} {model}'


class SoccerPlayer:

    def __init__(self, name, surname, goals=0, assists=0):
        self.name = name
        self.surname = surname
        self.goals = goals
        self.assists = assists

    def score(self, goals=1):
        self.goals += goals

    def make_assist(self, assists=1):
        self.assists += assists

    def statistics(self):
        print(f'{self.name} {self.surname} - голы: {self.goals}, передачи: {self.assists}')


class Zebra:

    stripes = 1

    def which_stripe(self):
        if self.stripes % 2 != 0:
            print(f'Полоска белая')
        else:
            print(f'Полоска черная')
        self.stripes += 1


class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False


# Практика. Класс Point(x, y)
class Point:

    list_points = []

    def __init__(self, x=0, y=0):
        self.move_to(x, y)
        Point.list_points.append(self.__str__())

    def __str__(self):
        return self.x, self.y

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def go_home(self):
        self.move_to(0, 0)

    def print_poit(self):
        print(f'Точка с координатами ({self.x}, {self.y})')

    def calc_distance(self, second_point):
        if isinstance(second_point, Point):
            print(((second_point.x - self.x)**2 + (second_point.y - self.y)**2)**0.5)
        else:
            print('Передана не точка')


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'


class Stack:

    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if len(self.values) > 0:
            value = self.values[-1]
            self.values.remove(value)
            return value
        else:
            print('Empty Stack')
        # if len(self.values) > 0:
        #     return self.values.pop(-1)
        # else:
        #     print('Empty Stack')

    def peek(self):
        if len(self.values) > 0:
            return self.values[-1]
        else:
            print('Empty Stack')

    def is_empty(self):
        return self.values == []

    def size(self):
        size = 0
        for _ in self.values:
            size += 1
        return size


class Student:

    def __init__(self, name, age, branch):
        self.__name = name
        self.__age = age
        self.__branch = branch

    def __display_details(self):
        print(f'Имя: {self.__name}\nВозраст: {self.__age}\nНаправление: {self.__branch}')

    def access_private_method(self):
        self.__display_details()


