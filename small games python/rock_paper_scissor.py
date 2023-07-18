import random


def play():
    user_choice = input("'r' for rock, 's' for scissor, 'p' for paper : ")
    computer_choice = random.choice(["r", "s", "p"])

    if computer_choice == user_choice:
        return "its a tie."

    if user_win(user_choice, computer_choice):
        return "congrats you have won"

    return "you have lost"


def user_win(player, computer):
    if (player == "s" and computer == "p") or (player == "p" and computer == "r") or (
            player == "r" and computer == "s"):
        return True


print(play())
