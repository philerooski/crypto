'''
A class for sending secret messages to all your 
instantiated python friends using RSA encryption

Author: Phil Snyder
'''

import random as random
import itertools

class SecretMessage(object):
    def __init__(self):
        pass

    def public_key(self):
        primes = self.generate_primes()
        composite = reduce(lambda x, y : x*y, primes)
        totient = self.generate_totient(primes[0], primes[1])
        exponent = random.sample([x for x in range(3, 100) 
            if x % 2 and self.wiki_egcd(x, totient)[0] == 1 and x < totient], 1)[0] 
        self.decryption_key = self.mod_inverse(exponent, totient)
        self.modulus = composite
        return exponent, composite 

    def encrypt_message(self, text, exponent, modulus):
        ciphertext = " ".join([str(pow(ord(character), exponent, modulus)) for character in text])
        return ciphertext

    def decrypt_message(self, ciphertext, decryption_key, modulus):
        chars = ciphertext.split()
        ans = ""
        for char in chars:
            c = long(char)
            ans += chr(pow(c, decryption_key, modulus))
        return ans
        
    def generate_totient(self, prime1, prime2):
        return (prime1 - 1) * (prime2 - 1)

    def mod_inverse(self, e, m):
        gcd, x, y = self.wiki_egcd(e, m)
        if gcd != 1:
            return ArithmeticError("Modular inverse does not exist")
        else: 
            return x % m

    # extended Euclidean algorithm (WIP)
    def egcd(self, n1, n2):
        larger = max(n1, n2)
        smaller = min(n1, n2)
        s = [0, 1]
        t = [1, 0] 
        r = 1
        while (r != 0):
            if (not larger % smaller):
                r = larger % smaller
                quotient = larger / smaller
                s.append(s[-2] - quotient * s[-1])
                t.append(t[-2] - quotient * t[-1])
                larger = max(smaller, r)
                smaller = min(smaller, r)
            else:
                return r, s[-1], t[-1]

    def wiki_egcd(self, a, b):
        x,y, u,v = 0,1, 1,0
        while a != 0:
            q, r = b//a, b%a
            m, n = x-u*q, y-v*q
            b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
        return gcd, x, y

    def wiki_modinv(self, a, m):
        gcd, x, y = self.wiki_egcd(a, m)
        if gcd != 1:
            return None  # modular inverse does not exist
        else:
            return x % m

    def generate_primes(self):
        reference_range = random.randrange(10, 100)
        primes_to_65000 = self.get_primes_erat(65000)
        potential_primes = [i for i in range(pow(10, 9), pow(10, 9) + pow(10, 3))]
        primes = set()
        for potential in potential_primes:
            prime = True
            for i in primes_to_65000:
                if not potential % i:
                    prime = False
                    break
            if prime:
                primes.add(potential)
        return random.sample(primes, 2)
                
    # super fast prime generator from python cookbook
    def erat2(self):
        D = {}
        yield 2
        for q in itertools.islice(itertools.count(3), 0, None, 2):
            p = D.pop(q, None)
            if p is None:
                D[q*q] = q
                yield q
            else:
                x = p + q
                while x in D or not (x&1):
                    x += p
                D[x] = p
                
    def get_primes_erat(self, n):
        return list(itertools.takewhile(lambda p: p<n, self.erat2()))
