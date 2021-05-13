from KeyGenerator import KeyGenerator

class RSA():
    def __init__(self,key_size):
        self.key_size = key_size
        self.key = KeyGenerator(self.key_size)
        self.private_key = self.key.private_key
        self.public_key = self.key.public_key
        self.encrypted_chunk_size_in_bytes_sub = self.key_size//8 - 1
        self.encrypted_chunk_size_in_bytes = self.key_size//8


    def __str__(self):
        return f"Private:{self.private_key}    Public:{self.public_key}"

    def encrypt_ecb(self,data):
        encrypted_data = []
        self.original_data_len = len(data)

        for i in range(0,len(data),self.encrypted_chunk_size_in_bytes_sub):
            data_to_encrypt_hex = bytes(data[i:i+self.encrypted_chunk_size_in_bytes_sub])
            encrypted_int = pow(int.from_bytes(data_to_encrypt_hex,'big'), self.public_key[0], self.public_key[1])
            encrypted_hex = encrypted_int.to_bytes(self.encrypted_chunk_size_in_bytes,'big')
            for i in range(self.encrypted_chunk_size_in_bytes_sub):
                encrypted_data.append(encrypted_hex[i])
        return encrypted_data

    def decrypt_ecb(self,data):
        decrypted_data = []

        for i in range(0, len(data), self.key_size):
            chunk_to_decrypt_hex = bytes(data[i: i + self.key_size])

            decrypted_int = pow(int.from_bytes(chunk_to_decrypt_hex, 'big'), self.private_key[0], self.private_key[1])
            print(decrypted_int)
            # decrypted_hex = decrypted_int.to_bytes(self.encrypted_chunk_size_in_bytes_sub, 'big')
            # for byte in decrypted_hex:
            #     decrypted_data.append(byte)

        return decrypted_data

    @staticmethod
    def kuba_encrypt_ecb(data, public_key):
        key_size = public_key[1].bit_length()
        encrypted_data = []
        step = key_size//8 -1

        for i in range(0, len(data), step):
            raw_data_bytes = bytes(data[i:i+step])
            raw_data_bytes_length = len(raw_data_bytes)
            raw_data_int = int.from_bytes(raw_data_bytes, 'big')
            encrypted_data_int = pow(raw_data_int, public_key[0], public_key[1])
            encrypted_data_bytes = encrypted_data_int.to_bytes(step+1, 'big')
            encrypted_data_length = len(encrypted_data_bytes)
            for encrypted_byte in encrypted_data_bytes:
                #if byte < raw_data_bytes_length -1:
                encrypted_data.append(encrypted_byte)
                #else: 
                #    encrypted_data.append(int.from_bytes(encrypted_data_bytes[byte:], 'big'))
        return encrypted_data
    
    @staticmethod
    def kuba_decrypt_ecb(data, private_key):
        key_size = private_key[1].bit_length()
        decrypted_data = []
        step = key_size//8

        for i in range(0, len(data), step):
            pack = data[i:i+step]
            encrypted_bytes = b''
            for byte in range(0, len(pack)):
                #if byte < len(pack) - 1:
                encrypted_bytes = encrypted_bytes + pack[byte].to_bytes(1, 'big')
                #else:
                #    encrypted_bytes = encrypted_bytes + pack[byte].to_bytes(se)
            encrypted_data_int = int.from_bytes(encrypted_bytes, 'big')
            #print(encrypted_data_int)
            decrypted_data_int = pow(encrypted_data_int, private_key[0], private_key[1])
            #print(decrypted_data_int)
            decrypted_data_bytes = decrypted_data_int.to_bytes(step-1, 'big')
            for decrypted_byte in decrypted_data_bytes:
                decrypted_data.append(decrypted_byte)
        return decrypted_data
