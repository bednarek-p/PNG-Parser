import struct # parsing PNG file
import zlib   # decompressing PNG file



def read_chunk(file):
    """
    Read chunks informations
    Returns (chunk_type,chunk_data)

    Build of chunk:
        1. Length - 4 bytes
        2. Chunk Type - 4 bytes
        3. Chunk Data
        4. CRC - Cyclic Redundancy Code - 4 bytes
    """
    chunk_length, chunk_type = struct.unpack('>I4s', file.read(8))
    chunk_data = file.read(chunk_length)
    checksum = zlib.crc32(chunk_data,zlib.crc32(struct.pack('>4s', chunk_type)))
    chunk_crc, = struct.unpack('>I',file.read(4))

    if chunk_crc != checksum:
        raise Exception('Chunk checksum failed {} != {}'.format(chunk_crc , checksum))
    return chunk_type,chunk_data, chunk_crc
