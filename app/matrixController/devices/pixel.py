
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


    def _getAsciimaticsColorRaw(self):
        # we can use some bitmasking. See asciimatics.Screen colours
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
        return '■ '


    def __repr__(self):
        return str((self.r, self.g, self.b))
