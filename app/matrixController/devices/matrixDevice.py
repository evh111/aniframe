
import abc

from app.matrixController.devices.pixel import Pixel

class MatrixDevice(metaclass=abc.ABCMeta):
    """
    Abstract base class for a matrix device.
    See the readme for more explanation.
    Represents an M by N matrix, where
    M is the number of rows and N is the number
    of columns.
    """
    
    @abc.abstractmethod
    def __init__(self, _M, _N):
        self.M = _M
        self.N = _N

    # probably doesn't need to be abstract
    def selectSection(self, section):
        self.currentSection = section

    @abc.abstractmethod
    def writeTopPixel(self, pixel):
        return

    @abc.abstractmethod
    def writeBottomPixel(self, pixel):
        return
    
    @abc.abstractmethod
    def clock(self):
        return

    @abc.abstractmethod
    def latch(self):
        return
