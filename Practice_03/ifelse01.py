s1=int(input("enter your age: "))
s2=int(input("enter your age: "))
s3=int(input("enter your age: "))
s4=int(input("enter your age: "))                         
if s1>s2 and s1>s3 and s1>s4:
    print("s1 is the oldest")   
elif s2>s1 and s2>s3 and s2>s4:
    print("s2 is the oldest")
elif s3>s1 and s3>s2 and s3>s4:
    print("s3 is the oldest")
elif s4>s1 and s4>s2 and s4>s3:
    print("s4 is the oldest")
else:
    print("All are equal in age")
# This code compares the ages of four individuals and determines who is the oldest.