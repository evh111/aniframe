from gpiozero import OutputDevice

from app.matrixController.devices.matrixDevice import MatrixDevice
from app.matrixController.devices.pixel import Pixel


class GpioMatrix(MatrixDevice):

    def __init__(self, _M, _N):
        super().__init__(_M, _N)
        self.currentColumn = 0

        # Set matrix pins to 'OutputDevice' (pins used on pi)
        self.GND = OutputDevice(6)
        self.R1 = OutputDevice(11)
        self.G1 = OutputDevice(12)
        self.B1 = OutputDevice(15)
        self.R2 = OutputDevice(16)
        self.G2 = OutputDevice(18)
        self.B2 = OutputDevice(22)
        self.A = OutputDevice(26)
        self.B = OutputDevice(24)
        self.C = OutputDevice(21)
        self.OE = OutputDevice(3)
        self.CLK = OutputDevice(5)
        self.LAT = OutputDevice(7)


    def selectSection(self, section):
        self.A.value = bool(section & 0b001)
        self.B.value = bool(section & 0b010)
        self.C.value = bool(section & 0b100)


    def writeTopPixel(self, pixel):
        self.R1.value = pixel.r
        self.G1.value = pixel.g
        self.B1.value = pixel.b


    def writeBottomPixel(self, pixel):
        self.R2.value = pixel.r
        self.G2.value = pixel.g
        self.B2.value = pixel.b


    def clock(self):
        self.CLK.on()
        self.CLK.off()


    def setLatch(self, arg):
        self.LAT.value = arg


    def setOutputEnable(self):
        return
