import struct # parsing PNG file

class TextChunkBase:
    """
    text chunk base class
    """
    
    def unpack_generator(self, chunk_data):
        data = chunk_data
        for byte in struct.iter_unpack("c", data):
            yield byte[0]

    def get_data_from_chunk(self,chunk_data):
        string = ""
        data=[]
        for byte in self.unpack_generator(chunk_data):
            if byte == b'\x00':
                data.append(string)
                string = ""
            else:
                char = byte.decode(self.ENCODING_TYPE)
                string = string + char
        data.append(string)
        return data