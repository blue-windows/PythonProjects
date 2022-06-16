import random

n = random.randint(1,10)

print("Guess a number between 1 and 10")

running = True
while running:
    guess_string = input("Put in your guess\n")

    guess = int(guess_string)
    if guess == n:
        print("Correct!")
        running = False
    elif guess < n:
        print("Try a bigger number")
    elif guess > n:
        print("Try a smaller number")
