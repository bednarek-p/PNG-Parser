from chunk import read_chunk
from IHDR_chunk import Ihdr
from sRGB_chunk import Srgb
import zlib
import cv2
import numpy as np
import matplotlib.pyplot as plt
import copy
import logging
logging.basicConfig(level=logging.DEBUG)

class Decoder:
    """Decoder class"""
    SIGNATURE = b'\x89PNG\r\n\x1a\n' #PNG file ALWAYS starts with this signature

    def __init__(self, image):
        self.image = image
        self.chunks_list = []

        while True:
            chunk_type , chunk_data = read_chunk(self.image)
            self.chunks_list.append((chunk_type, chunk_data))

            if chunk_type == b'IEND':
                break



    def print_chunks_type(self):
        print("CHUNKS TYPE: ", [chunk_type for chunk_type, chunk_data in self.chunks_list])

    def print_IHDR_chunk_data(self):
        data = Ihdr(self.chunks_list[0][1])
        data.print_data()

    def print_IHDR_chunk_formated_data(self):
        data = Ihdr(self.chunks_list[0][1])
        data.print_formated_data()

    def print_sRGB_chunk_data(self):
        try: 
            data = Srgb(self.get_chunk_from_list(b'sRGB'))
            data.print_data()
        except ValueError:
            raise Exception("png does not contain sRGB chunk")

    def print_sRGB_chunk_formated_data(self):
        try: 
            data = Srgb(self.get_chunk_from_list(b'sRGB'))
            data.print_formated_data()
        except ValueError:
            raise Exception("png does not contain sRGB chunk")

    def get_chunk_from_list(self, chunk):
        """
        Function returns particular chunk data is the one exist in png file,
        if it does not, than ValueError comes out
        """
        for chunk_type, chunk_data in self.chunks_list:
            if chunk_type == chunk:
                return chunk_data
        raise ValueError("png does not contain sRGB chunk")
