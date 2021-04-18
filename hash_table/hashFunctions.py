""" Questo modulo implementa diverse funzioni di hashing."""

import math

class HashFunction_module:
    """ Implementa un semplice modulo."""

    def hash(self, k, m):
        return k % m

class HashFunction_Adv:
    """ Implementa funzioni avanzate di hashing."""

    def numCifre(self, x):
        """Restituisce il numero di cifre in rappresentazione decimale"""
        c = 1
        while True:
            if int(x / math.pow(10, c)) == 0:
                break
            c += 1
        return c

    def cif_k(self, x, k):
        """Restituisce la k-esima cifra"""
        c = self.numCifre(x)
        if k < 0 or k > c:
            raise Exception("k is not in the range!")
        res = x % int(math.pow(10, k))
        res = int(res / int(math.pow(10, k - 1)))
        return res

    def hash(self, k, m):
        mix = m
        numm = self.numCifre(m)
        numk = self.numCifre(k)
        for i in range(0, numk):
            cik = self.cif_k(k, i + 1)
            cimix = self.cif_k(mix, i % numm + 1)
            #si rimpiazza la cifra i di mix con la somma modulo 10 delle \
            #due cifre calcolate sopra
            mix += ((cik + cimix) % 10) * (int(math.pow(10, i % numm))) \
                    - cimix * (int(math.pow(10, i % numm)));
        return mix % m

# DOUBLE HASHING

class doubleHash:
    def hash(self, k, i, m):
        """ Combiniamo due funzioni hash diverse.

            h(k,i)=h1(k)+i*h2(k)  Se m e' primo e h2(k)>=1 e' coprimo rispetto
            ad m, si generano tutte le posizioni. Cio' e' garantito se h2(k)
            e' un intero fra 1 e m-1
        """
        first = k % m
        second = k % (m - 1) + 1
        return (first + i * second) % m

class doubleHash_linearScan:
    def hash(self, k, i, m):
        return (k + i) % m;

class doubleHash_quadraticScan:
    def hash(self, k, i, m):
        """ Scandisce tutti gli elementi per opportuni c1,c2 ed m.
            h(k,i)=(h(k)+c1*i+c2*i^2) mod m.
            """
        return (int(k + 0.5 * i + 0.5 * i * i)) % m;
