from gpiozero import OutputDevice

from app.matrixController.devices.matrixDevice import MatrixDevice
from app.matrixController.devices.pixel import Pixel


class GpioMatrix(MatrixDevice):

    def __init__(self, _M, _N):
        super().__init__(_M, _N)
        self.currentColumn = 0
        self.currentPixels = np.full((_M, _N), Pixel(0, 0, 0))

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

    def preparePin(self, section):
        self.A.value = bool(section & 0b100)
        self.B.value = bool(section & 0b010)
        self.C.value = bool(section & 0b001)


    def selectSection(self, section):
        return


    def writeTopPixel(self, pixel):
        self.currentPixels[self.currentSection][self.currentColumn] = pixel


    def writeBottomPixel(self, pixel):
        self.currentPixels[self.currentSection + self.M // 2][self.currentColumn] = pixel


    def clock(self):
        self.CLK.on()


    def latch(self):
        self.LAT.on()


    def setOutputEnable(self):
        return
