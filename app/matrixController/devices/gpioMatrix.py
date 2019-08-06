from gpiozero import OutputDevice

from app.matrixController.devices.matrixDevice import MatrixDevice
from app.matrixController.devices.pixel import Pixel


class GpioMatrix(MatrixDevice):

    def __init__(self, _M, _N):
        super().__init__(_M, _N)
        self.currentColumn = 0

        # Set matrix pins to 'OutputDevice'
        self.R1 = OutputDevice(17)
        self.G1 = OutputDevice(18)
        self.B1 = OutputDevice(22)
        self.R2 = OutputDevice(23)
        self.G2 = OutputDevice(24)
        self.B2 = OutputDevice(25)
        self.A = OutputDevice(7)
        self.B = OutputDevice(8)
        self.C = OutputDevice(9)
        self.OE = OutputDevice(2)
        self.CLK = OutputDevice(3)
        self.LAT = OutputDevice(4)

    def selectSection(self, section):
        # Quick hack for strange functionality
        section = (section + 7) % (self.M // 2)
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

    def setOutputEnable(self, arg):
        self.OE.value = arg
