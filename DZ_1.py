class Data:
    def __init__(self, date):
        self.day_month_year = str(date)

    @classmethod
    def extract(cls, date):
        my_date = []
        for i in date.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'


    def __str__(self):
        return f'Дата - {Data.extract(self.day_month_year)}'


today = Data('12 - 5 - 1994')
print(today)
print(Data.extract('11 - 11 - 2011'))