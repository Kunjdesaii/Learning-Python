import random
def play_game():
    score = random.randint(1, 100)
    print(f"Your score is: {score}")
    with open(r"c:/Users/User/Desktop/Python Bee/Learning-Python/Practice_06/hisscore.txt", "r") as file:
        high_scoree = file.read()
        high_score = int(high_scoree) if high_scoree.strip() else 0
    if score>high_score:
        print("Congratulations! You've set a new high score!")
        with open(r"c:/Users/User/Desktop/Python Bee/Learning-Python/Practice_06/hisscore.txt", "w") as file:
            file.write(str(score))
        high_score = score                                                                              
    return score
play_game()

# import random
# def play_game():
#     score = random.randint(1, 100)
#     print(f"Your score is: {score}")
#     with open(r"c:/Users/User/Desktop/Python Bee/Learning-Python/Practice_06/hisscore.txt", "r") as file:
#         high_score_str = file.read()
#         high_score = int(high_score_str) if high_score_str.strip() else 0
#     if score > high_score:
#         print("Congratulations! You've set a new high score!")
#         with open(r"c:/Users/User/Desktop/Python Bee/Learning-Python/Practice_06/hisscore.txt", "w") as file:
#             file.write(str(score))
#         high_score = score
#     return score
# play_game()