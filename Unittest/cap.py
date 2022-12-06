from string import capwords


def cap_text(text):
    '''
    Input - строка
    Output - строка, в которой каждой слово с заглавной буквы
    '''
    # result = ' '.join([word.capitalize() for word in text.split()])
    # result = ' '.join(list(map(lambda word: word.capitalize(), text.split())))
    return capwords(text)
