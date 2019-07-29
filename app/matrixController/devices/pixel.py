
RED =   0b100
GREEN = 0b010
BLUE =  0b001
BLACK = 0b000
WHITE = 0b111

class Pixel:
    """
    Pixels are simple containers for three booleans:
    red, green, and blue
    This class also contains some convenience 
    methods for drawing "pixels" with asciimatics.
    """

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b


    def asTuple(self):
        return (self.r, self.g, self.b)

    
    def asRGBBytes(self):
        return (self.r * 0xff, self.g * 0xff, self.b * 0xff)

        
    @classmethod
    def fromBinary(cls, value):
        """
        Create a pixel from a value represented with bits
        b2,b1,b0 where the bits are bools for r, g. & b.
        
        Use this as Pixel.fromBinary(value)
        """
        r = bool(value & RED)
        g = bool(value & GREEN)
        b = bool(value & BLUE)
        return cls(r, g, b)


    def __repr__(self):
        return str((self.r, self.g, self.b))

    def __eq__(self, other):
        return (self.r, self.g, self.b) == (other.r, other.g, other.b)
