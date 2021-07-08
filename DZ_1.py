def nums_gen():
    for num in range(first, second + 1):
        if num % 2 != 0:
            result = num
            yield num

first = int(input("Введите начальное число: "))
second = int(input("Введите вонечное число: "))
result = nums_gen()
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
