characters = ["a", "b", "c", "d", "e"]


class Game:
    user_input = input("Choose p1 or p2 ? ")
    if user_input == "p1":
        user_input = input("choose a character:")
        for character in characters:
            if user_input == character:
            user_input = input("Choose your attack move: ")
