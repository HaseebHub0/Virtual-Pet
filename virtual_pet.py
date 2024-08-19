class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.hunger = 50
        self.health = 100
        self.energy = 50
        self.age = 0

    def feed(self):
        self.hunger -= 10
        self.health += 5
        self.age += 1
        print(f"{self.name} has been fed. Hunger is now {self.hunger}, Health is {self.health}.")

    def play(self):
        if self.energy > 10:
            self.happiness += 10
            self.hunger += 5
            self.energy -= 10
            self.age += 1
            print(f"{self.name} played and is now happier! Happiness is now {self.happiness}, Energy is {self.energy}.")
        else:
            print(f"{self.name} is too tired to play.")

    def sleep(self):
        self.energy += 20
        self.happiness += 5
        self.age += 1
        print(f"{self.name} is sleeping. Energy is now {self.energy}, Happiness is {self.happiness}.")

    def status(self):
        print(f"{self.name} - Happiness: {self.happiness}, Hunger: {self.hunger}, Health: {self.health}, Energy: {self.energy}, Age: {self.age}")

    def check_status(self):
        if self.hunger >= 100:
            print(f"{self.name} is too hungry and has passed away.")
            return False
        elif self.happiness <= 0:
            print(f"{self.name} is too unhappy and has passed away.")
            return False
        elif self.health <= 0:
            print(f"{self.name}'s health has deteriorated too much.")
            return False
        else:
            return True

def main():
    pet_name = input("What would you like to name your virtual pet? ")
    pet = VirtualPet(pet_name)

    while pet.check_status():
        action = input("What would you like to do? (feed/play/sleep/status/exit): ").lower()

        if action == "feed":
            pet.feed()
        elif action == "play":
            pet.play()
        elif action == "sleep":
            pet.sleep()
        elif action == "status":
            pet.status()
        elif action == "exit":
            print(f"Goodbye! {pet.name} will miss you.")
            break
        else:
            print("Please choose a valid action.")

if __name__ == "__main__":
    main()

