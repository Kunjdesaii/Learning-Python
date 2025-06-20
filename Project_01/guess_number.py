import random
n=random.randint(1, 100)
attempts = 0
guess = -1
print("Welcome to the Guess the Number game!")
print("I have selected a number between 1 and 100. Try to guess it!")
while guess!= n:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < n:
        print("Too low! Try again.")
    elif guess > n:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {n} in {attempts} attempts.")