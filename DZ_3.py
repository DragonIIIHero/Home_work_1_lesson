class Error:
    def __init__(self, *args):
        self.my_list = []


    def my_input(self):
        while True:
            try:
                val = int(input('Введите целое число: '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Необходимо ввести целое число")
                y_or_n = input(f'Хотите начать сначала? Y/N: ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Программа завершила работу'
                else:
                    return f'Программа завершила работу'


try_except = Error(1)
print(try_except.my_input())
