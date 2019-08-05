import numpy as np
import pygame
import os

from app.matrixController.devices.matrixDevice import MatrixDevice
from app.matrixController.devices.pixel import Pixel
from app import matrixDataTag
from time import sleep


class VirtualMatrix(MatrixDevice):

    def __init__(self, _M, _N):
        super().__init__(_M, _N)
        self.currentColumn = 0
        self.currentPixels = np.full((_M, _N), Pixel(0, 0, 0))

    # This method only seems necessary in the 'gpioMatrix' class

    def selectSection(self, section):
        self.currentSection = section

    def writeTopPixel(self, pixel):
        self.currentPixels[self.currentSection][self.currentColumn] = pixel

    def writeBottomPixel(self, pixel):
        self.currentPixels[self.currentSection +
                           self.M // 2][self.currentColumn] = pixel

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
        # This is something only the physical device will do
        return

    def startRendering(self):
        """
        Paint the virtual matrix.
        """
        # Set up stuff for drawing the virtual matrix
        pygame.init()
        LEDRadius = 10
        LEDSpacing = 3
        size = (width, height) = (
            self.N * (2 * LEDRadius + LEDSpacing) - LEDSpacing,
            self.M * (2 * LEDRadius + LEDSpacing) - LEDSpacing
        )
        self.screen = pygame.display.set_mode(size)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    os._exit(0)

            for i in range(0, self.M):
                for j in range(0, self.N):
                    # Accessing array in row-major but pygame
                    # takes (x,y) coords
                    pix = self.currentPixels[i][j]
                    color = pix.asRGBBytes()

                    if color == (0, 0, 0):
                        # Use gray on virtual matrix instead of true black
                        color = (20, 20, 20)

                    pixCenter = (
                        j * (2 * LEDRadius + LEDSpacing) + LEDRadius,
                        i * (2 * LEDRadius + LEDSpacing) + LEDRadius
                    )

                    pygame.draw.circle(
                        self.screen,
                        color,
                        pixCenter,
                        LEDRadius,
                        0  # Filled circle
                    )

            pygame.display.flip()
