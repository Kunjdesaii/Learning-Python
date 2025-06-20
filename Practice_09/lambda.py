square = lambda x: x * x
print(square(5))

sum = lambda a, b: a + b
print(sum(10, 20))

multiply = lambda a, b: a * b
print(multiply(10, 20))

l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sqlist = list(map(lambda x: x * x, l))
print(sqlist)