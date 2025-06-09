# with open(poemfile := r"c:\Users\User\Desktop\Python Bee\Learning-Python\Practice_06\poem.txt", 'r') as file:
#     poem = file.read()
# print(poem)


f = open(r"c:\Users\User\Desktop\Python Bee\Learning-Python\Practice_06\poem.txt", "r")
p= f.read()

# if p.__contains__("twinkle"):
#     print("twinkle found")

if "twinkle" in p:
    print("twinkle found")
else:
    print("twinkle not found")
    
print(p)
f.close()

