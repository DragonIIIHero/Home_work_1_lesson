class Car:
    is_police = False


    def __init__(self, color, name, is_police):
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self, speed):
        self.speed = speed
        print(f"Машина модели {self.name} тронулась, скорость {self.speed}.")


    def stop(self):
        self.speed = 0
        print(f"Машина модели {self.name} остановилась.")


    def turn(self, direction):
        if direction == "лево" or direction == "право":
            print(f"Машина модели {self.name} повернула на {direction}.")
        else:
            print(f"Машина запрограммирована поворачивать на лево и на право.")


    def show_speed(self):
        print(f"Скорость автомобиля {self.speed} км/ч.")


class TownCar(Car):


    def __init__(self, color, name, is_police):
        super().__init__(color, name, is_police)


    def show_speed(self):
        if self.speed >= 61:
            print(f"Ваша скорость равна {self.speed}, что превышает допустимую скорость в 60 км/ч")
        else:
            print(f"Скорость автомобиля {self.speed} км/ч.")


class SportCar(Car):


    def __init__(self, color, name, is_police):
        super().__init__(color, name, is_police)


class WorkCar(Car):


    def __init__(self, color, name, is_police):
        super().__init__(color, name, is_police)


    def show_speed(self):
        if self.speed >= 41:
            print(f"Ваша скорость равна {self.speed}, что превышает допустимую скорость в 40 км/ч")
        else:
            print(f"Скорость автомобиля {self.speed} км/ч.")

class PoliceCar(Car):


    def __init__(self, color, name, is_police):
        super().__init__(color, name, is_police)



auto_1 = PoliceCar("синий" , "Лада", True)
auto_1.go(20)
auto_2 = SportCar("красный", "Бугати", False)
auto_2.go(80)
auto_2.show_speed()
auto_2.turn("право")
auto_3 = WorkCar("черный", "JCB", False)
auto_3.go(46)
auto_3.show_speed()
auto_4 = TownCar("белый", "Лада", False)
auto_4.go(64)
auto_4.show_speed()
auto_4.stop()
auto_4.show_speed()
