# ОБЪЕКТНО - ОРИЕНТИРОВАННОЕ ПРОГРАМИРОВАНИЕ (ООП)

# Вспомним базовые объекты Python
# В Python, любой элемент является объектом. Можно использовать type(), чтобы узнать тип объекта:
print(type(1)) # <class 'int'>
print(type([])) # <class 'list'>
print(type(())) # <class 'tuple'>
print(type({})) # <class 'dict'>

# Как мы можем создавать свои собственные типы объектов?
# Для этого как раз пригодится ключевое слово class

# class

# Объекты пользователя создаются с помощью ключевого слова class.
# Класс - это шаблон, описывающий будущий объект.
# Из классов мы создаем экземпляры (инстансы).
# Экземпляр - это конкретный объект, созданный на основе конкретного класса.
# Например, объект lst, это экземпляр объекта list.
lst = [1, 2, 3]

# Создаем новый тип объекта, под названием Sample
class Sample: # Согласно принятым соглашениям об именовании, имена классов начинаются с заглавной буквы.
    pass
# Экземпляр класса Sample
x = Sample()
print(type(x))
# Внутри класса у нас пока есть только слово pass. Но мы можем определить атрибуты и методы класса.
# Атрибут - это характеристика объекта. Метод - это операция, которую мы можем выполнять над объектом.

# Атрибуты

# Синтаксис создания атрибута следующий:
# self.attribute = something
# Есть специальный метод, который называется __init__()
# Это метод используется для инициализации атрибутов объекта.
class Dog:
    def __init__(self, breed):
        self.breed = breed

sam = Dog(breed='Lab')
frank = Dog(breed='Huskie')

# Разберёмся, что здесь происходит.
# Специальный метод __init__() вызывается автоматически, сразу после создания объекта:
# def __init__(self, breed):
# Каждый атрибут в определении класса начинается со ссылки на экземпляр объекта.
# По соглашению об именовании, он называется self.
# Далее, breed это параметр. Значение передается при инициализации класса. self.breed = breed
# Итак, мы создали два экземпляра класса Dog. У нас два разных типа породы - breed.
# Мы можем получить значения атрибутов вот так:
print(sam.breed) # Lab
print(frank.breed) # Huskie
# Обратите внимание, что здесь нет скобок после breed; это потому, что атрибуты не принимают на вход никаких параметров.

# Атрибуты класса (class object attributes)
# Эти атрибуты одни и те же для всех экземпляров класса.
# Создадим атрибут species (вид) для класса Dog.
# Собаки, вне зависимости от породы, имени и других атрибутов, всегда являются млекопитающими (mammal).
class Dog1:
    # Class Object Attribute
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
# Атрибуты класса объекта определяются вне методов класса. По соглашению, мы помещаем их в начале, перед методом init.

# Методы

# Методы - это функции, определённые внутри класса. Они используются для выполнения операций с атрибутами объектов.
# Методы можно представить себе как функции, которые работают с объектом,
# ссылаясь на этот объект с помощью параметра self.

class Circle:
    pi = 3.14  # атрибут класса

    # Circle инициализируется, используя радиус (по умолчанию 1)
    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    # Метод для указания радиуса
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # Метод для определения длины окружности
    def getCircumference(self):
        return self.radius * self.pi * 2

c = Circle(5)
print('Радиус:', c.radius)
print('Площадь:', c.area)
print('Длина окружности:', c.getCircumference())

# В методе __init__ выше, чтобы вычислить атрибут area, мы вызываем Circle.pi.
# Поскольку в объекте ещё нет своего атрибута .pi, мы вызываем атрибут класса объекта id.
# Однако в методе setRadius мы уже работаем с существующим объектом класса Circle,
# в котором есть свой атрибут pi. Так что здесь мы можем использовать или Circle.pi, или self.pi.

# Наследование (Inheritance)

# Наследование - это способ создавать новые классы на основе уже существующих классов.
# Новые классы называются производными (derived) классами, а те классы,
# на основе которых они создаются, называются базовыми классами.
# Важные преимущества наследования - это переиспользование существующего кода, а также уменьшение сложности программ.
# Производные (дочерние) классы переопределяют и/или расширяют функциональность базовых (родительских) классов.

class Animal:
    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog2(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        print("Dog")

    def bark(self):
        print("Woof!")

d = Dog2()
d.who_am_i()
d.eat()
d.bark()

# В этом примере у нас есть два класса: Animal и Dog. Animal является базовым классом, а Dog производным классом.
# Производный класс наследует функциональность базового класса
# >>> это показано с помощью метода eat().
# Производный класс меняет поведение базового класса.
# >>> это показано с помощью метода who_am_i().
# И наконец, производный класс расширяет функциональность базового класса, добавляя новый метод bark().

# Полиморфизм (Polymorphism)

# Полиморфизм - это когда различные объекты класса могут иметь одно и то же название метода,
# и эти методы можно вызывать из одной и той же точки кода для различных объектов.

class Dog3:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says Woof!'


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says Meow!'

niko = Dog3('Niko')
felix = Cat('Felix')
print(niko.speak())
print(felix.speak())

# Здесь у нас есть классы Dog и Cat, и каждый из них имеет метод .speak().
# При вызове, метод для каждого объекта .speak() возвращает результат, специфичный для этого объекта.

# Есть разные способы продемонстрировать полиморфизм - с помощью цикла for и с помощью функции
for pet in (niko, felix):
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)

# Более общей практикой является использование абстрактных классов и наследования.
# Абстрактный класс - это такой класс, для которого никогда не создаются экземпляры.

class Animal1:
    def __init__(self, name):  # конструктор класса
        self.name = name

    def speak(self):  # абстрактный метод
        raise NotImplementedError("Subclass must implement abstract method")

class Dog4(Animal1):

    def speak(self):
        return self.name + ' says Woof!'

class Cat1(Animal1):

    def speak(self):
        return self.name + ' says Meow!'

fido = Dog4('Fido')
isis = Cat1('Isis')
print(fido.speak())
print(isis.speak())

# Примеры полиморфизма из реальной жизни:
# >>> открытие разных типов файлов - для отображения файлов Word, pdf и Excel нужны разные приложения
# >>> сложение разных объектов - оператор + выполняет и сложение чисел, и конкатенацию строк

# Специальные методы

# Классы в Python могут выполнять определенные операции с помощью специальных методов.
# Эти методы вызываются не напрямую, а с помощью специального синтаксиса языка Python.
class Book:
    def __init__(self, title, author, pages):
        print("Создаём книгу")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Название: %s, Автор: %s, Кол-во страниц: %s" %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("Книга удалена")

book = Book("Руководство по Python", "Влад", 159)

#Special Methods
print(book)
print(len(book))
del book

# Методы __init__(), __str__(), __len__() and __del__()
# Эти специальные методы определяются с помощью символов нижнего подчёркивания.
# Они позволяют использовать определенные функции Python для объектов, которые создаются на основе нашего класса.
