import random

class KeyGenerator:
    """
    n = pq
    """
    def __init__(self, key_size):
        self.key_size = key_size
        self.n, self.e, self.d = 0,0,0
        self.prime_binary_size = key_binary_size/2 #key is made by two prime numbers

    @classmethod
    def is_prime(self, number):
        """
        source: https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python:_Probably_correct_answers
        
        Miller-Rabin primality test.
    
        A return value of False means n is certainly not prime. A return value of
        True means n is very likely a prime.
        """
        #Miller-Rabin test for prime
        if number==0 or number==1 or number==4 or number==6 or number==8 or number==9:
            return False
    
        if number==2 or number==3 or number==5 or number==7:
            return True
        s = 0
        d = number-1
        while d%2==0:
            d>>=1
            s+=1
        assert(2**s * d == number-1)
    
        def trial_composite(a):
            if pow(a, d, number) == 1:
                return False
            for i in range(s):
                if pow(a, 2**i * d, number) == number-1:
                    return False
            return True  
    
        for i in range(8):#number of trials 
            a = random.randrange(2, number)
            if trial_composite(a):
                return False
    
        return True 

    @classmethod
    def prime_generator(self, prime_binary_size):
        while True:
            number = random.randrange(2**(prime_binary_size-1), 2**prime_binary_size-1)
            print(number)
            if KeyGenerator.is_prime(number): return number

