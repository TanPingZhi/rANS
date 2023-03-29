from Encoder import Encoder
from Decoder import Decoder
import random
random.seed(0)

e = Encoder()
d = Decoder()
stats = {'symbols': (1, 2), 'freqs': (1, 4)}
seq = (2, 1, 2, 2, 2)

e.setStatistics(**stats)
d.setStatistics(**stats)
encoding = e.encodeSequence(seq, True)
decodedSeq = d.decode(encoding, len(seq), True)
