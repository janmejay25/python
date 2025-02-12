# simple class example
class myClass:
    name = "janmejay"
    age = 20
print(myClass.name)
print(myClass.age)


# init used in class
class car:
    def __init__(self,name,modal):
        self.name = name
        self.modal = modal

    def display(self):
        print("Name: ",self.name)
        print("Modal: ",self.modal)
        return "using retrun type  Name: "+self.name+" Modal: "+str(self.modal)

c1 = car("tiago",2025)
c2 = car("BMW",2024)
car.display(c1)
print(c2.display())
print(c1.name)
