# Загрузчики: FileSystemLoader, PackageLoader, FunctionLoader и другие

from jinja2 import Environment, FileSystemLoader, FunctionLoader
 
persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0}
]
 
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
 
tm = env.get_template('main.html')  # Template
msg = tm.render(users = persons)
 
print(msg)


# FunctionLoader

def loadTpl(path):
    if path == "index":
        return '''Имя {{u.name}}, возраст {{u.old}}'''
    else:
        return '''Данные: {{u}}'''
    
file_loader = FunctionLoader(loadTpl)
env = Environment(loader=file_loader)
 
tm = env.get_template('index')
msg = tm.render(u = persons[0])
print(msg)