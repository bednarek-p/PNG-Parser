import struct # parsing PNG file

from text_chunk_base_class import TextChunkBase

class Text(TextChunkBase):
    """
    iTXt chunk class
    """
    ENCODING_TYPE = 'latin-1'

    def __init__(self, chunk_data):
        self.all_data = chunk_data
        self.keyword, self.text = self.get_data_from_chunk(chunk_data)

    def print_data(self):
        print("Keyword: {keyword}".format(keyword=self.keyword))
        print("Text: {text}".format(text=self.text))