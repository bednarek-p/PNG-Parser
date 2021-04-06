from decoder import Decoder


"""READING PNG FILE"""
file_name = input("Path to your file: ")
png_file = open(file_name , 'rb')

#Check if file is png file
if png_file.read(len(Decoder.SIGNATURE)) != Decoder.SIGNATURE:
    raise Exception('Its not PNG file')
else:
    png = Decoder(png_file)
    #png.print_chunks_type()
    png.print_IHDR_chunk_data()
