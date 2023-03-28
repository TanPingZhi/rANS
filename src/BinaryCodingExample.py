from Encoder import Encoder
from Decoder import Decoder
import random
random.seed(0)

# e = Encoder()
# d = Decoder()
# stats = {"symbols": (1, 2), "freqs": (1, 4)}
# e.setStatistics(**stats)
# d.setStatistics(**stats)
# enc = e.encodeSequence(tuple((2, 1, 2, 2, 2)))



e = Encoder()
d = Decoder()
stats = {"symbols": (1, 2), "freqs": (1, 9)}
e.setStatistics(**stats)
d.setStatistics(**stats)
enc = e.encodeSequence(tuple((1, 2, 2, 2, 2, 2, 2, 2, 2, 2)))
print()
enc = e.encodeSequence(tuple((2, 2, 2, 2, 2, 1, 2, 2, 2, 2)))