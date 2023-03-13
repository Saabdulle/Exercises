class Game: 
    def __init__(self, characters):
        self.characters = [
                    Character("tank", 10, 5, 7, 100, 50),
                    Character("bruiser", 7, 3, 12, 80, 100),
                    Character("healer", 12, 7, 5, 90, 70),
                    Character("mage", 8, 8, 6, 120, 40),
                    Character("fighter", 15, 3, 3, 110, 60)
                ] 
    def start(self):
        print("Epic Terminal Fighting Game")
        print("Select your character: ")
        for i, char in enumerate(self.characters):
            print(f"{i+1}. {character.name}, (HP: {character.health}, Energy: {character.energy})")
        P1_choice = int(input("Player 1: "))
        P2_choice = int(input("Player 2: "))
        print("Start match!!")
        