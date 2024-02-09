
class user:
    
    def __init__(self,username):
        self.__username = username

    def setusername(self,name):
        self.__username = name

    def getusername(self):
        return self.__username
    
rahul = user("steav1")
print(rahul.getusername())
rahul.setusername("steav2")
print(rahul.getusername())