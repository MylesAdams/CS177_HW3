#!/usr/bin/env python

import crypt
import sys
from hmac import compare_digest as compare_hash

# This function takes the number of lines in a file and returns a list
# of ints which indicate how big a chunk of the file we can load into memory
# All chunks will be of size 1m except for the last one which will be Len % 1000000
# I do this because for the larger lists, I cannot load the entire file into
# memory at once.
def CreateChunkSizesList(Len):
    ListSizes = []
    while (Len > 1000000):
        ListSizes.append(1000000)
        Len -= 1000000
    ListSizes.append(Len)
    return ListSizes


# Main function
if __name__ == "__main__":

    # Salts and Hashes for the 4 accounts, they are in order of the shadow file
    # Top line of shadow is the 0th index of Salts and Hashes
    Salts = ['$1$bAc99821', 'aa', '$6$aBcDeF', '$5$aAbBcCdD']
    Hashes = ['$1$bAc99821$noxC9VXXiMuA0IRfECCVA/', 'aa.YVJDT1VruA', '$6$aBcDeF$qn4wyWpQKwjaKGr02tGUWKcFjl0p90b68.oaaJTFX87UzsSWIzq3ZoAEG0/xUQ1kcYTiHkKqye1Qat6vL4rMZ.', '$5$aAbBcCdD$TSZ4rpRmpbVDoas2FK97mHEZwXX.TIUxy.2JeYlmYV.']

    # The first command line argument after file name is which
    # account you would like to try and find the password for
    AcctNum = int(sys.argv[1])

    # Next we find the number of lines (words) in the file
    with open(sys.argv[2]) as f:
        for i, l in enumerate(f):
            pass
        FILELENGTH = i + 1

    # Create a list of Chunk Sizes (number of words) to load into memory
    ChunkSizes = CreateChunkSizesList(FILELENGTH)

    # Open the file
    File = open(sys.argv[2])

    # Iterate over all chunks of file
    for n in range(0, len(ChunkSizes)):

        # Load ChunkSizes[n] number of lines (words) into memory, then strip
        # off the newline and throw away words under 6 characters
        Words = [File.next().rstrip('\n') for i in range(0, ChunkSizes[n])]
        Words = [word for word in Words if len(word) >= 6]

        # Iterate over all words in the Chunk and Hash the word and then
        # check if it matches the account's hash. If it does, we have
        # recovered the password. We print to console and file and exit.
        for Word in Words:
            Hash = crypt.crypt(Word, Salts[AcctNum])

            if compare_hash(Hash, Hashes[AcctNum]):
                print("Found Password: " + Word)
                with open(str(AcctNum) + "_Password.txt", 'w') as f:
                    f.write(Word)
                exit()
