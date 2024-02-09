
class Rectangle():
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.side = 4

    def getArea(self):
        return self.width * self.height
    
class circle():
    def __init__(self,radius):
        self.radius = radius
        self.side = 0

    def getArea(self):
        return (self.radius * self.radius * 3.142)
    

shape = [Rectangle(5,10),circle(3)]
# print(shape[0].side)
# print(shape[0].getArea())
# print(shape[1].side)
# print(shape[1].getArea())


# duck typing

class dog():
    def speak(self):
        print("Woof Woof")

class cat():
    def speak(self):
        print("meow meow")

class Animalsound():
    def sound(self,animal):
        animal.speak()

obj = Animalsound()
Dog = dog()
Cat =cat()

obj.sound(Dog)
obj.sound(Cat)


