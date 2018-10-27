#!/usr/bin/env python

from fractions import gcd

def FindTotient(Num):
    NumRelPrime = 0
    for i in range(1, Num):
        if (gcd(Num, i) == 1):
            NumRelPrime += 1
    return NumRelPrime

def FindPrivateKey(TotientN, PublicKey):
    for i in range(1, TotientN):
        if (PublicKey * i % TotientN == 1):
            return i


if __name__ == "__main__":
    Totient = FindTotient(2214119)
    print(Totient)
    PrivateKey = FindPrivateKey(Totient, 5)
    print(PrivateKey)

