class human:
    def speak(self):
        print("i can speak")
    def talk(self):
        print("i can talk")

class male(human):
    def dance(self):
        print("i can dance")
    def talk(self):
        print("i can talk as class male")

#object for class male
male_1 = male()

# male function speak and talk
# inherited from class human
male_1.speak()
# talk method is used in class human and male
# that is called method overRiding
# but it`ll give the output using class male
# (class male >> class human) beacuse it has method in OG class
male_1.talk()

# dance method is in male class
male_1.dance()