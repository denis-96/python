# Public, protected, private attr and methods

class BankAccount:

    # Аттрибуты:
    def __init__(self, name, balance, passport):
        # Создание публичных аттрибутов:
        # self.name = name
        # self.balance = balance
        # self.passport = passport

        # Создание защищённых атрибутов:
        # self._name = name
        # self._balance = balance
        # self._passport = passport
        # Защищённые атрибуты можно использовать вне касса, но не нужно!

        # Создание приватных аттрибутов:
        self.__name = name
        self.__balance = balance
        self.__passport = passport
        # Этими аттрибутами можно пользоваться только внутри класса


    # Методы:
    # Публичный метод:
    def print_private_data(self):
        print(self.__name, self.__balance, self.__passport)

    # Приватный метод:
    def __print_private_data(self):
        print(self.__name, self.__balance, self.__passport)


acc1 = BankAccount('Bob', 1000, '34767145')
acc1.print_private_data()
# Выдаст ошибку:
# print(acc1.__name)
# print(acc1.__balance)
# print(acc1.__passport)

# Но всё-таки способ получить доступ к приватным методам и аттрибутам есть:
print(acc1._BankAccount__name)
acc1._BankAccount__print_private_data()
