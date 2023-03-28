import random
from Encoder import Encoder
from Decoder import Decoder

random.seed(2)


def getNumberOfBitsFromSeq(seq):
    bits = 0
    for x in seq:
        bits += len(bin(x)) - 2
    return bits


def getNumberOfBitsFromInt(encoding):
    return len(bin(encoding)) - 2


e = Encoder()
d = Decoder()
stats = {'symbols': (1, 2), 'freqs': (1, 4)}
seq = (2, 1, 2, 2, 2)

e.setStatistics(**stats)
d.setStatistics(**stats)
encoding = e.encodeSequence(seq, True)
decodedSeq = d.decode(encoding, 5, True)