
numbers = []
quantity = int(input('quantity:  '))
counter = 0

while quantity >= counter:
    counter += 1
    
    output_numbers = float(input('Enter:  '))
    numbers.append(output_numbers)

    if quantity == counter:
        numbers.sort()
        print(numbers)