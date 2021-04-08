import struct # parsing PNG file

class Gama:
    """
    gAMA chunk class
    -This chunk specifies the relationship between the image samples and the desired display output intensity
    -This chunk contains:
        -Gamma          (4 bytes)
            Value:
            - the value stored in 4 bytes represent gamma times 100 000.
              ex. gamma of 0.45455 would be stored as 45455
    """

    def __init__(self, chunk_data):
        self.all_data = chunk_data
        self.gamma = self.rendering_intent = struct.unpack('>I', chunk_data)[0]

    def print_data(self):
        print("Gamma: {gamma}".format(gamma=self.gamma))

    def print_formated_data(self):
        print("Gamma: {gamma}".format(gamma = self.gamma_format()))

    def gamma_format(self):
        real_gamma = self.gamma / 100000
        return real_gamma