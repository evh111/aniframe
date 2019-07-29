import json
import numpy as np
from time import sleep
from loto import LockoutTagout
from app import matrixDataTag
from app.matrixController.devices.pixel import Pixel
from threading import Thread

# Converter function for a json 3D array of 
# color values (not rgb tuples)
# Conversion is easy with numpy magic!
converter = np.vectorize(lambda pix: Pixel.fromBinary(int(pix)))

class MatrixArtist:
    """Handles interpreting animation data and interfacing
    with a matrix device.

    This class consumes json data that represents the frames
    of an animation and handles timing and drawing the
    frames to the passed matrix device.
    """

    def __init__(self, device, frameRate=3):
        self.device = device
        self.frameRate = frameRate  # frames per second
        # framedata is just a single black frame initially
        self.frameData = np.full(
            (1, self.device.M, self.device.N),
            Pixel.fromBinary(0b000)
            )
        self.currentFrameIndex = 0
        self.rowOffset = self.device.M // 2
        self.numSections = self.device.M // 2


    def updateData(self, data):
        # the data is already passed to it as a python dict
        # extract frame data from the json 
        # that the server gave us
        self.frameData = converter(data['frames'])
        self.currentFrameIndex = 0
        


    def startPainting(self):
        """Tells an artist that it should start
        interfacing with its matrix device.

        This causes the matrix device to start undergoing
        its process of havving pixels written, clocking,
        and latching.
        """

        try:
            Thread(target=self.device.startRendering).start()
        except:
            pass
        
        while True:
            self.paintFrame()
            # perod is reciprocal of frequency
            sleep(1.0 / self.frameRate)


    @LockoutTagout(matrixDataTag)
    def paintFrame(self):
        """Send one frame's worth of data
        to the matrix device.

        To prevent other code from corrupting this
        data, lockout-tagout the other code with the
        same tag.
        """
        
        # we're using 3D numpy arrays; essentially an array
        # of frames. So, we access pixel data as
        # frameData[frame][row][column]
        frame = self.frameData[self.currentFrameIndex]
        for section in range(0, self.numSections):
            self.device.selectSection(section)
            topRow = frame[section]
            bottomRow = frame[section + self.rowOffset]
            for column in range(0, self.device.N):
                topPixel = topRow[column]
                bottomPixel = bottomRow[column]
                self.device.writeTopPixel(topPixel)
                self.device.writeBottomPixel(bottomPixel)
                self.device.clock()

            # latch the rows once we wrote to every column
            self.device.latch()

        self.currentFrameIndex += 1
        # possibly wrap frame index back around to beginning frame
        self.currentFrameIndex %= len(self.frameData)
