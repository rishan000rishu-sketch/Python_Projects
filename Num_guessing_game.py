import random

secret_number = random.randint(1, 100)

attempts = 0

print("===== NUMBER GUESSING GAME =====")
print("Guess a number between 1 and 100")

while True:

    guess = int(input("Enter your guess: "))

    attempts += 1

    if guess > secret_number:

        print("Too High! Try again.")

    elif guess < secret_number:

        print("Too Low! Try again.")

    else:

        print("\nCorrect Guess!")
        print("The number was:", secret_number)
        print("Total attempts:", attempts)

        break
    