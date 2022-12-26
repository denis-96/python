# Моносостояние для всех экземпляров класса

class Cat:

    __shared_state = {
        'breed': 'pers',
        'color': 'black'
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_state

d = Cat()
g = Cat()
d.breed = 'siam'  # атрибут breed изменится во всех экземплярах класса, а не только в d
d.name = 'Bob'  # ситуация аналогичная, атрибут name добавится во все экземпляры класса
print(d.__dict__)
print(g.__dict__)