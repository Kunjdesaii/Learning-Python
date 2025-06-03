marks=[]
s1=int(input("Enter marks of student 1: "))
s2=int(input("Enter marks of student 2: "))
s3=int(input("Enter marks of student 3: "))
s4=int(input("Enter marks of student 4: "))
s5=int(input("Enter marks of student 5: "))
marks=[s1,s2,s3,s4,s5]
marks.sort()
print("Marks of students in ascending order:", marks)
print("sum of marks:", sum(marks))
zeros=[1,0,0,2,7,0,23]
print("zeros in list:", zeros.count(0))