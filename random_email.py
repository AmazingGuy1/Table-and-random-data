from mimesis import Person
from mimesis.locales import Locale

person = Person(Locale.EN)

mail = person.email(domains=['@gmail.com'])
mail += '\n'
print(mail)

random_mail = open('random_mail.txt', 'a')
random_mail.write(mail)