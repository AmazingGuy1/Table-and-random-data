# Версия 1.0 RU

number_of_iteration = int(input('Введите колличество итераций  '))
counter = 0

if len(str(number_of_iteration)) > 0:
	
    sum_of_numbers = int()
    different_of_number = int()
    
    
    while counter != number_of_iteration:
    
        _integer = int(input('Введите число  '))

        sum_of_numbers += _integer
        different_of_number -= _integer
        
        counter += 1
    
    print(sum_of_numbers, different_of_number, sep='\n')
      


else:
    print('Программа окончилась неудачно')
