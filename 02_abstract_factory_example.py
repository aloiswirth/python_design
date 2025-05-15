class Dog:
    """
    Dog class representing a dog.
    One of the objects to be returned by the factory method.
    """
    def speak(self):
        return "Woof!"

    def __str__(self):
        return self.__class__.__name__

class DogFactory:
    """
    Factory class to create Dog objects.
    Concrete factory class.
    """
    def get_pet(self):
        """returns a Dog object"""
        return Dog()
    
    def get_food(self):
        """returns Dog food"""
        return "Dog Food"
    
class PetStore:
    """Houses our Abstract Factory"""
    def __init__(self, pet_factory=None):
        """pet_factory is our Abstract Factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the detais of the object returned"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print(f"our pet is {pet}. It makes {pet.speak()} and eats {pet_food}")

# Create Concrete Factory
factory = DogFactory()

# Create a pet store housing the Abstract Factory
shop = PetStore(factory)

# Invoke the utility method to display the details of the pet
shop.show_pet()