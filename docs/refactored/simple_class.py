class Animal(metaclass=type):
    def __init__(self, name: str, species: str):
        self.name: str = name
        self.species: str = species

    def speak(self) -> str:
        return f"I am a {self.species} and my name is {self.name}"

if __name__ == "__main__":
    dog = Animal(name="Buddy", species="Dog")
    cat = Animal(name="Whiskers", species="Cat")

    print(dog.speak())
    print(cat.speak())