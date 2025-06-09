def generatetable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n * i}\n"
        with open(fr"C:\Users\User\Desktop\Python Bee\Learning-Python\Practice_06\tables\table_{n}.txt" ,"w") as file:
            file.write(table)

for i in range(1, 21):
    generatetable(i)
    