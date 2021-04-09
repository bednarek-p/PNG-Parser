import numpy as np

class Plte:
    """Plte chunk  class
    -Chunk contains from 1 to 256 palette entries, each a three-byte series of the form:
            Red:   1 byte (0 = black, 255 = red)
            Green: 1 byte (0 = black, 255 = green)
            Blue:  1 byte (0 = black, 255 = blue)

    -This chunk MUST appear for color type 3
    -This chunk CAN appear for color types 2 and 6
    -This chunk MUST NOT appear for color types 0 and 4

    -There CAN'T be more than one PLTE chunk
    -A chunk length not divisible by 3 is an error.
    """

    def __init__(self,chunk_data):
        self.all_data = chunk_data
        self.palette = []

    def check_chunk_correctness(self, color_type, bit_depth):
        self.parse_data()
        if(color_type == 3):
            print("PLTE chunk MUST appear in this image\n")
        elif(color_type == 2 or color_type == 6):
            print("PLTE chunk CAN appear in this image\n")
        elif(color_type == 0 or color_type == 4):
            raise Exception("PLTE chunk MUST NOT appear in this image")

        if(len(self.all_data) % 3 != 0):
            raise Exception("Chunk length not divisible by 3!")
        if(len(self.palette) > 2**bit_depth):
            raise Exception("Incorrect number of entires in palette.Should be: for example, 2^(4) = 16 for a bit depth of 4")

    def print_data(self):
        print(self.all_data)

    def print_data_formated(self):
        self.parse_data()
        self.palette = np.reshape(self.palette, (-1,3))
        print("\n~~~~~~~~~~~PLTE CHUNK - PALETTE~~~~~~~~~~~~~~")
        print(self.palette)

    def parse_data(self):
        for i in range(0,len(self.all_data), 3):
            raw_pixel= self.all_data[i:i+3]
            pixel = (raw_pixel[0], raw_pixel[1], raw_pixel[2])
            self.palette.append(pixel)

    def get_palette_length(self):
        return len(self.palette)
