import struct # parsing PNG file

class Ihdr:
    """IHDR chunk  class"""

    def __init__(self, chunk_data):
        self.all_data = chunk_data
        self.width = struct.unpack('>IIBBBBB', chunk_data)[0]
        self.height = struct.unpack('>IIBBBBB', chunk_data)[1]
        self.bit_depth = struct.unpack('>IIBBBBB', chunk_data)[2]
        self.color_type = struct.unpack('>IIBBBBB', chunk_data)[3]
        self.compression_method = struct.unpack('>IIBBBBB', chunk_data)[4]
        self.filter_method = struct.unpack('>IIBBBBB', chunk_data)[5]
        self.interlace_method = struct.unpack('>IIBBBBB', chunk_data)[6]

    def print_data(self):
        print("Width: {width}\nHeight: {height}\nBit depth: {bit_d}".format(width = self.width, height = self.height, bit_d = self.bit_depth))
        print("Color type: {color_t}\nCompression method: {compr_m}".format(color_t = self.color_type, compr_m = self.compression_method))
        print("Filter method: {filter_m}\nInterlace method: {inter_m}\n".format(filter_m = self.filter_method, inter_m = self.interlace_method))
