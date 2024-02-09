
class car:
    def __init__(self,model,color):
        self.model = model
        self.color = color

    def printdetails(self):
        print("model :",self.model)
        print("color :",self.color)

class sedanEngine():
    def start(self):
        print("Car has started.")

    def stop(self):
        print("Car has stopped.")

class sedan(car):

    def __init__(self, model, color):
        super().__init__(model, color)
        self.engine = sedanEngine()

    def setStart(self):
        self.engine.start

    def setStop(self):
        self.engine.stop

car1 = sedan("Toyota","Grey")
car1.setStart()
car1.printdetails()
car1.setStop()