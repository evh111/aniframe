#! usr/bin/python
    
import asciimatics 

from app.matrixController.devices.gpioMatrix import GpioMatrix
from app.matrixController.devices.virtualMatrix import VirtualMatrix

class Controller:
    def __init__(self, useVirtualMatrix=False):
        # We will use a 
        if useVirtualMatrix:
            print("Using virtual matrix for output.")
            self.device = VirtualMatrix(16, 32)
        else:
            self.device = GpioMatrix(16, 32)

        # TODO implement a MatrixArtist and have it handle
        # drawing to a generic matrixdevice object
        
        # TODO spawn a flask server to get animation data
        # to give to the MatrixArtist

    def begin(self):
        self.device.startPainting()
