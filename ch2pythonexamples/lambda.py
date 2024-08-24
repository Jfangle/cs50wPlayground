people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Hermione", "house": "Gryffindor"},
]



people.sort(key=lambda person: person["name"])
print(people)