class Car:
    def __init__(self):
        self.__engine_status = "OFF"  # private variable

    def start(self):
        self.__check_fuel()
        self.__engine_status = "ON"
        print("Car started..")

    def __check_fuel(self):
        print("Checking fuel level.. => Fuel level checked ,Ready to Start")

car = Car()
car.start()
