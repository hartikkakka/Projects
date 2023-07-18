import random
from project_file.all_words import words
import string


def get_valid_words(letters):
    word = random.choice(letters)
    while "-" in letters or " " in letters:
        word = random.choice(letters)

    return word.upper()


def hangman():
    word = get_valid_words(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()

    while len(word_letter) > 0 :
        print("you have used these letter : ", " ".join(used_letter))

        word_list = [letter if letter in used_letter else '-' for letter in word]
        print("current words: ", " ".join(word_list))

        user_letter = input('guess a letter : ').upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
                print("")

        elif user_letter in used_letter:
            print("you have already guessed that word.")
        else:
            print('invalid character.')

    print(f"yay you have guessed the '{word}' correctly ")


hangman()
