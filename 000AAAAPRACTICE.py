class Car():
    def __init__(self, model, color, milaege):
        self.model = model
        self.color = color
        self.milaege = milaege
        self.on = False

    def car_details(self):
        print(f"Model of car: {self.model}")
        print(f"Colour of car: {self.color}")
        print(f'Milaege: {self.milaege}')
        
    def start(self):
        print("car has been started")
        self.on = True

    def stop(self):
        if self.on:
            print("Car has been stopped")
            self.on = False
        else:
            print("Car is not on")

bmw2021 = Car("BMW", "Red", 12)
bmw2021.car_details()
bmw2021.start()
bmw2021.stop()

