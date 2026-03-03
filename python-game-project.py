import random

print("🎮 Welcome to Number Guessing Game")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess > secret_number:
            print("Too High 📈 Try again!")
        elif guess < secret_number:
            print("Too Low 📉 Try again!")
        else:
            print("🎉 Congratulations! You guessed it!")
            print("Total Attempts:", attempts)
            break

    except ValueError:
        print("❌ Please enter a valid number")
