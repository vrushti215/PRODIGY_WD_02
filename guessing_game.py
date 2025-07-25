import random

def guessing_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!\n")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Prompt the user for input
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Compare guess with the target number
            if guess < number_to_guess:
                print("📉 Too low! Try again.\n")
            elif guess > number_to_guess:
                print("📈 Too high! Try again.\n")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("❌ Invalid input. Please enter a number.\n")

if __name__ == "__main__":
    guessing_game()
