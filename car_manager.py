from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_LIST = []
CAR_COUNT = 20


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.setheading(180)
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(random.randint(300, 1200), random.randint(-280, 280))
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_list = []

    def gen_cars(self):
        for _ in range(CAR_COUNT):
            car = CarManager()
            self.car_list.append(car)

    def move(self):
        for car in self.car_list:
            car.forward(self.car_speed)
            if car.xcor() < -300:
                car.goto(random.randint(300, 1200), random.randint(-250, 250))

    def level_up(self):
        # commented code clears screen and generates a new set of cars for next level
        # for car in self.car_list:
        #     car.goto(1000, 0)
        # self.car_list = []
        self.car_speed += MOVE_INCREMENT
        # self.gen_cars()

