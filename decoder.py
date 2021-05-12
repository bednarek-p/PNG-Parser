import cv2
import struct
import zlib

from chunk import read_chunk
from fft_spectrum import Spectrum

from IHDR_chunk import Ihdr
from sRGB_chunk import Srgb
from IDAT_chunk import Idat
from IEND_chunk import Iend
from gAMA_chunk import Gama
from cHRM_chunk import Chrm
from PLTE_chunk import Plte
from tEXt_chunk import Text




class Decoder:
    """Decoder class"""
    SIGNATURE = b'\x89PNG\r\n\x1a\n' #PNG file ALWAYS starts with this signature

    def __init__(self, image, cv2_image):
        self.image = image
        self.cv2_image = cv2_image
        self.chunks_list = []

        while True:
            chunk_type , chunk_data, chunk_crc = read_chunk(self.image)
            self.chunks_list.append((chunk_type, chunk_data, chunk_crc))

            if chunk_type == b'IEND':
                break



    def print_chunks_type(self):
        print("CHUNKS TYPE: ", [chunk_type for chunk_type, chunk_data, chunk_crc in self.chunks_list])

    def get_chunk_from_list(self, chunk):
        """
        Function returns particular chunk data if the one exist in png file,
        if it does not, than ValueError comes out
        """
        for chunk_type, chunk_data, chunk_crc in self.chunks_list:
            if chunk_type == chunk:
                return chunk_data
        raise ValueError("png does not contain ??? chunk")

    def png_contain_chunk(self, chunk):
        """
        Function o check if png contains particular chunk
        """
        chunk_type_list = []
        for chunk_type, chunk_data, chunk_crc in self.chunks_list:
                chunk_type_list.append(chunk_type)
        if chunk in chunk_type_list:
            return True
        else:
            raise ValueError("png does not contain ??? chunk")

    def get_chunk(self, chunk):
        """
        Generator to query particular chunks data
        """
        self.png_contain_chunk(chunk)
        for chunk_type, chunk_data, chunk_crc in self.chunks_list:
            if chunk_type == chunk:
                yield chunk_data

    def Spectrum_show_images(self):
        try:
            image_grayscale = cv2.cvtColor(self.cv2_image, cv2.COLOR_BGR2GRAY)
            spectrum = Spectrum(image_grayscale)
            spectrum.show_spectrum_fft()
        except ValueError:
            raise Exception("Error while showing spectrum")

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

    def IDAT_return_data(self):
        try:
            idat_data = b''.join(chunk_data for chunk_type, chunk_data, chunk_crc in self.chunks_list if chunk_type == b'IDAT')
            image_width = Ihdr(self.chunks_list[0][1]).get_width()
            image_height = Ihdr(self.chunks_list[0][1]).get_height()
            data=Idat(idat_data,image_width,image_height)
            return(data.return_IDAT_chunk_data())
        except ValueError:
            raise Exception("png does not contain IDAT chunk")
    def IDAT_plot_image(self):
        idat_data = b''.join(chunk_data for chunk_type, chunk_data, chunk_crc in self.chunks_list if chunk_type == b'IDAT')
        image_width = Ihdr(self.chunks_list[0][1]).get_width()
        image_height = Ihdr(self.chunks_list[0][1]).get_height()
        data=Idat(idat_data,image_width,image_height)
        data.plot_decoded_image()
        # try:
        #     idat_data = b''.join(chunk_data for chunk_type, chunk_data, chunk_crc in self.chunks_list if chunk_type == b'IDAT')
        #     image_width = Ihdr(self.chunks_list[0][1]).get_width()
        #     image_height = Ihdr(self.chunks_list[0][1]).get_height()
        #     data=Idat(idat_data,image_width,image_height)
        #     data.plot_decoded_image()
        # except ValueError:
        #     raise Exception("png does not contain IDAT chunk")

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
            width = Ihdr(self.get_chunk_from_list(b'IHDR')).get_width()
            height = Ihdr(self.get_chunk_from_list(b'IHDR')).get_height()
            data = Plte(self.get_chunk_from_list(b'PLTE'),width,height)
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

    def PLTE_plot_chunk_palette(self):
        try:
            data = Plte(self.get_chunk_from_list(b'PLTE'))
            color_type = Ihdr(self.get_chunk_from_list(b'IHDR')).get_color_type()
            bit_depth = Ihdr(self.get_chunk_from_list(b'IHDR')).get_bit_depth()
            data.check_chunk_correctness(color_type, bit_depth)
            data.plot_data_palette()
        except ValueError:
            raise Exception("png does not contain PLTE chunk")

    def TEXT_print_chunk_data(self):
        try:
            for chunk in self.get_chunk(b'tEXt'):
                data = Text(chunk)
                print("")
                data.print_data()
        except ValueError:
            raise Exception("png does not contain tEXt chunk")

    def anonymization(self):
        filename = "anonymization_result.png"
        file_ = open(filename, 'wb')
        file_.write(Decoder.SIGNATURE)
        for chunk_type, chunk_data, chunk_crc in self.chunks_list:
            if chunk_type in [b'IHDR', b'IDAT', b'PLTE', b'IEND']:
                chunk_len = len(chunk_data)
                file_.write(struct.pack('>I', chunk_len))
                file_.write(chunk_type)
                file_.write(chunk_data)
                file_.write(struct.pack('>I', chunk_crc))
        file_.close()
        return filename

    def save_encrypted_file(self,file_name,encrypted_data):
        filename = f"{file_name}.png"
        file_ = open(filename, 'wb')
        file_.write(Decoder.SIGNATURE)
        for chunk_type, chunk_data, chunk_crc in self.chunks_list:
            if chunk_type in [b'IDAT']:
                idat_data = bytes(encrypted_data)
                new_data, new_crc = self.compress_IDAT(idat_data)
                chunk_len = len(new_data)
                file_.write(struct.pack('>I', chunk_len))
                file_.write(chunk_type)
                file_.write(new_data)
                file_.write(struct.pack('>I', new_crc))
            else:
                chunk_len = len(chunk_data)
                file_.write(struct.pack('>I', chunk_len))
                file_.write(chunk_type)
                file_.write(chunk_data)
                file_.write(struct.pack('>I', chunk_crc))
        file_.close()
        return filename

    def save_decrypted_file(self,file_name,decrypted_data):
        filename = f"{file_name}.png"
        file_ = open(filename, 'wb')
        file_.write(Decoder.SIGNATURE)
        for chunk_type, chunk_data, chunk_crc in self.chunks_list:
            if chunk_type in [b'IDAT']:
                idat_data = bytes(decrypted_data)
                new_data, new_crc = self.compress_IDAT(idat_data)
                chunk_len = len(new_data)
                file_.write(struct.pack('>I', chunk_len))
                file_.write(chunk_type)
                file_.write(new_data)
                file_.write(struct.pack('>I', new_crc))
            else:
                chunk_len = len(chunk_data)
                file_.write(struct.pack('>I', chunk_len))
                file_.write(chunk_type)
                file_.write(chunk_data)
                file_.write(struct.pack('>I', chunk_crc))
        file_.close()
        return filename

    def compress_IDAT(self,all_data):
        new_data = zlib.compress(all_data,9)
        crc = zlib.crc32(new_data, zlib.crc32(struct.pack('>4s', b'IDAT')))
        return new_data, crc
