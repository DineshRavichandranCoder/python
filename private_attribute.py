# private attributes

class Employee:
    def __init__(self,Id,Salary):
        self.Id = Id
        self.__Salary = Salary

    def displaysalary(self):
        print(self.__Salary)

Rahul = Employee(367,1500)

print(Rahul.Id)
(Rahul.displaysalary())

class Employee1:
    def __init__(self,Id,Salary):
        self.Id = Id
        self.__Salary = Salary

steave = Employee1(367,1500)

print(steave._Employee1__Salary)

