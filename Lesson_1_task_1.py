second = int(input("Введите секунды для перевода в минуты, часы, сутки и ТД: "))
minuts = int(0)
hours = int(0)
days = int(0)
month = int(0)
age = int(0)

while second >= 60:
    second = second - 60
    minuts = minuts + 1
    if second < 60:
        break
while minuts >=60:
    minuts = minuts - 60
    hours = hours + 1
    if minuts < 60:
        break
while hours >= 24:
    hours = hours - 24
    days = days + 1
    if hours < 24:
        break
while True:
    if month == 1 and days >= 28 and age != ((age % 4) - 1):
        days = days - 28
        month = month + 1
        continue
    elif month == 1 and days >= 29 and age == ((age % 4) - 1):
        age = age + 1
        month = month - 12
    elif month == 0 and days >= 31:
        days = days - 31
        month = month + 1
        continue
    elif month % 2 and days >= 31:
        days = days - 31
        month = month + 1
        continue
    elif (month + 1) % 2 and days >= 30:
        days = days - 30
        month = month + 1
        continue
    elif month >= 12:
        age = age + 1
        month = month - 12
    else:
        break

print(age, "лет, ", month, "месяцев, ", days, "дней, ", hours, "часов, ", minuts, "минут, ", second, "секунд.")

print(input("Для выхода из программы нажмите 'Enter'"))