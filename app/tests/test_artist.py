import pytest
import json
import numpy as np
from app.matrixController.artist import MatrixArtist
from app.matrixController.devices.pixel import Pixel
from unittest.mock import Mock

ONE_FRAME_RED_4x4 = json.loads("""
{
    "frames": [
        [
            [4,4,4,4],
            [4,4,4,4],
            [4,4,4,4],
            [4,4,4,4]
        ]
    ]
}
""")

def test_artist_parse_one_frame():
    mockDevice = Mock()
    mockDevice.M = 4
    mockDevice.N = 4
    artist = MatrixArtist(mockDevice)
    artist.updateData(ONE_FRAME_RED_4x4)
    assert artist.numSections == 2
    assert np.array_equal(
        artist.frameData,
        np.full((1,4,4), Pixel.fromBinary(0b100))
        )

TWO_FRAMES_RED_BLUE_2x2 = json.loads("""
{
    "frames": [
        [
            [4,4],
            [4,4]
        ],
        [
            [1,1],
            [1,1]
        ]
    ]
}
""")

def test_matrix_artist_parse_two_frames():
    mockDevice = Mock()
    mockDevice.M = 2
    mockDevice.N = 2
    artist = MatrixArtist(mockDevice)
    artist.updateData(TWO_FRAMES_RED_BLUE_2x2)
    assert artist.numSections == 1
    expected = np.concatenate(
        (
            np.full((1,2,2), Pixel.fromBinary(0b100)),
            np.full((1,2,2), Pixel.fromBinary(0b001))
        ),
        0
    )
    assert np.array_equal(artist.frameData, expected)
