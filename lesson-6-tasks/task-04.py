#
# Task 4
#


class Car:
    def __init__(self, color, name, is_police):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        print(f'Car turned {direction}')

    def show_speed(self):
        print(f'Speed is {self.speed}')


class TownCar(Car):
    def __init__(self):
        super().__init__('white', 'TownCar', False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Warning the speed is over 60')


class WorkCar(Car):
    def __init__(self):
        super().__init__('black', 'WorkCar', False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Warning the speed is over 40')


class SportCar(Car):
    def __init__(self):
        super().__init__('yellow', 'SportCar', False)


class PoliceCar(Car):
    def __init__(self):
        super().__init__('blue', 'SportCar', True)


car_list = [TownCar(), WorkCar(), SportCar(), PoliceCar()]

for car in car_list:
    print(f'The car is {car.name}, color is {car.color}, is police {car.is_police}')
    car.go(50)
    car.show_speed()
    car.turn('right')
    car.stop()
    car.show_speed()
