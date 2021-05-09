import random

class KeyGenerator:
    """
    n = pq
    """
    def __init__(self, key_binary_size):
        self.key_binary_size = key_binary_size
        self.p ,self.q, self.e, self.d = 0, 0, 0, 0
        self.prime_binary_size = key_binary_size/2 #key is made by two prime numbers
        self.public_key = self.create_publc_key()
        self.private_key = self.create_private_key()

    @staticmethod
    def is_prime(number):
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

    @staticmethod
    def prime_generator(prime_binary_size):
        while True:
            number = random.randrange(2**(prime_binary_size-1), 2**prime_binary_size-1)
            if KeyGenerator.is_prime(number): return number

    @classmethod
    def create_pq(cls, n_size):
        """ n=pq 
        thoughts:
            beside p and q have correct bit size, there is possibility
            to have n thats q_bit_size + p_bit_size -1. 
        """
        p_size = n_size/2 + random.randrange(int(n_size/100), int(n_size/10)) #to avoid same bit size p and q
        q_size = n_size - p_size
        p,q = 0, 0
        while (p*q).bit_length() != n_size:
            p = cls.prime_generator(p_size)
            q = cls.prime_generator(q_size)
        return p, q

    @classmethod
    def create_e(cls, p, q):
        phi = (p-1)*(q-1)

        if phi >65537: return 65537 #suggested by Pan Doktor on lecture
        else:
            e = phi -1
            while True:
                if cls.is_prime(e): return e
                e = e - 2

    @classmethod
    def greatest_common_divisor(cls, a ,b):
        """ by Euklides """
        if b == 0: return a
        else : return cls.greatest_common_divisor(b, a%b)

    @staticmethod
    def create_d(e, p, q):
        """ d = e^-1 %phi """
        phi = (p-1)*(q-1)
        u1, u2, u3 = 1, 0, e
        v1, v2, v3 = 0, 1, phi
        while v3 != 0:
            q = u3 // v3 
            v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
        return u1 % phi

    def create_publc_key(self):
        self.p ,self.q = self.create_pq(self.key_binary_size)
        self.e = self.create_e(self.p, self.q)
        return (self.e, self.p*self.q)

    def create_private_key(self):
        self.d = self.create_d(self.e, self.p, self.q)
        return (self.d, self.p*self.q)

    def __repr__(self):
        line1 = "#### KEY ####\n"
        line2 = "# bit lenth of data:\n"
        line3 = f"# p: {self.p.bit_length()}\n"
        line4 = f"# q: {self.q.bit_length()}\n"
        line5 = f"# n: {self.private_key[1].bit_length()}\n"
        line6 = f"# e: {self.public_key[0].bit_length()}\n"
        line7 = f"# d: {self.private_key[0].bit_length()}\n"

        return line1 + line2 + line3 + line4 + line5 + line6 + line7