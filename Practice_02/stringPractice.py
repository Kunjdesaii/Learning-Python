# diplay name by greeting
name=input("enter your name:")
print(f"welcome {name}")
# REPLACE NAME AND DATE
letter="""Dear <name>,today is <date> and I am writing to you to say that I am very happy to see you again. I hope you are doing well and that we can catch up soon. Take care and see you soon!"""
letter=letter.replace("<name>",name).replace("<date>","01/06/2025")
print(letter)
# find spaces in string
spacee="kunj is a  python developer"
print(spacee.find("  "))
# replace spaces in string
spacee=spacee.replace("  "," ")
print(spacee)
# find length of string
print(len(spacee))  
# find index of character
# print(spacee.index("a"))
# # find count of character
# print(spacee.count("a"))    
# # find character in string
# print(spacee[0])  # first character 
# print(spacee[-1]) # last character
# # find character in string  
# print(spacee[0:4]) # first 4 characters
# # find character in string
# print(spacee[0:4:2]) # first 4 characters with step 2
# # find character in string
# print(spacee[0:4:-1]) # first 4 characters with step -1 (will not work as step is negative)
# # find character in string
# print(spacee[0:4:1]) # first 4 characters with step 1
# # find character in string
# print(spacee[0:4:3]) # first 4 characters with step 3
l="\n\ndear kunj, \n\ttoday is 01/06/2025 and I am writing to you to say that I am very happy to see you again. I hope you are doing well and that we can catch up soon. \n\nTake care and see you soon!"
print(l)
