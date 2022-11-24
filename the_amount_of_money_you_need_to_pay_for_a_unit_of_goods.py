from tabulate import tabulate

product_name = input('Введите имя продукта  ')
sell_product = float(input('Введите стоимость продукта  '))
k_product = int(input('Введите количетсво продукта  '))

a = tabulate([['Названия продукта', product_name], ['Стоимость продукта', sell_product], ['Количество продукта', k_product], ['Итоговая стоимость', sell_product * k_product]], tablefmt="simple_outline")

print(a)
