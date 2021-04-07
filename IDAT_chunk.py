import struct # parsing PNG file
import zlib
import matplotlib.pyplot as plot
import numpy as np

class Idat:
    """IDAT chunk  class"""

    def __init__(self, chunk_data, width, height):
        self.all_data = zlib.decompress(chunk_data)
        self.reconstructed_pixel_data = []
        self.width = width
        self.height = height
        self.bytes_per_pixel = 4
        self.stride = self.width * self.bytes_per_pixel

    def print_IDAT_chunk_data(self):
        print(len(self.all_data))

    def plot_decoded_image(self):
        self.update_reconstructed_pixel_data()
        plot.imshow(np.array(self.reconstructed_pixel_data).reshape((self.height,self.width,self.bytes_per_pixel)))
        plot.show()

    def update_reconstructed_pixel_data(self):
        i = 0
        for row in range(self.height): # for each scanline
            filter_type = self.all_data[i] # first byte of scanline is filter type
            i += 1
            for c in range(self.stride): # for each byte in scanline
                filter_x = self.all_data[i]
                i += 1
                if filter_type == 0: # None
                    recon_x = filter_x
                elif filter_type == 1: # Sub
                    recon_x = filter_x + self.recon_a(row, c)
                elif filter_type == 2: # Up
                    recon_x = filter_x + self.recon_b(row, c)
                elif filter_type == 3: # Average
                    recon_x = filter_x + (self.recon_a(row, c) + self.recon_b(row, c)) // 2
                elif filter_type == 4: # Paeth
                    recon_x = filter_x + self.paeth_predict(self.recon_a(row, c), self.recon_b(row, c), self.recon_c(row, c))
                else:
                    raise Exception('unknown filter type: ' + str(filter_type))
                self.reconstructed_pixel_data.append(recon_x & 0xff) # truncation to byt


    def recon_a(self, r, c):
        return self.reconstructed_pixel_data[r * self.stride + c - self.bytes_per_pixel] if c >= self.bytes_per_pixel else 0

    def recon_b(self, r, c):
        return self.reconstructed_pixel_data[(r-1) * self.stride + c] if r > 0 else 0

    def recon_c(self, r, c):
        return self.reconstructed_pixel_data[(r-1) * self.stride + c - self.bytes_per_pixel] if r > 0 and c >= self.bytes_per_pixel else 0

    def paeth_predict(self, a, b, c):
        p = a + b - c
        pa = abs(p - a)
        pb = abs(p - b)
        pc = abs(p - c)
        if pa <= pb and pa <= pc:
            Pr = a
        elif pb <= pc:
            Pr = b
        else:
            Pr = c
        return Pr
