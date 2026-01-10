secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number: "))

    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")

print("Correct! You guessed the number.")
