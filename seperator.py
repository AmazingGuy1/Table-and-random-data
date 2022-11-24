# Создать функцию, написать разделить (слова, буквы, предложения)

text = input('Введите текст  ')

def seperator(text = str()):
    from tabulate import tabulate
    
    words = text.split(' ')
    letters = len(text)
    offers = text.split('.')
    
    _tabulate = tabulate([['Количество слов', len(words)], ['Количество букв', letters], ['Количество предложений', len(offers)]],   tablefmt="simple_grid")
    print(_tabulate)
    
    
seperator(text)