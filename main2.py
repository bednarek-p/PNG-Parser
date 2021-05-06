import cv2
from decoder import Decoder
import argparse


"""READING PNG FILE"""
def init_png(image_path):
    png_file = open(image_path , 'rb')
    png_cv2_image = cv2.imread(image_path)

    #Check if file is png file
    if png_file.read(len(Decoder.SIGNATURE)) != Decoder.SIGNATURE:
        raise Exception('Its not PNG file')
    else:
        png_object = Decoder(png_file, png_cv2_image)

    return png_object

if __name__ == "__main__":
    png = init_png('images/1.png')
    png.print_chunks_type()
    png.modifty_file()