import random
print("---------Number Guessing Game---------")
play_again = "y"
best_score = 0
while play_again == "y":
    number = random.randint(1,100)
    score = 100

    for attempts in range(1, 6):
        guess = int(input("\nGuess a number between 1 and 100: "))

        if  guess < number:
            print("The number is less than the real number\n")
            score = score - 10
        elif guess > number:
            print("The number is high than the real number\n")
            score = score - 10
        elif guess == number:
            print("congrats...!!\n")
            break

        remaining = 5 - attempts
        print(f"You have {remaining} attempts left")
    else:
        print("Sorry you have used all your attempts.")
    print(f"Your score is: {score}")
    if score > best_score:
        best_score = score

    print(f"Best score is : {best_score}")

    play_again = input("\nDo you want to play again? y/n: ").lower()
    