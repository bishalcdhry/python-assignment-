import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a random number between 1 and 100. Try to guess it!")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0

    while True:
        try:
            # Prompt the user for a guess
            user_guess = int(input("Enter your guess: "))
            
            # Increment the attempts
            attempts += 1

            # Check if the guess is correct
            if user_guess == secret_number:
                print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
                break
            elif user_guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()