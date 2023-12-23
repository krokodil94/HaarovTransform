# Image Compression and Decompression

This project implements an image compression and decompression algorithm using [Harova Transformacija (Hartley Transform)] and Huffman coding. It processes images into 8x8 blocks, applies transformations, and compresses the data. The project also supports the reverse process of decompression.

## Features

- Image Padding
- Image Transformation and Zigzag Reordering
- Thresholding for Compression
- Huffman Coding for Compression
- Binary Data Conversion for Storage
- Huffman Decoding for Decompression
- Inverse Process Image for Decompression

## Requirements

- Python 3.x
- NumPy
- imageio

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name

python main.py <input_file> <operation> <output_file> [<threshold>]
