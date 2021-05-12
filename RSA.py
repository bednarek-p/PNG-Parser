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
