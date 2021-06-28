from itertools import count
"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start) -> None:
        self.start = start
        self.counter = count(self.start)
        

    def generate(self):
        """Here we create an iterator using count
        from itertools. We call next on it to return
        the next value from the iterator."""
        while True:
            return next(self.counter)
    

    def reset(self):
        """If the reset method is called, we reset
        the iterator back to the start value that 
        was passed into the instance."""
        self.counter = count(self.start)
    

    def __repr__(self):
        return f'{self.__class__.__name__}: (Start: {self.start}, Next: {self.start + 1})'


sg = SerialGenerator(100)
print(sg.generate())
print(sg.generate())
print(sg.generate())
sg.reset()
print(sg.generate())
print(repr(sg))
