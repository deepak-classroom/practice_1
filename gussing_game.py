import numpy as np
secret = np.random.randint(1, 51)
guesses = []
attempts = 0

print("Guess the number (1-50)!")

while True:
    guess = int(input("Your guess: "))
    guesses.append(guess)
    attempts += 1
    
    if guess == secret:
        print(f"Correct! You got it in {attempts} attempts!")
        print(f"Your guesses: {guesses}")
        print(f"Average guess: {np.mean(guesses):.1f}")
        print(f"Closest guess: {guesses[np.argmin(np.abs(np.array(guesses) - secret))]}")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")