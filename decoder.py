from chunk import read_chunk
from IHDR_chunk import Ihdr
from sRGB_chunk import Srgb
from IDAT_chunk import Idat

import zlib
import cv2
import numpy as np
import matplotlib.pyplot as plt
import copy


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

    def IHDR_print_chunk_data(self):
        data = Ihdr(self.get_chunk_from_list(b'IHDR'))

    def IHDR_print_chunk_formated_data(self):
        data = Ihdr(self.get_chunk_from_list(b'IHDR'))
        data.print_formated_data()

    def IDAT_plot_image(self):
        idat_data = b''.join(chunk_data for chunk_type, chunk_data in self.chunks_list if chunk_type == b'IDAT')#needed for IDAT chunk processing
        image_width = Ihdr(self.chunks_list[0][1]).get_width()
        image_height = Ihdr(self.chunks_list[0][1]).get_height()
        data=Idat(idat_data,image_width,image_height)
        data.plot_decoded_image()

    def SRGB_print_chunk_data(self):
        try:
>>>>>>> 87f4e55fa5675145e17df90a1c024946593b6692
            data = Srgb(self.get_chunk_from_list(b'sRGB'))
            data.print_data()
        except ValueError:
            raise Exception("png does not contain sRGB chunk")

    def SRGB_print_chunk_formated_data(self):
        try:
>>>>>>> 87f4e55fa5675145e17df90a1c024946593b6692
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
