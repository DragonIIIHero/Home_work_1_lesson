class Road:


    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
        self.score = lenght * width * 25 * 0.005

    def road_check(self):
        print(f"{self._lenght}М * {self._width}М * 25кг * 5 см = {self.score}т")


road_score = Road(20, 5000)
road_score.road_check()