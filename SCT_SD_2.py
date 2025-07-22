import numpy as np

def number_guessing(r):
    random_number = np.random.randint(r+1)
    attempts = 0
    guess = None
    i = 0 #lower bound
    j = r #upper bound
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {i} and {j}.")
    while guess != random_number:
        try:
            guess = int(input(f"Enter a between number({i}-{j}): "))
            if guess > random_number:
                print("High")
                if j > guess:
                    j = guess
            elif guess < random_number:
                print("Low")
                if i < guess:
                    i = guess
            attempts += 1
            
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Congratulations! You guessed the number {guess} correctly! In {attempts} Attempts")
if __name__ == "__main__":
    while True:
        try:
            length = int(input("Enter a Upper Limit for the Number Guessing Game (Ex: 100 , 500 , 1000):\n"))
            if length < 1:
                print("Please enter a positive integer.")
                continue
            number_guessing(length)
            #wanna play again!
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again != 'yes':
                print("Thank you for playing! Goodbye!")
                break
        except:
            print("Invalid input. Plese enter a number\n")
    
