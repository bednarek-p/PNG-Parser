from chunk import read_chunk

"""CONSTANT VARIABLES"""
png_signature = b'\x89PNG\r\n\x1a\n' #PNG file ALWAYS starts with this signature



"""READING PNG FILE"""
file_name = input("Path to your file: ")
png_file = open(file_name , 'rb')

if png_file.read(len(png_signature)) != png_signature:
    raise Exception('Its not PNG file')



"""READING CHUNKS FROM PNG FILE"""
chunks_list = []

while True:
    chunk_type , chunk_data = read_chunk(png_file)
    chunks_list.append((chunk_type))

    if chunk_type == b'IEND':
        break



"""PRINTING CHUNKS INFORMATIONS"""
print ("CHUNKS TYPE: ", chunks_list)
