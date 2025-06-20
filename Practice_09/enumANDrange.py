l=[1,2,3,4,5,6,7,8,9,10]

for i,item in enumerate(l):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 9:
        print(f"Index {i} , value: {item}")
try:
    n=int(input("Enter a number: "))
    table= [n*i for i in range(1, 11)]
    
    with open("table.txt", "a") as file:
        file.write(f"Multiplication table of {n} is {str(table)}: \n")

except ValueError:
    print("Invalid input! Please enter a valid integer.")