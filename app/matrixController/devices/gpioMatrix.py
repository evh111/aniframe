
import gpiozero

from app.matrixController.devices.matrixDevice import MatrixDevice

class GpioMatrix(MatrixDevice):

    def __init__(self, _M, _N):
        super().__init__(_M, _N)

    def selectSection(self, section):
        return
        

    def writeTopPixel(self, pixel):
        return
        

    def writeBottomPixel(self, pixel):
        return

    
    def clock(self):
        return


    def latch(self):
        return

# TODO fill these in with gpio interaction
# should be pretty easy
