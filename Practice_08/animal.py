class Animal:
    def eat(self):
        return "Eating..." 
class pet(Animal):
    def play(self):
        return "Playing..."
class Dog(pet):
    def bark(self):
        return "Barking..."                                  
obj=Dog()
print(obj.eat())
print(obj.play())
print(obj.bark())
