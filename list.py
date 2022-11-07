from tabulate import tabulate

# RUS VERSION

txt = input('Введите текст  ')
lis = []
counter = 0

for _ in txt.split(' '):
    counter += 1
    lis.append(_)

print(tabulate([['Разделёный текст' , lis], ['Количество элементов', counter]], tablefmt="simple_grid"))