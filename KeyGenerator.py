import random

class KeyGenerator:
    def __init__(self, key_size):
        self.key_size = key_size
        self.n, self.e, self.d = 0,0,0
        self.prime_binary_size = key_binary_size/2 #key is made by two prime numbers

    @classmethod
    def is_prime(self, number):
        """
        Fuction check if the number is prime number
        """
        if number == 1: return False
        if number == 2: return True
        if number == 3: return True
        if number % 2 == 0 or number % 3 == 0: return False
        i = 5
        while i < number/2:
            if number % i == 0 or number % (i+2) == 0: return False
            i = i+6
        return True

    @classmethod
    def prime_generator(self, prime_binary_size):
        while True:
            number = random.randrange(2**(prime_binary_size-1), 2**prime_binary_size-1)
            if KeyGenerator.is_prime(number): return number