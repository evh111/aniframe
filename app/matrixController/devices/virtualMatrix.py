
import numpy as np

from app.matrixController.devices.matrixDevice import MatrixDevice
from app.matrixController.devices.pixel import Pixel
from app import matrixDataTag
from asciimatics.screen import Screen
from asciimatics.screen import ManagedScreen
from asciimatics.event import KeyboardEvent
from time import sleep

class VirtualMatrix(MatrixDevice):

    def __init__(self, _M, _N):
        super().__init__(_M, _N)
        self.currentColumn = 0

        # asciimatics requires we draw the whole screen every frame
        # The real physical matrix device may just use
        # one or two rows at a time instead of the whole screen
        self.currentScreen = np.full((self.M, self.N), Pixel(0, 0, 0))


    def writeTopPixel(self, pixel):
        self.currentScreen[self.currentSection][self.currentColumn] = pixel

    def writeBottomPixel(self, pixel):
        self.currentScreen[self.currentSection + self.M // 2][self.currentColumn] = pixel

    def clock(self):
        self.currentColumn += 1

    def setLatch(self, state):
        """Set latch line high or low (1 or 0)"""

        # The real matrix will be using
        # shift registers to get our clocked bits,
        # so it will automatically be ready to go back to
        # column 0 by the time we latch.
        # Also, the latch and the OutputEnable pin
        # need to stay high WHILE we change sections,
        # so this is being changed to accept a state param
        self.currentColumn = 0
        # The real matrix device class will keep track of
        # whether they're toggled. They should be brought low AFTER
        # we select the address for the next section

    def setOutputEnable(self, state):
        # this is something only the physical device will do
        return 
        

    @ManagedScreen
    def startRendering(self, screen=None):
        """
        Paint the virtual matrix.
        This returns and stops the painting loop if any input
        event is detected.
        """

        screenWidth, screenHeight = screen.dimensions
        numSections = self.M / 2
        while True:
            screen.refresh()

            ev = screen.get_event()
            if isinstance(ev, KeyboardEvent):
                if ev.key_code is ord('q'):
                    return
            for i in range(0, self.M):
                for j in range(0, self.N):
                    # accessing array in row-major but asciimatics
                    # takes (x,y) coords
                    # Mind the british spelling :)
                    pixel = self.currentScreen[i][j]
                    pixelString = pixel.getAsciimaticsChar()
                    screen.print_at(
                            pixel.getAsciimaticsChar(),
                            j * len(pixelString),
                            i,
                            colour=pixel.getAsciimaticsColor(),
                            attr=Screen.A_BOLD
                        )
