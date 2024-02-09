
# create class and obj

class Myclass():
    pass
obj = Myclass()

# initializing value & assigning value

class Employee:
    Id = None
    Salary = None
    Department = None

Rahul = Employee()

Rahul.Id = 3789
Rahul.Salary = 15000
Rahul.Department = "Software Enginnering"

# Outside class add property
Rahul.Title = "Team Lead"

class Employee1:

    def __init__(self,Id,Salary,Department):
        self.Id = Id
        self.Salary = Salary
        self.Department = Department

Rahul = Employee1(367,1500,"Software Engineering")


# class variable and instant variable

class footballteam:
    Teamname = "Liver Poool"
    def __init__(self,name):
        self.name = name

p1 = footballteam("steave")
p2 = footballteam("mark")

# class variable use differtway

class footballteam1:
    Teamname = "Liver Poool"
    teamplayer = []

    def __init__(self,name):
        self.name = name
        self.teamplayer.append(name)

p1 = footballteam1("steave")
p2 = footballteam1("mark")

# print(p1.name)
# print(p1.Teamname)
# print(p1.teamplayer)
# print(p2.name)
# print(p2.Teamname)
# print(p2.teamplayer)



# class method

class Employeeclass:

    def __init__(self,Id,Salary,Department,name = "Dinesh"):
        self.Id = Id
        self.Salary = Salary
        self.Department = Department
        self.name = name

    def tax(self):
        print("Hi I am :",self.name)
        return self.Salary * 0.2
    
    def SalaryperDay(self):
        return self.Salary / 30

    

Rahul = Employeeclass(367,1500,"Software Engineering","Mohan")

print(Rahul.Id)
print(Rahul.Salary)
print(Rahul.Department)
print(Rahul.tax())
print(Rahul.SalaryperDay())