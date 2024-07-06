# simple_class.py

class Animal(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return "I am a {} and my name is {}".format(self.species, self.name)

if __name__ == "__main__":
    dog = Animal("Buddy", "Dog")
    cat = Animal("Whiskers", "Cat")

    print dog.speak()
    print cat.speak()
