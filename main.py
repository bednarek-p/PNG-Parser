import cv2
from decoder import Decoder


"""READING PNG FILE"""
file_name = input("Path to your file: ")
png_file = open(file_name , 'rb')
png_cv2_image = cv2.imread(file_name)

#Check if file is png file
if png_file.read(len(Decoder.SIGNATURE)) != Decoder.SIGNATURE:
    raise Exception('Its not PNG file')
else:
    png = Decoder(png_file, png_cv2_image)
    #png.print_chunks_type()
    # png.IEND_print_chunk_data()
    # png.print_chunks_type()
    # png.IHDR_print_chunk_data()
    # png.IHDR_print_chunk_formated_data()
    # png.IDAT_plot_image()
    # png.IEND_print_chunk_data(
    # png.SRGB_print_chunk_data()
    # png.SRGB_print_chunk_formated_data()
    # png.PLTE_print_chunk_data()
    # png.PLTE_print_chunk_formated_data()
    png.Spectrum_show_images()
    #png.anonymization()

