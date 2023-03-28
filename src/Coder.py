from itertools import accumulate


class Coder:
    def __init__(self) -> None:
        self.symbols: tuple[int, ...] = tuple()
        self.counts: tuple[int, ...] = tuple()
        self.cumCounts: tuple[int, ...] = tuple()
        self.totalCount: int = 0

    def setStatistics(self, symbols: tuple[int, ...], freqs: tuple[int, ...]) -> None:
        assert len(symbols) == len(freqs)
        self.symbols = symbols
        self.counts = freqs
        self.cumCounts = (0,) + tuple(accumulate(self.counts))
        self.totalCount = sum(freqs)

    def setStatisticsFromSequence(self, sequence: tuple[int, ...]) -> None:
        self.symbols = tuple(set(sequence))
        self.counts = tuple(sequence.count(x) for x in self.symbols)
        self.cumCounts = (0,) + tuple(accumulate(self.counts))
        self.totalCount = sum(self.counts)
