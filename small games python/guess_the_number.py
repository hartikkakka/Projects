import random


def guess(x):
    random_number = random.randint(1, x)
    guesses = 0
    while guesses != random_number:
        guesses = int(input("enter your guessed number:  "))
        if guesses < random_number:
            print("sorry the number is too low")
        else:
            print("sorry the number is too high")

    print(f"hooray, you guessed the correct number")


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            random_guess = random.randint(low, high)
        else:
            random_guess = low
        feedback = input(f"Is {random_guess} too high (H),too lower(l),or correct(C)?? ").lower()
        if feedback == "h":
            high = random_guess - 1
        elif feedback == "l":
            low = random_guess + 1

    print(f"hooray computer guessed correct number ")


(computer_guess(10))
