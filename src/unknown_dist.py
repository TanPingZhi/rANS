import random
from Encoder import Encoder
from math import gcd, log2
import numpy as np
import matplotlib.pyplot as plt

TRIALS: int = 100
M: int = 1000  # M will match K for this experiment


def countBits(n: int) -> int:
    ans: int = 0
    while n > 0:
        n >>= 1
        ans += 1
    return ans


def test_ratio(p: float) -> list[float]:
    # p: the true proportion of 2's
    # fix constant distribution q = 0.1 to match f = (1, 9)s
    q: float = 0.1
    nOnes: int = int(q * M)
    nTwos: int = M - nOnes

    # reduce the ratios in f to simplest form
    g: int = gcd(nOnes, nTwos)
    ratioOnes: int = nOnes // g
    ratioTwos: int = nTwos // g
    stats = {"symbols": (1, 2), "freqs": (ratioOnes, ratioTwos)}
    e = Encoder()
    e.setStatistics(**stats)

    numBitsResults = []

    for trial in range(TRIALS):
        randomTwosIndices = random.sample(range(M), k=int(p*M))
        randomSeq = [1 for i in range(M)]
        for ri in randomTwosIndices:
            randomSeq[ri] = 2
        randomSeq = tuple(randomSeq)
        enc = e.encodeSequence(randomSeq)
        numBitsResults.append(countBits(enc))

    return numBitsResults


means: list = []
comps: list = []
compsstds: list = []
stds: list = []
xs = np.array(range(5, 100, 10)) / 100
for p in xs:
    res = np.array(test_ratio(p))
    means.append(np.mean(res))
    stds.append(np.std(res))
    comps.append(M / np.mean(res))
    compsstds.append(np.std(M / res))
print("r: ", *xs)

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
