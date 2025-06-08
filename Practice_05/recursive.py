def sum_of(n):
    if n == 1:
        return 1
    else:
        return n + sum_of(n - 1)
print(sum_of(10))  
