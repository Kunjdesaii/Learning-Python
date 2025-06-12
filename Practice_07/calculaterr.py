class Calculate:
    def __init__(self, n):
        self.n = n
    def square(self):
        return self.n ** 2
    def cube(self):
        return self.n ** 3                                      
    def square_root(self):
        return self.n ** 0.5

a= Calculate(4)
print("Square:", a.square())
print("Cube:", a.cube())
print("Square Root:", a.square_root())

b= Calculate(9)
print("Square:", b.square())
print("Cube:", b.cube())
print("Square Root:", b.square_root())

    