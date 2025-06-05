marks1=int(input("Enter marks of student : "))
marks2=int(input("Enter marks of student : ")) 
marks3=int(input("Enter marks of student : "))
percentage1=((marks1+marks2+marks3)/300)*100
if(percentage1>40 and marks1>33 and marks2>33 and marks3>33):   
    print("Student is pass")
else:
    print("Student is fail")
print("Percentage of student is: ", percentage1)