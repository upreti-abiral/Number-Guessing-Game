import random
import sys


def welcome_message():
    print("=" * 50)
    print("Welcome to the Number Guessing Game")
    print("=" * 50)
    print("Rules:")
    print("1. The computer chooses a random number within a range.")
    print("2. Try to guess the number in as few attempts as possible.")
    print("3. You will be told if your guess is too high or too low.")
    print("4. Type 'q' anytime to quit the game.")
    print()


def choose_difficulty():
    print("Select Difficulty Level:")
    print("1. Easy   (1 - 50, unlimited attempts)")
    print("2. Medium (1 - 100, max 10 attempts)")
    print("3. Hard   (1 - 500, max 12 attempts)")

    while True:
        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            return 1, 50, None
        elif choice == "2":
            return 1, 100, 10
        elif choice == "3":
            return 1, 500, 12
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


def get_player_guess():
    guess = input("Enter your guess (or 'q' to quit): ")

    if guess.lower() == "q":
        print("Thanks for playing. Goodbye!")
        sys.exit()

    if not guess.isdigit():
        print("Please enter a valid number.")
        return None

    return int(guess)


def play_game():
    welcome_message()

    while True:
        low, high, max_attempts = choose_difficulty()
        secret_number = random.randint(low, high)
        attempts = 0

        print(f"\nI have chosen a number between {low} and {high}.")
        print("Good luck!\n")

        while True:
            guess = get_player_guess()

            if guess is None:
                continue

            if guess < low or guess > high:
                print(f"Please enter a number between {low} and {high}.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(
                    f"Correct! You guessed the number in "
                    f"{attempts} attempts."
                )
                break

            if max_attempts and attempts >= max_attempts:
                print(
                    f"Out of attempts! The number was {secret_number}."
                )
                break

        play_again = input(
            "\nDo you want to play again? (y/n): "
        ).lower()

        if play_again != "y":
            print("Thanks for playing! See you next time.")
            break


if __name__ == "__main__":
    play_game()
