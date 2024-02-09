class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return (self.x * self.x) + (self.y * self.y) + (self.z * self.z)

test = Point(1,3,5)

# print(test.sqSum())


class Student:
    def __init__(self,name,phy,chem,bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        totsub = self.phy + self.chem + self.bio
        
        return totsub

    def percentage(self):
        totsub = self.phy + self.chem + self.bio

        print(totsub/300)
        percentage = (self.totalObtained//300) * 100

        return percentage

obj1 = Student("Mark",80,90,40)

# print(obj1)
print(obj1.totalObtained())
print(obj1.percentage())