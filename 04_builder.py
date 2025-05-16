
class Director():
    """ Director class to manage the construction of a car using a builder."""
    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        """ Construct a car using the builder."""
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

        return None

    def get_car(self):
        return self._builder.car
    
class Builder():
    """ Builder class to define the interface for building a car."""
    def __init__(self):
        self.car = None
    
    def create_new_car(self):
        self.car = Car()
        return self.car
    
class SkyLarkBuilder(Builder):
    """ Builder class to build a SkyLark car."""
    def add_model(self):
        self.car.model = "SkyLark"
    
    def add_tires(self):
        self.car.tires = "All Season Tires"

    def add_engine(self):
        self.car.engine = "V8 Engine"


class Car():
    """Product"""
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None
        
    def __str__(self):
        return '{} | {} | {}'.format(self.model, self.tires, self.engine)



builder = SkyLarkBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()
print(car)