import random

print("🎯 Number Guessing Game")

secret_number = random.randint(1, 50)
max_attempts = 5

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt} - Enter guess: "))

    if guess < secret_number:
        print("Too Low ⬇")
    elif guess > secret_number:
        print("Too High ⬆")
    else:
        print("🎉 You Win!")
        break
else:
    print("❌ Game Over!")
    print("Correct number was:", secret_number)
