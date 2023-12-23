import unittest
import os
import imageio

from dn2 import (read_image, process_image, treshold,
                              generate_huffman_tree, huffman_encode,
                              convert_to_binary_data, convert_from_binary,
                              huffman_decode, inverse_process_image)
import numpy as np

def create_mock_image(width, height, channels=3):
    """
    Creates a mock image using NumPy.

    Parameters:
    - width (int): Width of the mock image.
    - height (int): Height of the mock image.
    - channels (int): Number of color channels, default is 3 (RGB).

    Returns:
    - mock_image (numpy.ndarray): A mock image represented as a NumPy array.
    """
    # Create a random image with the specified dimensions and channels
    # Values are in the range [0, 255], typical for an 8-bit color depth image
    mock_image = np.random.randint(0, 256, (height, width, channels), dtype=np.uint8)
    return mock_image

class TestReadImage(unittest.TestCase):
    def test_image_padding(self):
        # Create a mock image
        mock_image = create_mock_image(10, 10)  # 10x10 image

        # Save the mock image to a temporary file
        mock_image_path = 'temp_image.png'
        imageio.imwrite(mock_image_path, mock_image)

        # Test the read_image function
        padded_image, height, width = read_image(mock_image_path)

        # Assert that the image dimensions are now multiples of 8
        self.assertEqual(padded_image.shape[0] % 8, 0)
        self.assertEqual(padded_image.shape[1] % 8, 0)

        # Clean up: remove the temporary file
        os.remove(mock_image_path)

if __name__ == '__main__':
    unittest.main()
