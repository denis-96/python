# Match/case construction

# match <variable>:
#     case <template_1>:
#         operators
#     case <tamplate_n>:
#         operators
#     case _:
#         else (default)


# Work with strings  integers, floatings and booleans

cmd = 'top'
match cmd:
    case 'top':  # проверка на соотвествие одной константе
        print('вверх')
    case 'left' | 'right':  # проверка на соотвествие нескольким константам
        print('влево или вправо')
    case _:  # wildcard (подстановочный знак), обработка всех остальных значений
        print('другое')


cmd1 = 8.1
match cmd1:
    # Сначала частные шаблоны, потом более общие
    case str() as command:  # or str(command)
        print(f'String {command}')
    case bool() as command:
        print(f'Boolean {command}')        
    case int() | float() as command if 0 <= command <= 9:  # IF - guard
        print(f'Integer or floating {command}')
    case command:
        print(f'команда: {command}')



# Work with tuples and lists

cmd_tuple = ('Балакирев С.М.', 'Python', 2000.78)
match cmd_tuple:
    # This template will work with tuples and lists
    case (str() as author, str(title), float() | int() as price, *_) if len(cmd_tuple) < 6:  # tuple unpacking 
        # if number of tuple elements will be bigger or smaller than number of specified variables, the template will not work
        print(f'Кортеж: {author}, {title}, {price}')
    case _:
        print('непонятный формат данных')
        

cmd_list1 = ['Балакирев С.М.', 'Python', 2000.78]
cmd_list2 = [1, 'Балакирев С.М.', 'Python', 2000.78, 2022]
match cmd_list1:
    case tuple():
        print("Неверный формат данных кортеж")
    
    # Short way
    case [author, title, price] | [_, author, title, price, _]:
        print(f'Книга: {author}, {title}, {price}')       

    # Long way
    # case [author, title, price]:
    #     print(f'Книга 1: {author}, {title}, {price}')
    # case [_, author, title, price, _]:
    #     print(f'Книга 2: {author}, {title}, {price}')
    
    case _:
        print('непонятный формат данных')

