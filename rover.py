
# class rover():
#     def __init__(self,x,y,dir):
#         self.x = x
#         self.y = y
#         self.dir = dir

#     def move(self,cmd):
#         for cmd in cmd:
#             if(cmd == "M"):
#                 self.forward()
#             elif(cmd == "L"):
#                 self.turn_left()
#             elif(cmd == "R"):
#                 self.turn_right()
    
#     def forward(self):
#         if(self.dir == "N"):
#             self.y += 1
#         elif(self.dir == "S"):
#             self.y -= 1
#         elif(self.dir == "E"):
#             self.x += 1
#         elif(self.dir == "W"):
#             self.x -= 1

#     def turn_left(self):
#         if(self.dir == "N"):
#             self.dir = "W"
#         elif(self.dir == "S"):
#             self.dir = "E"
#         elif(self.dir == "E"):
#             self.dir = "N"
#         elif(self.dir == "W"):
#             self.dir = "S"

#     def turn_right(self):
#         if(self.dir == "N"):
#             self.dir = "E"
#         elif(self.dir == "S"):
#             self.dir = "W"
#         elif(self.dir == "E"):
#             self.dir = "S"
#         elif(self.dir == "W"):
#             self.dir = "N"
        
# obj1 = rover(1,2,'N')
# obj1.move("LMLMLMLMM")

# obj2 = rover(3,3,'E')
# obj2.move("MMRMMRMRRM")

# print(f"rover position{obj1.x,obj1.y} and direction {obj1.dir}")
# print(f"rover position{obj2.x,obj2.y} and direction {obj2.dir}")

class Player:
    def __init__(self, ID, name, teamName):
        self.ID = ID
        self.name = name
        self.teamName = teamName


class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def getNumberOfPlayers(self):
        return len(self.players)

    def addPlayer(self, player):
        self.players.append(player)


class School:
    def __init__(self, name):
        self.name = name
        self.teams = []

    def addTeam(self, team):
        self.teams.append(team)

    def getTotalPlayersInSchool(self):
        length = 0
        for n in self.teams:
            length = length + (n.getNumberOfPlayers())
            print(self.players)
        return length


p1 = Player(1, "Harris", "Red")
p2 = Player(2, "Carol", "Red")
p3 = Player(1, "Johnny", "Blue")
p4 = Player(2, "Sarah", "Blue")

red_team = Team("Red Team")
red_team.addPlayer(p1)
red_team.addPlayer(p2)

blue_team = Team("Blue Team")
blue_team.addPlayer(p2)
blue_team.addPlayer(p3)

mySchool = School("My School")
mySchool.addTeam(red_team)
mySchool.addTeam(blue_team)

print("Total players in mySchool:", mySchool.getTotalPlayersInSchool())