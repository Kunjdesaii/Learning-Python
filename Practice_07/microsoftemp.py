class Programmer:
    @staticmethod
    def greet():
        print("good morning")
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language
Programmer.greet()  # Calling the static method
k=Programmer("John", 30, "Python")
print(k.name, k.age, k.language)
k2=Programmer("Alice", 25, "Java")
print(k2.name, k2.age, k2.language)