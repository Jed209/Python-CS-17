#Car Creation PY-05-L8
#Object-Oriented Programming

class Car:
    def __init__(self, color, door_number, price):
        self.color = color
        self.door_number = door_number
        self.price = price


car1 = Car("Red", 4, 65000)
car2 = Car("Antimatter Blue Metallic", 4, 76800)

print(car1.price)
print(car2.color)
