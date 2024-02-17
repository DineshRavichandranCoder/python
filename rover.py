
class rover():
    def __init__(self,x,y,dir):
        self.x = x
        self.y = y
        self.dir = dir

    def move(self,cmd):
        for cmd in cmd:
            if(cmd == "M"):
                self.forward()
            elif(cmd == "L"):
                self.turn_left()
            elif(cmd == "R"):
                self.turn_right()
    
    def forward(self):
        if(self.dir == "N"):
            self.y += 1
        elif(self.dir == "S"):
            self.y -= 1
        elif(self.dir == "E"):
            self.x += 1
        elif(self.dir == "W"):
            self.x -= 1

    def turn_left(self):
        if(self.dir == "N"):
            self.dir = "W"
        elif(self.dir == "S"):
            self.dir = "E"
        elif(self.dir == "E"):
            self.dir = "N"
        elif(self.dir == "W"):
            self.dir = "S"

    def turn_right(self):
        if(self.dir == "N"):
            self.dir = "E"
        elif(self.dir == "S"):
            self.dir = "W"
        elif(self.dir == "E"):
            self.dir = "S"
        elif(self.dir == "W"):
            self.dir = "N"
        
obj1 = rover(1,2,'N')
obj1.move("LMLMLMLMM")

obj2 = rover(3,3,'E')
obj2.move("MMRMMRMRRM")

print(f"rover position{obj1.x,obj1.y} and direction {obj1.dir}")
print(f"rover position{obj2.x,obj2.y} and direction {obj2.dir}")
