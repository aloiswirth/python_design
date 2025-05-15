class Borg:

    """
    The Borg design pattern allows multiple instances of a class to share the same state.
    This is done by storing the state in a shared dictionary.
    """
    _shared_data = {}

    def __init__(self):
        self.__dict__ = self._shared_data

class Singleton(Borg):
    """
    The Singleton design pattern ensures that a class has only one instance and provides a global point of access to it. This is done by overriding the __new__ method to control the instantiation of the class.
    """
    # _instance = None
    def __init__(self, **kwargs):
        super().__init__()
        self._shared_data.update(kwargs) # update the shared state and add / modify the attribute dictionary
        
    def __str__(self):
        return str(self._shared_data) # returns the shared attribute dictionary for printing
    
x = Singleton(HTTP = "Hyper Text Transfer Protocol")
print(x)

y = Singleton(SNMP = "Simple Network Management Protocol")
print(y)

def test_singleton():
    """
    Test the Singleton class to ensure that it behaves as a singleton.
    """
    assert x is y, "Singleton instances are not the same!"
    assert x.HTTP == y.HTTP, "HTTP values are not the same!"
    assert x.SNMP == y.SNMP, "SNMP values are not the same!"
    print("All tests passed!")
    return x if x is y else None

test_singleton