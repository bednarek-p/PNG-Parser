import struct # parsing PNG file

class Chrm:
    """
    cHRM chunk class
    - This chunk must appear before IDAT & PLTE
    - This chunk is being overwritten by sRGB or iCCP
    - This chunk define device-independent specification of colors.
    - This chunk contains:
        - White Point x         (4 bytes)
        - White Point y         (4 bytes)
        - Red x                 (4 bytes)
        - Red y                 (4 bytes)
        - Green x               (4 bytes)
        - Green y               (4 bytes)
        - Blue x                (4 bytes)
        - Blue y                (4 bytes)

        Values stored in 4 bytes, represents real values times 100 000
    """
    def __init__(self, chunk_data):
        self.all_data = chunk_data
        self.white_point_x =  struct.unpack('>IIIIIIII', chunk_data)[0]
        self.white_point_y =  struct.unpack('>IIIIIIII', chunk_data)[1]
        self.red_x = struct.unpack('>IIIIIIII', chunk_data)[2]
        self.red_y = struct.unpack('>IIIIIIII', chunk_data)[3]
        self.green_x = struct.unpack('>IIIIIIII', chunk_data)[4]
        self.green_y = struct.unpack('>IIIIIIII', chunk_data)[5]
        self.blue_x = struct.unpack('>IIIIIIII', chunk_data)[6]
        self.blue_y = struct.unpack('>IIIIIIII', chunk_data)[7]
    
    def print_data(self):
        print("White Point x: {wpx}".format(wpx=self.white_point_x))
        print("White Point y: {wpy}".format(wpy=self.white_point_y))
        print("Red x: {red_x}".format(red_x=self.red_x))
        print("Red y: {red_y}".format(red_y=self.red_y))
        print("Green x: {green_x}".format(green_x=self.green_x))
        print("Green y: {green_y}".format(green_y=self.green_y))
        print("Blue x: {blue_x}".format(blue_x=self.blue_x))
        print("Blue y: {blue_y}".format(blue_y=self.blue_y))

    def print_formated_data(self):
        print("White Point x: {wpx}".format(wpx=self.format(self.white_point_x)))
        print("White Point y: {wpy}".format(wpy=self.format(self.white_point_y)))
        print("Red x: {red_x}".format(red_x=self.format(self.red_x)))
        print("Red y: {red_y}".format(red_y=self.format(self.red_y)))
        print("Green x: {green_x}".format(green_x=self.format(self.green_x)))
        print("Green y: {green_y}".format(green_y=self.format(self.green_y)))
        print("Blue x: {blue_x}".format(blue_x=self.format(self.blue_x)))
        print("Blue y: {blue_y}".format(blue_y=self.format(self.blue_y)))

    def format(self, value):
        real_value = value / 100000
        return real_value