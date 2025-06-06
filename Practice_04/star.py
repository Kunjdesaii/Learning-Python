k=int(input("Enter number of rows: "))
for i in range(1, k + 1):
    print(" "* (k-1), end="")
    print("*" * (2 * i - 1))
    k -= 1
for l in range(1, k + 1):
    print("*"* l, end="")
    print("")
