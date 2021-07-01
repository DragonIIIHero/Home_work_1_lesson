import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    nouns_1 = nouns.copy()
    adverbs_1 = adverbs.copy()
    adjectives_1 = adjectives.copy()
    result = []
    i = 0
    while i < n:
        tmp = []

        roster_1 = random.choice(nouns_1)
        tmp.append(roster_1)
        nouns_1.remove(roster_1)

        roster_2 = random.choice(adverbs_1)
        tmp.append(roster_2)
        adverbs_1.remove(roster_2)

        roster_3 = random.choice(adjectives_1)
        tmp.append(roster_3)
        adjectives_1.remove(roster_3)

        result.append(" ".join(tmp))

        i += 1
    return result

numberOfJokes = int(input("Введите количество шуток(максимум 5): "))
print(get_jokes(n = numberOfJokes))