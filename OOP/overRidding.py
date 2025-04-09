class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Create objects
animal = Animal()
dog = Dog()
cat = Cat()

print(animal.sound())  # Output: Some generic animal sound
print(dog.sound())     # Output: Bark
print(cat.sound())     # Output: Meow
