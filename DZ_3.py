tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Анна'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]

while len(tutors) > len(klasses):
    klasses.append("None")

resalt = zip(tutors, klasses)

print(resalt)
print(next(resalt))
print(next(resalt))
print(next(resalt))
print(next(resalt))
print(next(resalt))
print(next(resalt))
print(next(resalt))
print(next(resalt))