def num_translate_adv():
    for key, value in numbers.items():
        if write_number == key:
            return value[0]
        elif write_number == key.title():
            return value[1]
        else:
            continue


numbers = {'one': ['один', 'Один'],
           'two': ['два', 'Два'],
           'three': ['три', 'Три'],
           'four': ['четыре', 'Четыре'],
           'five': ['пять', 'Пять'],
           'six': ['шесть', 'Шесть'],
           'seven': ['семь', 'Семь'],
           'eight': ['восемь', 'Восемь'],
           'nine': ['девять', 'Девять'],
           'ten': ['десять', 'Десять'],
           'zero': ['ноль', 'Ноль']}
write_number = input('Напишите число на английском от нуля до десяти: ')
print(num_translate_adv())