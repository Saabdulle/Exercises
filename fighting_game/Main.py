from Characters import Characters
import random

characters = [
    Character("Healer", 100, 5, 20, 10, 40),
    Character("Mage", 100, 5, 20, 10, 40),
    Character("Marksman", 100, 5, 20, 10, 40)
]

def character_select():
    print("Select Character: ")
    for i, characters in enumerate(characters):
        print(f"{i+1}, {character.name}")
    P1_choice = int(input("Player 1: "))
    P2_choice = int(input("Player 2: "))
    P1 = characters[P1_choice - 1]
    P2 = characters[P2_choice - 1]
    return P1, P2