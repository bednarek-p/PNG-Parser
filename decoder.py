from chunk import read_chunk

from IHDR_chunk import Ihdr
from sRGB_chunk import Srgb
from IDAT_chunk import Idat
from IEND_chunk import Iend
from gAMA_chunk import Gama
from cHRM_chunk import Chrm
from PLTE_chunk import Plte

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

    def get_chunk_from_list(self, chunk):
        """
        Function returns particular chunk data if the one exist in png file,
        if it does not, than ValueError comes out
        """
        for chunk_type, chunk_data in self.chunks_list:
            if chunk_type == chunk:
                return chunk_data
        raise ValueError("png does not contain ??? chunk") #FIX THIS (???) !

    def IHDR_print_chunk_data(self):
        try:
            data = Ihdr(self.get_chunk_from_list(b'IHDR'))
            data.print_data()
        except ValueError:
            raise Exception("png does not contain IHDR chunk")


    def IHDR_print_chunk_formated_data(self):
        try:
            data = Ihdr(self.get_chunk_from_list(b'IHDR'))
            data.print_formated_data()
        except ValueError:
            raise Exception("png does not contain IHDR chunk")


    def IDAT_plot_image(self):
        try:
            idat_data = b''.join(chunk_data for chunk_type, chunk_data in self.chunks_list if chunk_type == b'IDAT')
            image_width = Ihdr(self.chunks_list[0][1]).get_width()
            image_height = Ihdr(self.chunks_list[0][1]).get_height()
            data=Idat(idat_data,image_width,image_height)
            data.plot_decoded_image()
        except ValueError:
            raise Exception("png does not contain IDAT chunk")

    def IEND_print_chunk_data(self):
        try:
            data = Iend(self.get_chunk_from_list(b'IEND'))
            data.print_data()
        except ValueError:
            raise Exception("png does not contain IEND chunk")

    def SRGB_print_chunk_data(self):
        try:
            data = Srgb(self.get_chunk_from_list(b'sRGB'))
            data.print_data()
        except ValueError:
            raise Exception("png does not contain sRGB chunk")

    def SRGB_print_chunk_formated_data(self):
        try:
            data = Srgb(self.get_chunk_from_list(b'sRGB'))
            data.print_formated_data()
        except ValueError:
            raise Exception("png does not contain sRGB chunk")

    def GAMA_print_chunk_data(self):
        try:
            data = Gama(self.get_chunk_from_list(b'gAMA'))
            data.print_data()
        except ValueError:
            raise Exception("png does not contain gAMA chunk")

    def GAMA_print_chunk_formated_data(self):
        try:
            data = Gama(self.get_chunk_from_list(b'gAMA'))
            data.print_formated_data()
        except ValueError:
            raise Exception("png does not contain gAMA chunk")

    def CHRM_print_chunk_data(self):
        try:
            data = Chrm(self.get_chunk_from_list(b'cHRM'))
            data.print_data()
        except ValueError:
            raise Exception("png does not contain cHRM chunk")

    def CHRM_print_chunk_formated_data(self):
        try:
            data = Chrm(self.get_chunk_from_list(b'cHRM'))
            data.print_formated_data()
        except ValueError:
            raise Exception("png does not contain cHRM chunk")

    def PLTE_print_chunk_data(self):
        try:
            data = Plte(self.get_chunk_from_list(b'PLTE'))
            color_type = Ihdr(self.get_chunk_from_list(b'IHDR')).get_color_type()
            bit_depth = Ihdr(self.get_chunk_from_list(b'IHDR')).get_bit_depth()
            data.check_chunk_correctness(color_type, bit_depth)
            data.print_data()
        except ValueError:
            raise Exception("png does not contain PLTE chunk")

    def PLTE_print_chunk_formated_data(self):
        try:
            data = Plte(self.get_chunk_from_list(b'PLTE'))
            color_type = Ihdr(self.get_chunk_from_list(b'IHDR')).get_color_type()
            bit_depth = Ihdr(self.get_chunk_from_list(b'IHDR')).get_bit_depth()
            data.check_chunk_correctness(color_type, bit_depth)
            data.print_data_formated()
        except ValueError:
            raise Exception("png does not contain PLTE chunk")
