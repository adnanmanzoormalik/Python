class Car:
    def start(self):
        print("started")

car = Car.__new__(Car)
car.start()