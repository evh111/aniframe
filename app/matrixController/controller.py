from app.matrixController.devices.gpioMatrix import GpioMatrix
from app.matrixController.devices.virtualMatrix import VirtualMatrix
from app.matrixController.artist import MatrixArtist


class Controller:
    """Manages a matrix device to control using the web 
    API endpoints.

    This class sets up a matrix device and is used to
    send it new animation data.
    """

    def __init__(self, useVirtualMatrix=False):
        if useVirtualMatrix:
            print("Using virtual matrix for output.")
            self.device = VirtualMatrix(16, 32)
        else:
            pass
            self.device = GpioMatrix(16, 32)

        self.artist = MatrixArtist(self.device)

    def updateData(self, data):
        """
        Send a new animation to the controller. 
        This is not thread safe on its own.
        The caller should make sure it's okay to
        write data before calling this.
        """
        self.artist.updateData(data)

    def updateFrameRate(self, data):
        self.artist.setFrameRate(data)

    def begin(self):
        self.artist.startPainting()
