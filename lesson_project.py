_input_data = input('Enter your gmail for seperator >>  ')

def gmailSeperator(email = str()):
    
    from rich import print
    import tabulate
    
    
    new_email = email.split('@')
    
    if email.find('@') > 0:
        
        print(tabulate.tabulate([['your email'.upper(), new_email[0],  '@' +  new_email[1]]], tablefmt="simple_grid"))
        
        
    elif email.find('@') < 0:
        
        print('Вы ввели неправильную почту, не пытайтесь обмануть нас!')
        
        
    else:
        print('Что-то пошло не по плану')
    
gmailSeperator(_input_data)