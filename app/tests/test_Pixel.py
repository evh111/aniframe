import pytest
from app.matrixController.devices.pixel import *

def test_pixel_colors():
    cyanPixel = Pixel(0, 1, 1)
    assert cyanPixel.asRGBBytes() == (0x00, 0xff, 0xff)
    bluePixel = Pixel(0, 0, 1)
    assert bluePixel.asRGBBytes() == (0x00, 0x00, 0xff)
    whitePixel = Pixel(1, 1, 1)
    assert whitePixel.asRGBBytes() == (0xff, 0xff, 0xff)


def test_pixel_from_binary():
    pix = Pixel.fromBinary(0b101)
    assert pix.r == 1
    assert pix.g == 0
    assert pix.b == 1
    assert pix.asRGBBytes() == (0xff, 0x00, 0xff)
