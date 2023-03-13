characters = ["a", "b", "c", "d", "e"]


class Game:
    def play(self):
        print("Welcome to the game! ")
        print("Please choose a player: 1 || 2 ? ")
        player_choice = int(input())
        if player_choice == "p1":
            print("Choose a character: ")
            character_choice = int(input())
            for character in characters:
                if character_choice == character:
                    print("Choose your attack move: ")
                    attack_choice = int(input())
        elif player_choice == "p2":
            characters_choice = int(input())
        print("Choose a character: ")
        character_choice = int(input())
        for character in characters:
            if character_choice == character:
                print("Choose your defense move: ")
                attack_choice = int(input())


game = Game()
game.play()
