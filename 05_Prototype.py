
import copy

class Prototype:
    
    def __init__(self):
        self._objects = {}
        
    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj
        
    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]
        
    def clone(self, prototype_name, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(prototype_name))
        obj.__dict__.update(attr)
        return obj
        
class Car:
    def __init__(self):
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"
        
    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.options)
        
c = Car()
prototype = Prototype()
prototype.register_object('skylark',c)

c1 = prototype.clone('skylark')
c2 = prototype.clone('skylark', color='Blue')
c3 = prototype.clone('skylark', name='Mercedes', options='Ex, Sunroof')

print(c1)
print(c2)
print(c3)
