'''Creating a random unique profile  EN'''

def uniqueProfile():
    from mimesis import Person
    from mimesis.locales import Locale

    person = Person(Locale.EN)
    
    full_name = person.full_name()
    gender = person.gender()
    age = person.age()
    language = person.language()
    nationality = person.nationality()
    political_views = person.political_views()
    
    profile = [full_name,
               gender,
               age,
               nationality,
               language,
               political_views]
    
    
    question = str(input('Do you want to look at the table? YES/NO '))
    
    if question == 'YES' or question == 'yes':
        import tabulate
        
        table = tabulate.tabulate([['Full name', profile[0]],
                                   ['Gender', profile[1]],
                                   ['Age', profile[2]],
                                   ['Nationality', profile[3]],
                                   ['Language', profile[4]],
                                   ['Political views', profile[5]]], tablefmt="heavy_grid")
        
        return table
    
    return profile
    
print(uniqueProfile())