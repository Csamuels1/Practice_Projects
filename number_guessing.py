import random


def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:

        try:

            guess = int(input("Guess a Number Between 1 and 100"))
            attempts += 1

            if guess < secret_number:
                print("Too Low! Pleas Try again. ")
            elif guess > secret_number:
                print("Too High! Please Try again. ")
            else:
                print(
                    "Congratulation! You guessed correctly. You had {attempts}attempts. ")

                break

        except ValueError:
            print("Please enter a valid number. ")


if __name__ == "__main__":
    number_guessing_game()
