# Builder 

The Builder pattern is a creational design pattern that separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

Key Components:

Product
The complex object that is being built.

Abstract Builder
Defines the steps required to build the product. It usually provides abstract methods for creating parts of the product and a method to return the final product.

Concrete Builder
Implements the steps defined in the abstract builder to construct and assemble parts of the product. Each concrete builder can create a different representation of the product.

Director
Controls the construction process. It uses a builder object to construct the product step by step.

``` python
# Product
class House:
    def __init__(self):
        self.walls = None
        self.roof = None

    def __str__(self):
        return f"House with {self.walls} and {self.roof}"

# Abstract Builder
from abc import ABC, abstractmethod

class HouseBuilder(ABC):
    def __init__(self):
        self.house = House()

    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass

    def get_result(self):
        return self.house

# Concrete Builder
class WoodenHouseBuilder(HouseBuilder):
    def build_walls(self):
        self.house.walls = "wooden walls"

    def build_roof(self):
        self.house.roof = "wooden roof"

# Director
class Director:
    def construct(self, builder: HouseBuilder):
        builder.build_walls()
        builder.build_roof()

# Usage
if __name__ == "__main__":
    builder = WoodenHouseBuilder()
    director = Director()
    director.construct(builder)
    house = builder.get_result()
    print(house)
```

Summary:

The Director orchestrates the building process.
The Abstract Builder defines the building steps.
The Concrete Builder implements the steps for a specific product.
The Product is the final object constructed.
This pattern is useful when you need to construct complex objects step by step, possibly with different representations.

