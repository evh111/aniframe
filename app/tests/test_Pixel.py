
import pytest
from asciimatics.screen import Screen
from app.matrixController.devices.pixel import Pixel

def test_pixel_colors():
    cyanPixel = Pixel(0, 1, 1)
    assert cyanPixel.getAsciimaticsColor() == Screen.COLOUR_CYAN
    bluePixel = Pixel(0, 0, 1)
    assert bluePixel.getAsciimaticsColor() == Screen.COLOUR_BLUE
    whitePixel = Pixel(1, 1, 1)
    assert whitePixel.getAsciimaticsColor() == Screen.COLOUR_WHITE

    # Test black pixels being claculated raw vs asciimatics white
    # for rendering in the virtual matrix
    blackPixel = Pixel(0, 0, 0)
    assert blackPixel.getAsciimaticsColor() == Screen.COLOUR_WHITE
    assert blackPixel._getAsciimaticsColorRaw() == Screen.COLOUR_BLACK

def assert_pixel_from_binary():
    pix = Pixel.fromBinary(0b101)
    assert pix.r == 1
    assert pix.g == 0
    assert pix.b == 1
