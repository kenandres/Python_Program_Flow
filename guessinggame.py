import random

highest = 1000
answer = random.randint(1, highest)
print(answer)

print(f"Please guess a number between 1 and {highest}. ")
print("Or enter 0 to quit:"),
guess = 0
tries = 0

while guess != answer:
    guess = int(input())
    tries = tries + 1

    if guess == 0:
        print("Bye, better luck next time.")
        break
    if guess == answer:
        print(f"You got it correct! It took you {tries} tries to get the correct answer.")
    else:
        if guess < answer:
            print("Please guess higher!")
        elif guess > answer:   # guess must be greater than answer1
            print("Please guess lower")
