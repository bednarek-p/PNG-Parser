class Iend:
    """Iend chunk  class
    -The IEND chunk must appear LAST.
    -It marks the end of the PNG datastream.
    -The chunk's data field is EMPTY.
    """

    def __init__(self,chunk_data):
        self.message = "IEND chunk appears in this file at LAST POSITION. \nIEND Chunk data is empty"
        self.chunk_data = chunk_data


    def print_data(self):
        print(self.message)
