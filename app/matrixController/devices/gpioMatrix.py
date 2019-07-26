
import gpiozero

from app.matrixController.devices.matrixDevice import MatrixDevice

class GpioMatrix(MatrixDevice):

    def __init__(self, _M, _N):
        super().__init__(_M, _N)

    # TODO implement gpio writing
    