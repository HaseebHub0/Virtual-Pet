class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.hunger = 50

    def feed(self):
        self.hunger -= 10
        print(f"{self.name} has been fed. Hunger is now {self.hunger}.")

    def play(self):
        self.happiness += 10
        self.hunger += 5
        print(f"{self.name} played and is now happier! Happiness is now {self.happiness}.")

    def status(self):
        print(f"{self.name} - Happiness: {self.happiness}, Hunger: {self.hunger}")

def main():
    pet_name = input("What would you like to name your virtual pet? ")
    pet = VirtualPet(pet_name)

    while True:
        action = input("What would you like to do? (feed/play/status/exit): ").lower()

        if action == "feed":
            pet.feed()
        elif action == "play":
            pet.play()
        elif action == "status":
            pet.status()
        elif action == "exit":
            print(f"Goodbye! {pet.name} will miss you.")
            break
        else:
            print("Please choose a valid action.")

if __name__ == "__main__":
    main()
