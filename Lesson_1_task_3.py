percent = int(input("Введите число от 1 до 20: "))
if percent == 1:
    print(percent, "процент.")
elif percent > 1 and percent <= 4:
    print(percent, "процента")
elif percent > 4 and percent <= 20:
    print(percent, "процентов")
else:
    print("Необходимо ввести число в диапазоне от 1 до 20 включительно")

print(input("Для выхода из программы нажмите 'Enter'"))