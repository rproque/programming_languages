#!/usr/local/bin/python3
# MACOSX


class Car:
    '''Class of Car'''
    pass

    def __init__(self, make, model, year, color, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    def turn_on(self):
        '''Turn the car on'''
        return self.make + ' is on'

    def drive(self, miles):
        '''Log Mileage'''
        self.mileage = self.mileage + miles
        return "Car traveled {} miles.".format(miles)


if __name__ == '__main__':
    # Create an class object of type Car:
    bronco = Car('Ford', 'Bronco', '1993', 'Green', 0)

    # Print class info
    help(Car)

    # Print characteristics of object
    print("*" * 15, "CAR", "*" * 15)
    print("Make:     {}".format(bronco.make))
    print("Model:    {}".format(bronco.model))
    print("Year:     {}".format(bronco.year))
    print("Color:    {}".format(bronco.color))
    print("Mileage:  {}".format(bronco.mileage))

    # Access methods
    print("*" * 15, "DO STUFF", "*" * 15)
    print(bronco.turn_on())
    print("Mileage:  {}".format(bronco.mileage))
    print(bronco.drive(500))
    print("Mileage:  {}".format(bronco.mileage))
    print(bronco.drive(250))
    print("Mileage:  {}".format(bronco.mileage))

    # Instance variable
    bronco.horsepower = 325
    print("The {} {} has {} horsepower".format(bronco.make, bronco.model, bronco.horsepower))