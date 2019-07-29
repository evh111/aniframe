
import pytest
from app.matrixController.devices.virtualMatrix import VirtualMatrix

# TODO unit tests for matrix device interface


@pytest.fixture
def virtual_matrix_device():
    return VirtualMatrix(16,32)


def test_setup_matrix(virtual_matrix_device):
        pass
