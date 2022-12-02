# Russian Version

choice = input('Хотите ли вы увидеть инструкцию ') # False, True

if choice == 'True' or choice == 'true':
    print('Возможные типы перевода', 'мин', 'час', 'сек')


type_number = ['мин', 'час', 'сек']
input_time = int(input('Введите время '))
type_time = input('Введите тип времени ')


if type_time == type_number[0]:
    where = input('Введите куда вы хотите перевести ')
    if where == type_number[1]:
        print(f'{input_time / 60}')
    elif where == type_number[2]:
        print(f'{input_time * 60}')

if type_time == type_number[1]:
    where = input('Введите куда вы хотите перевести ')
    if where == type_number[0]:
        print(f'{input_time / 60}')
    elif where == type_number[2]:
        print(f'{input_time * 60}')
        
if type_time == type_number[2]:
    where = input('Введите куда вы хотите перевести ')
    if where == type_number[0]:
        print(f'{input_time / 60}')
    elif where == type_number[1]:
        print(f'{input_time / 60 / 60}')