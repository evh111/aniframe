from asciimatics.screen import Screen

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

    @classmethod
    def fromBinary(cls, value):
        """
        Create a pixel from a value represented with bits
        b2,b1,b0 where the bits are bools for r, g. & b.
        
        Use this as Pixel.fromBinary(value)
        """
        r = (value & 0b100) >> 2
        g = (value & 0b010) >> 1
        b = (value & 0b001) >> 0
        return cls(r, g, b)


    def _getAsciimaticsColorRaw(self):
        # We can use some bitmasking. See asciimatics.Screen colours
        color =  (
            Screen.COLOUR_RED * self.r   |
            Screen.COLOUR_GREEN * self.g |
            Screen.COLOUR_BLUE * self.b  
        )
        return color


    def getAsciimaticsColor(self):
        # To draw "black" pixels on the black background,
        # we draw white characters but use a diffferent symbol.
        # See getAsciimaticsChar()
        color = self._getAsciimaticsColorRaw()
        if color == Screen.COLOUR_BLACK:
            color = Screen.COLOUR_WHITE
        return color

    def getAsciimaticsChar(self):
        if self._getAsciimaticsColorRaw() == Screen.COLOUR_BLACK:
            return '- '
        return '¤ '


    def __repr__(self):
        return str((self.r, self.g, self.b))

    def __eq__(self, other):
        return (self.r, self.g, self.b) == (other.r, other.g, other.b)
