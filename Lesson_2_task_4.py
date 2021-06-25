task = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
words = []
name = []


for sentence in task:
    words = sentence.split()
    sentence = words[-1:]
    sentence = str(sentence)
    name = sentence.lower().title()
    name = name.strip("[").strip("]").strip("'")
    print(f"Привет, {name}")

