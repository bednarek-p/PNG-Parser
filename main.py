import cv2
from decoder import Decoder
import argparse
from RSA import RSA

"""READING PNG FILE"""
def init_png(image_path):
    png_file = open(path , 'rb')
    png_cv2_image = cv2.imread(image_path)

    #Check if file is png file
    if png_file.read(len(Decoder.SIGNATURE)) != Decoder.SIGNATURE:
        raise Exception('Its not PNG file')
    else:
        png_object = Decoder(png_file, png_cv2_image)

    return png_object

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", required=True, help="image file path")
    ap.add_argument("-l", "--chunk_list", nargs='?', const=True, default=False, help="display chunks type list")
    ap.add_argument("--ihdr", nargs='?', const=True, default=False, help="display information of iHDR chunk")
    ap.add_argument("--srgb", nargs='?', const=True, default=False, help="display information of sRGB chunk")
    ap.add_argument("--idat", nargs='?', const=True, default=False, help="display information of iDAT chunk")
    ap.add_argument("--iend", nargs='?', const=True, default=False, help="display information of iEND chunk")
    ap.add_argument("--gama", nargs='?', const=True, default=False, help="display information of gAMA chunk")
    ap.add_argument("--chrm", nargs='?', const=True, default=False, help="display information of cHRM chunk")
    ap.add_argument("--plte", nargs='?', const=True, default=False, help="display information of pLTE chunk")
    ap.add_argument("--fft", nargs='?', const=True, default=False, help="procede Fast Fourier Transformate on png")
    ap.add_argument("--text", nargs='?', const=True, default=False, help="display information of tEXt chunk")
    ap.add_argument("-a", "--anonymization", nargs='?', const=True, default=False, help="proced anonymization")
    ap.add_argument("--encrypt", nargs='?', const=True, default=False, help="encrypt")
    ap.add_argument("--decrypt", nargs='?', const=True, default=False, help="decrypt")
    ap.add_argument("--key_size", default=False, help="key_size")

    args = vars(ap.parse_args())
    path = args["path"]
    chunk_list = args["chunk_list"]
    ihdr = args["ihdr"]
    srgb = args["srgb"]
    idat = args["idat"]
    iend = args["iend"]
    gama = args["gama"]
    chrm = args["chrm"]
    plte = args["plte"]
    fft = args["fft"]
    text = args["text"]
    anonymization = args["anonymization"]
    encrypt = args["encrypt"]
    decrypt = args["decrypt"]
    key_size = args["key_size"]

    png = init_png(path)
    if chunk_list:
        print("LISTA")
        png.print_chunks_type()
        print("-----------------------------\n")

    if ihdr:
        print("IHDR")
        try:
            png.IHDR_print_chunk_formated_data()
        except:
            print("NO IHDR CHUNK IN THIS FILE!")
        print("-----------------------------\n")

    if srgb:
        print("SRGB")
        try:
            png.SRGB_print_chunk_data()
        except:
            print("NO SRGB CHUNK IN THIS FILE!")
        print("-----------------------------\n")

    if idat:
        print("IDAT")
        try:
            png.IDAT_plot_image()
            print("Image displayed using IDAT data.")
        except:
            print("NO IDAT CHUNK IN THIS FILE!")
        print("-----------------------------\n")

    if iend:
        print("IEND")
        try:
            png.IEND_print_chunk_data()
        except:
            print("NO IEND CHUNK IN THIS FILE!")
        print("-----------------------------\n")

    if gama:
        print("GAMA")
        try:
            png.GAMA_print_chunk_formated_data()
        except:
            print("NO GAMA CHUNK IN THIS FILE!")
        print("-----------------------------\n")

    if chrm:
        print("CHRM")
        try:
            png.CHRM_print_chunk_formated_data()
        except:
            print("NO CHRM CHUNK IN THIS FILE!")
        print("-----------------------------\n")

    if plte:
        print("PLTE")
        try:
            #png.PLTE_print_chunk_formated_data()
            png.PLTE_plot_chunk_palette()
        except:
            print("NO PLTE CHUNK IN THIS FILE!")
        print("-----------------------------\n")

    if fft:
        print("FFT")
        try:
            png.Spectrum_show_images()
        except:
            print("ERROR WHILE DOING FFT!")
        print("-----------------------------\n")

    if anonymization:
        print("ANONYMIZATION")
        print("---")
        print("chunks before")
        png.print_chunks_type()
        print("---")

        path = png.anonymization()
        png2 = init_png(path)

        print("---")
        print("chunks after")
        png2.print_chunks_type()
        print("---")
        print("-----------------------------\n")

    if text:
        print("tEXt")
        try:
            png.TEXT_print_chunk_data()
        except:
            print("NO tEXt CHUNK IN THIS FILE")
        print("-----------------------------\n")

    if encrypt:
        print("ENCRYPTION STARTED")
        png.print_chunks_type()
        rsa = RSA(int(key_size))
        print(rsa)
        encrypted_data = rsa.encrypt_ecb(png.IDAT_return_data())
        png.save_encrypted_file('encrypted',encrypted_data)
        decrypted_data = rsa.decrypt_ecb(encrypted_data)
        png.save_encrypted_file('decrypted',decrypted_data)

        # try:
        #     png.print_chunks_type()
        #     rsa = RSA(int(key_size))
        #     print(rsa)
        #     encrypted_data = rsa.encrypt_ecb(png.IDAT_return_data())
        #     png.save_encrypted_file('encrypted',encrypted_data)
        #     decrypted_data = rsa.decrypt_ecb(encrypted_data)
        #     png.save_encrypted_file('decrypted',decrypted_data)
        # except:
        #     print("CANT ENCRYPT!!!")
        print("-----------------------------\n")

    if decrypt:
        print("DECRYPTION STARTED")
        try:
            print("DECRIPTION")
        except:
            print("CANT DECRIPT!!!")
        print("-----------------------------\n")
