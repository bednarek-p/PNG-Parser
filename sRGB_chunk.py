import struct # parsing PNG file

class Srgb:
    """
    sRGB chunk class
    -The present means that image samples conform to sRGB color spaces.
    displayed using the specified rendering intent as defined by the International Color Consortium 
    -This chunk contains:
        - Rendering intent          (1 byte)
            Value:
            - 0 -> Percepual
            - 1 -> Relative colorimetric
            - 2 -> Saturation
            - 3 -> Absolute colorimetric
    """

    def __init__(self, chunk_data):
        self.all_data = chunk_data
        self.rendering_intent = struct.unpack('>B', chunk_data)[0]

    def print_data(self):
        print("Rendering intent: {rendering_intent}".format(rendering_intent = self.rendering_intent))

    def print_formated_data(self):
        print("Rendering intent: {rendering_intent}".format(rendering_intent = self.rendering_intent_format()))

    def rendering_intent_format(self):
        rendering_intent_content = ["Preceptual",
                                    "Relative colorimetirc",
                                    "Saturation",
                                    "Absolute colorimetric",
                                    ]
        
        try:
            return rendering_intent_content[self.rendering_intent]
        except IndexError:
            raise Exception("Invalid rendering intent")