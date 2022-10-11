class Car:
    def __init__(self, momentum=0):
        self.momentum = momentum
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("I am traveling at {} kph!".format(self.momentum))

    def accelerate(self):
        self.momentum += 12

    def brake(self):
        if self.momentum < 12:
            self.momentum = 0
        else:
            self.momentum -= 12

    def step(self):
        self.odometer += self.momentum
        self.time += 1

    def average_momentum(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass


if __name__ == '__main__':

    my_car = Car()
    print("I am a car named XYZ!")
    while True:
        action = input("Let me know, what should I do? [A]ccelerate, [B]rake, "
                       "show [O]ddometer, or show average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I can't do that :) !")
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has traveled {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("This XYZ car's average momentum is {} kph".format(my_car.average_momentum()))
        my_car.step()
        my_car.say_state()
