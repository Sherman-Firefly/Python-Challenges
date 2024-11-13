import random

def num_guess():
    nummies=random.randint(1,20)
    attempts = 0

    print("Guess the number, win nothing!")
    print("It's between 1 and 20")

    while True:
        guess=int(input("Take a guess, any guess! "))
        attempts += 1
        
        if guess < nummies:
            print("Too low! Try again.")
        elif guess > nummies:
            print("Too high! Try again.")
        else:
            print("Good work! The number of attempts is ", attempts)
    
num_guess()