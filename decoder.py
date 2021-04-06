from chunk import read_chunk


class Decoder:
    """Decoder class"""
    SIGNATURE = b'\x89PNG\r\n\x1a\n' #PNG file ALWAYS starts with this signature

    def __init__(self, image):
        self.image = image
        self.chunks_list = []

        while True:
            chunk_type , chunk_data = read_chunk(self.image)
            self.chunks_list.append((chunk_type, chunk_data))

            if chunk_type == b'IEND':
                break



    def print_chunks_type(self):
        print("CHUNKS TYPE: ", [chunk_type for chunk_type, chunk_data in self.chunks_list])
        return 0
