from jinja2 import Template

# Использование {{ }} в шаблонах

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_name(self):
#         return self.name
    
#     def get_age(self):
#         return self.age
    
    
# per = Person('Denis', 16)

per = {'name': 'Denis', 'age': 16}

# Двойных фигурных скобках можно писать любое выражение Python
tm = Template('My name is {{ p.name }} and I am {{ p.age }} y.o')
# Или так
# tm = Template('My name is {{ p["name"] }} and I am {{ p["age"] }} y.o')

msg = tm.render(p=per)

print(msg)