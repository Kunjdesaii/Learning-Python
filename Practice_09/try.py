try:
    with open("one.txt","r") as f: 
        print(f.read())

except Exception as e:
        print(f"An error occurred: {e}")


try:
    with open("two.txt","r") as f:
        print(f.read())

except Exception as e:
    print(f"An error occurred: {e}")


try:
    with open("three.txt","r") as f:
        print(f.read())

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("This block always executes, regardless of whether an exception occurred or not.")