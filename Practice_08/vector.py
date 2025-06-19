class TwoDVectore:
    def __init__(self,i, j):
        self.i=i
        self.j=j
    def show(self):
        print(f"({self.i}, {self.j})")
class ThreeDVectore(TwoDVectore):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"({self.i}, {self.j}, {self.k})")

obj1 = TwoDVectore(1, 2)
obj2 = ThreeDVectore(1, 2, 3)
obj1.show()
obj2.show()
