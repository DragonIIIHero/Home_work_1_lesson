class Stationery:
    title = "Канцелярия"


    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    title = "Ручка"


    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencile(Stationery):
    title = "Карандаш"


    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationery):
    title = "Маркер"


    def draw(self):
        print("Запуск отрисовки маркером")


stationary = Stationery()
stationary.draw()
pen = Pen()
print(pen.title)
pen.draw()
pencile = Pencile()
pencile.draw()
handle = Handle()
handle.draw()