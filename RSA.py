import random
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

    @staticmethod
    def encrypt_ecb(data, public_key):
        key_size = public_key[1].bit_length()
        encrypted_data = []
        step = key_size//8 -1

        for i in range(0, len(data), step):
            raw_data_bytes = bytes(data[i:i+step])
            raw_data_int = int.from_bytes(raw_data_bytes, 'big')
            encrypted_data_int = pow(raw_data_int, public_key[0], public_key[1])
            encrypted_data_bytes = encrypted_data_int.to_bytes(step+1, 'big')
            for encrypted_byte in encrypted_data_bytes:
                encrypted_data.append(encrypted_byte)
        return encrypted_data

    @staticmethod
    def decrypt_ecb(data, private_key):
        key_size = private_key[1].bit_length()
        decrypted_data = []
        step = key_size//8

        for i in range(0, len(data), step):
            encrypted_bytes = b''
            for byte in data[i:i+step]:
                encrypted_bytes += byte.to_bytes(1, 'big')
            encrypted_data_int = int.from_bytes(encrypted_bytes, 'big')
            decrypted_data_int = pow(encrypted_data_int, private_key[0], private_key[1])
            decrypted_data_bytes = decrypted_data_int.to_bytes(step-1, 'big')
            for decrypted_byte in decrypted_data_bytes:
                decrypted_data.append(decrypted_byte)
        return decrypted_data



    @staticmethod
    def encrypt_cbc(data, public_key):
        key_size = public_key[1].bit_length()
        encrypted_data = []
        step = key_size//8 -1
        previous = random.getrandbits(key_size)

        for i in range(0, len(data), step):
            raw_data_bytes = bytes(data[i:i+step])
            previous = previous.to_bytes(step + 1, 'big')
            previous = int.from_bytes(previous[:len(raw_data_bytes)], 'big')
            print(previous)
            xor = int.from_bytes(raw_data_bytes, 'big') ^ previous
            encrypted_data_int = pow(xor, public_key[0], public_key[1])
            previous = encrypted_data_int
            encrypted_data_bytes = encrypted_data_int.to_bytes(step+1, 'big')

            for encrypted_byte in encrypted_data_bytes:
                encrypted_data.append(encrypted_byte)
        return encrypted_data
