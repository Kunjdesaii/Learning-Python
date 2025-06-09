import random
computer=random.randint(0, 2)
you=int(input("Enter your choice (0 for Rock, 1 for Paper, 2 for Scissors): "))
if you == computer:
    print("It's a tie!")    
elif (you == 0 and computer == 2) or (you == 1 and computer == 0) or (you == 2 and computer == 1):
    print("You win!")
elif (computer == 0 and you == 2) or (computer == 1 and you == 0) or (computer == 2 and you == 1):
    print("You lose!")
else:
    print("Invalid input. Please enter 0, 1, or 2.")
1