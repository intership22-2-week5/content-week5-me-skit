DATA = [
    {
        'name': 'Carlos',
        'age': 72,
        'organization': 'Ciancoders',
        'position': 'Technical Leader',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Ciancoders',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Ciancoders',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Ciancoders',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'internship',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():

    # Comprehensions solutions
    # 1. obtener todos los desarrolladores de python
    p_developers = list(filter(lambda person: person['language'] == 'python', DATA))
    print(len(p_developers))
    for item in p_developers:
      print(item)    

    # 2. obtener todos los desarrolladores de python que tienen una edad mayor a 20
    p_developers_20 = [person for person in DATA if person['language'] == 'python' and person['age'] > 20 ]
    print(len(p_developers_20))
    for item in p_developers_20:
        print(item)

    # 3. obtener todos los trabajadores de ciancoders 
    cc_workers = list(filter(lambda person: person['organization'] == 'Ciancoders', DATA))
    print(len(cc_workers))
    for item in cc_workers:
        print(item)
    
    # 4. obtener todos los trabajadores de ciancoders que tienen una edad mayor a 30
    cc_workers_30 = [person for person in DATA if person['organization'] == 'Ciancoders' and person['age'] > 30 ]
    print(len(cc_workers_30))
    for item in cc_workers_30:
      print(item)

    # 5. obtener todos los trabajadores de mayores de 18 años
    adults = list(filter(lambda person: person['age'] >= 18, DATA))
    print(len(adults))
    for item in adults:
      print(item)

    # 6. obtener todos los trabajadores de mayores a 70 años
    mayor_70 = [person for person in DATA if person['age'] > 70 ]
    print(len(mayor_70))
    for item in mayor_70:
      print(item)

if __name__ == '__main__':
    run()