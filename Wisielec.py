import sys
import random

number_of_tries = 5

my_list = ["Brzęczy", "Aneta", "Kamila", "Dodawanie", "Pedał"]
word = random.choice(my_list)
used_letters = []
user_word = []

def find_indexes(word, letter):
    indexes = []


    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

def show_state_of_game():
    print()
    print(user_word)
    print("Pozostało prób:", number_of_tries)
    print("Użyte litery:", used_letters)
    print()

for _ in word:
    user_word.append("_")

while True:
    letter = input("Podaj literę:")
    used_letters.append(letter)

    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print("Nie ma takiej litery.")
        number_of_tries -= 1

        if number_of_tries == 0:
            print("Koniec gry :(")
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter

        if "".join(user_word) == word:
           print("Wygrałeś!!!")
           sys.exit(0)

        show_state_of_game()

        #my_random_choice = random.choice(my_list)