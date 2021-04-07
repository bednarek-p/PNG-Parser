import struct # parsing PNG file

class Ihdr:
    """IHDR chunk  class
    -This chunk must appear FIRST!
    -This chunk contains:
        - Width              (4 bytes)
        - Height             (4 bytes)
        - Bit Depth          (1 byte)
        - Color type         (1 byte)
            Value:
            - 0 -> Each pixel is a grayscale sample.
            - 2 -> Each pixel is a R,G,B triple.
            - 3 -> Each pixel is a palette index; a PLTE chunk shall appear.
            - 4 -> Each pixel is a grayscale sample followed by an alpha sample.
            - 6 -> Each pixel is a R,G,B triple followed by an alpha sample.
        - Compression method (1 byte)
            Value:
            - 0 -> deflate/inflate compression with a sliding window
            - 1 -> not defined - ERROR
        - Filter method      (1 byte)
            Value:
            - 0 -> Adaptive filtering with five basic filter types
            - 1 -> not defined - ERROR
        - Interlace method   (1 byte)
            Value:
            - 0 -> No interlace method
            - 1 -> Adam7 interlace method
    """

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

    def print_formated_data(self):
        print("Width: {width}\nHeight: {height}\nBit depth: {bit_d}".format(width = self.width, height = self.height, bit_d = self.bit_depth))
        print("Color type: {color_t}\nCompression method: {compr_m}".format(color_t = self.color_type_format(), compr_m = self.compression_method_format()))
        print("Filter method: {filter_m}\nInterlace method: {inter_m}\n".format(filter_m = self.filter_method_format(), inter_m = self.interlace_method_format()))


    def color_type_format(self):
        if self.color_type == 0:
            return "Grayscale"
        elif  self.color_type == 2:
            return "Truecolor"
        elif  self.color_type == 3:
            return "Indexed-color"
        elif  self.color_type == 4:
            return "Grayscale with alpha"
        elif  self.color_type == 6:
            return "Truecolor with alpha"
        else:
            raise Exception("Invalid color type")

    def interlace_method_format(self):
        if self.interlace_method == 0:
            return "No interlace"
        elif self.interlace_method == 1:
            return "Adam7 interlace"
        else:
            raise Exception("Invalid interlace method")

    def compression_method_format(self):
        if self.compression_method == 0:
            return "deflate/inflate compression with a sliding window"
        else:
            raise Exception("Invalid compression_method")

    def filter_method_format(self):
        if self.filter_method == 0:
            return "Adaptive filtering"

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
