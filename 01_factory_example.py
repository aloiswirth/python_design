class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof!"
    
class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Meow!"

def get_pet(pet="dog" ):
    """Factory method to create a pet object."""
    pets = dict(dog=Dog("Buddy") , cat=Cat("Kitty"))
    return pets.get(pet)

e = get_pet("elephant")  # This will return None
if e is None:
    print("No such pet available.")
f = get_pet()
print(f.speak())  # Output: Woof!
d = get_pet("dog")
print(f'{d.name} makes {d.speak()}')  # Output: Buddy makes Woof!
c = get_pet("cat")
print(c.speak())  # Output: Meow!