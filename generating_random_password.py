'''Generating random password   EN'''



def grp_V1():
    
    import string
    import random

    total = string.ascii_letters + string.digits + string.punctuation
    lenght = int(input('Enter the value you need '))

    password = ''.join(random.sample(total, lenght))

    print(password)
    
    

def grp_V2(total, lenght):
    
    from random import sample
    
    password = ''.join(sample(total, lenght))
    
    print(password)