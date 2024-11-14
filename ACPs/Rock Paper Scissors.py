import random

def compchoice():
    ch = ["rock", "paper", "scissors"]
    return random.choice(ch)

def winner(userchoice, compchoice):
    if userchoice == compchoice:
        return "Tie!"
    elif (userchoice == "rock" and compchoice == "scissors"):
        return "You win!"
    elif (userchoice == "paper" and compchoice == "rock"):
        return "You win!"
    elif (userchoice == "scissors" and compchoice == "paper"):
        return "You win!"
    else:
        return "Womp womp!"  
    
def game():
    print("Rock, paper, scissors. The classic game.")
    while True:
        userchoice = input("Enter 'rock', 'paper', 'scissors' or 'quit' to exit: ").lower()

        if userchoice == 'quit':
            print("Bye!")
            break

        if userchoice not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Try again!")
            continue

        compschoices = compchoice()

        print(f"\nYou chose: {userchoice}")
        print(f"The computer chose: {compschoices}\n")

        result = winner(userchoice, compschoices)
        print(result)

game()
