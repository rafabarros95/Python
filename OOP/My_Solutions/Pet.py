class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    
    def display_info(self):
        print(f"{self.name} is a {self.species} and is {self.age} years old.")
    
    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old.")

    def make_sound(self):
        if self.species == "Dog".lower():
            print("Woof! Woof!")
        elif self.species == "Cat".lower():
            print("Meow!")
        else:
            print("I am a pet.")

    
def main():
    pet1 = Pet("Fido", "dog", 3)
    pet1.display_info()
    pet1.birthday()
    pet1.make_sound()

    pet2 = Pet("Whiskers", "cat", 5)
    pet2.display_info()
    pet2.make_sound()

if __name__ == "__main__":
    main()