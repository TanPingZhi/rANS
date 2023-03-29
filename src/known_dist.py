import random
from Encoder import Encoder
from math import gcd
import numpy as np
import matplotlib.pyplot as plt

TRIALS: int = 100
M: int = 1000


def countBits(n: int) -> int:
    return len(bin(n)) - 2


random.seed(0)
def test_ratio(p: float) -> list[float]:
    # p: the true proportion of 2's
    nTwos: int = int(p * M)
    nOnes: int = M - nTwos

    # reduce the ratios in f to simplest form
    g: int = gcd(nOnes, nTwos)
    ratioOnes: int = nOnes // g
    ratioTwos: int = nTwos // g
    stats = {"symbols": (1, 2), "freqs": (ratioOnes, ratioTwos)}
    e = Encoder()
    e.setStatistics(**stats)

    numBitsResults = []

    for trial in range(TRIALS):
        randomSeq = tuple(2 if random.uniform(0, 1) < p else 1 for i in range(M))
        enc = e.encodeSequence(randomSeq)
        numBitsResults.append(countBits(enc))

    return numBitsResults


means: list = []
comps: list = []
compsstds: list = []
stds: list = []
xs = np.array(range(5, 100, 10)) / 100
print("r: ", *xs)
for p in xs:
    res = np.array(test_ratio(p))

    means.append(np.mean(res))
    stds.append(np.std(res))

    comps.append(M / np.mean(res))
    compsstds.append(np.std(M / res))


plt.title("rANS")
plt.ylabel("Average encoding length")
plt.xlabel("Fraction of 2's in a sequence of 1's and 2's")
plt.errorbar(xs, y=means, yerr=stds)
plt.show()
print("average encoding length")
print(*map(lambda x: round(x), means), sep=" & ")
print()

plt.title("rANS")
plt.ylabel("Average compression ratio")
plt.xlabel("Fraction of 2's in a sequence of 1's and 2's")
plt.errorbar(xs, y=comps, yerr=compsstds)
plt.show()

print("average compression ratio")
print(*map(lambda x: round(x, 1), comps), sep=" & ")
