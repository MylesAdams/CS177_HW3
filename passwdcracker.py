import crypt
import sys
from hmac import compare_digest as compare_hash

def GetSalt(String):
    String.split()


if __name__ == "__main__":
    Salts = ['$1$bAc99821$noxC9VXXiMuA0IRfECCVA', 'aa.YVJDT1VruA', '$6$aBcDeF$qn4wyWpQKwjaKGr02tGUWKcFjl0p90b68.oaaJTFX87UzsSWIzq3ZoAEG0/xUQ1kcYTiHkKqye1Qat6vL4rMZ.', '$5$aAbBcCdD$TSZ4rpRmpbVDoas2FK97mHEZwXX.TIUxy.2JeYlmYV.']
    Hashes = ['noxC9VXXiMuA0IRfECCVA', 'YVJDT1VruA', 'qn4wyWpQKwjaKGr02tGUWKcFjl0p90b68.oaaJTFX87UzsSWIzq3ZoAEG0/xUQ1kcYTiHkKqye1Qat6vL4rMZ.', 'TSZ4rpRmpbVDoas2FK97mHEZwXX.TIUxy.2JeYlmYV.']

    Passwords = [None] * 4
    PasswordsSolved = 0

    with open(sys.argv[1]) as f:
        Words = f.readlines()

    Words = [word for word in Words if len(word) >= 6]

    ndx = 0
    while (PasswordsSolved < 4):
        if (ndx % 250 == 0):
            print(str(ndx) + " passwords tested")
        Hash0 = crypt.crypt(Words[ndx], Salts[0])
        Hash1 = crypt.crypt(Words[ndx], Salts[1])
        Hash2 = crypt.crypt(Words[ndx], Salts[2])
        Hash3 = crypt.crypt(Words[ndx], Salts[3])

        if compare_hash(Hash0, Hashes[0]):
            Passwords[0] = Words[ndx]
            print("Found Password:" + Passwords[0])

        if compare_hash(Hash1, Hashes[1]):
            Passwords[1] = Words[ndx]
            print("Found Password:" + Passwords[1])

        if compare_hash(Hash2, Hashes[2]):
            Passwords[2] = Words[ndx]
            print("Found Password:" + Passwords[2])

        if compare_hash(Hash3, Hashes[3]):
            Passwords[3] = Words[ndx]
            print("Found Password:" + Passwords[3])
        ndx += 1
