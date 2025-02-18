# simple inheritance in python
class human:
    def speak(self):
        print("i can speak")
    def talk(self):
        print("i can talk")

class male(human):
    pass

#object for class male
male_1 = male()
# object for class human
male_2 = human()

# male function speak and talk
#inherited from class human
male_1.speak()
male_1.talk()

#simple class calling using object
male_2.speak()
male_2.talk()