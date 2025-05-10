"""
    Project: Number Guessing Game
    1. Guessing function that checks the guess: 3 situations (high, low, and equal)
    2. User input checker (Invalid input like symbols and letters)
    3. main()
"""
import random

def guessing_game():
    ## Generate a number
    number_to_guess = random.randint(1, 100)
    attempts = 1
    while True:
        num = input_checker("Tell me your guess: ")
        if num < number_to_guess:
            if attempts == 10:
                print("Game over! Better luck next time!")
                break
            print(f"Guess the number (between 1 and 100): {num} Too low! Try again.")
            attempts += 1
        elif num > number_to_guess:
            if attempts == 10:
                print("Game over! Better luck next time!")
                break
            print(f"Guess the number (between 1 and 100): {num} Too high! Try again.")
            attempts += 1
        else:
            print(f"Guess the number (between 1 and 100): {num} Congratulations! You guessed it in {attempts} attempts!")
            break

##
def input_checker(prompt: str) -> int:
    while True:
        num = input(prompt).strip()
        if num.isdigit():
            n = int(num)
            if 1 <= n <= 100:
                return n
            else:
                print(f" --> {n} is out of the range, try again. \n")
        try:
            f = float(num)
        except ValueError:
            print(f" --> '{num}' is invalid input, try again.\n")
        else:
            print(" → Float numbers are not allowed, try again.\n")

def main():
    guessing_game()

if __name__ == "__main__":
    main()