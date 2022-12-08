# ВВОД - ВЫВОД ДЛЯ ФАЙЛОВ
#Открываем файл
file = open('myfile.txt', encoding='utf-8') #если файл в той же папке где и файл с кодом, просто указываем имя файла
#file = open(r'C:\Users\barga\Desktop\Python\Python projects\PythonAbstracts\myfile.txt') #если файл в другом месте, указываем путь

print(file.read()) #выведет содержание файла
#повторное использование этой команды ничего не выведет
#потому что указатель после чтения остался в конце файла
#чтобы вернуть указатель в начало нужна следующая команда:
file.seek(0) #(seek - искать)

text = file.readlines() #читатет файл, создаёт список и каждую строку из файла записывает как отдельный элемент списка
file.close() #закрываем файл

with open('myfile.txt', encoding='utf-8') as myfile: #автоматически закроет файл после выполнения блока с отступом
    contents = myfile.read()

#Запись в файл
with open('myfile.txt', mode='r', encoding='utf-8') as myfile:
    contents = myfile.read()
#аргумент 'mode='  - управление доступом к файлу
#mode= 'r' - только чтение (read)
#mode= 'w' - только запись (write) (перезаписывает файл или создаёт новый)
#mode= 'a' - только добавление (append) к существующему файлу
#mode= 'r+' - чтение и запись
#mode= 'w+' - запись и чтение (перезаписывает файл или создаёт новый)

with open('mynewfile.txt', mode='w', encoding='utf-8') as f:
    f.write('One!\nTwo!\nThree!\nOne Two Three!!!')
with open('mynewfile.txt', mode='a', encoding='utf-8') as f:
    f.write('\nОдин Два Три!!!')
with open('mynewfile.txt', mode='r', encoding='utf-8') as f:
    print(f.read())

#Создади новый файл и прочитаем его
with open('newnewnew.txt', mode='w+', encoding='utf-8') as f:
    f.write('Привет\nЭто новый файл')
    f.seek(0)
    print(f.read())
