
class vechile:
    def __init__(self,make,color,model):
        self.make = make
        self.color = color
        self.model = model

    def printdetails(self):
        print(self.make)
        print(self.color)
        print(self.model)

class car(vechile):
    def __init__(self, make, color, model, door):
        vechile.__init__(self,make, color, model)
        self.door = door

    def printcardetails(self):
        self.printdetails()
        print(self.door)

obj = car("Tata","Blue","Punch",4)

# obj.printcardetails()


# super()

class vechile():
    fuelcap = 90

class car(vechile):
    fuelcap = 50
    def display(self):
        print(super().fuelcap)
        print(self.fuelcap)

obj1 = car()
# obj1.display()

class vechile1():
    def display(self):
        print("parent")

class car1(vechile1):
    fuelcap = 50
    def display(self):
        super().display()
        print("child")

obj1 = car1()
# obj1.display()


class parent():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class child(parent):
    def __init__(self, x, y,z):
        super().__init__(x, y)
        self.z = z

obj2 = child(1,2,3)
# print(obj2.x)
# print(obj2.y)
# print(obj2.z)


# Type of inheritance

# single inheritance

class vechile:

    def topspeed(self,speed):
        self.speed = speed
        print(self.speed)

class car(vechile):
    
    def printdetails(self):
        print("Above is Vechile speed")

obj2 = car()
# obj2.topspeed(210)
# obj2.printdetails()

# multiple inheritance
class vechile:

    def topspeed(self,speed):
        self.speed = speed
        print(self.speed)

class car(vechile):
    
    def printdetails(self):
        print("Above no is Vechile speed")

class hybrid(car):

    def printhybriddetails(self):
        print("Above Vechile is Truck")

obj2 = hybrid()
# obj2.topspeed(210)
# obj2.printdetails()
# obj2.printhybriddetails()

# Hierarchical inheritance

class vechile:

    def topspeed(self,speed):
        self.speed = speed
        print(self.speed)

class car(vechile):
    pass

class truck(vechile):
    pass

obj2 = car()
# obj2.topspeed(95)

obj3 = truck()
# obj3.topspeed(105)

# multiple inheritance

class CombustionEngine():
    def settankcapaccity(self,capacity):
        self.capacity = capacity

class ElectricalEngine():
    def setchargecapacity(self,charge):
        self.charge = charge

class car(CombustionEngine,ElectricalEngine):
    def printdetails(self):
        print(self.capacity)
        print(self.charge)

obj5 = car()
# obj5.settankcapaccity("250 li")
# obj5.setchargecapacity("250 W")
# obj5.printdetails()

# hybrid inheritance

class Engine:
    def setpower(self,power):
        self.power = power

class CombustionEngine(Engine):
    def settankcapaccity(self,capacity):
        self.capacity = capacity

class ElectricalEngine(Engine):
    def setchargecapacity(self,charge):
        self.charge = charge

class car(CombustionEngine,ElectricalEngine):
    def printdetails(self):
        print(self.power)
        print(self.capacity)
        print(self.charge)

obj5 = car()
obj5.setpower("250 cc")
obj5.settankcapaccity("250 li")
obj5.setchargecapacity("250 W")
obj5.printdetails()