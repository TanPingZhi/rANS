from Coder import Coder


class Decoder(Coder):
    def decode(self, state: int, sequenceSize: int, verbose=False) -> tuple[int, ...]:
        sequence = []
        if verbose:
            print("DECODING")
        for i in range(sequenceSize):
            symbol, state = self.decodingStep(state)
            sequence.append(symbol)
            if verbose:
                print("state:", state)
        sequence.reverse()
        return tuple(sequence)

    def decodingStep(self, encoding: int) -> tuple[int, int]:
        def findSymbolIndex(symbols: tuple[int, ...], cumulFreqs: tuple[int, ...], slot: int) -> int:
            for i in range(len(cumulFreqs)):
                if slot < cumulFreqs[i]:
                    return i - 1
            raise Exception("slot > total frequencies")

        blockId: int = encoding // self.totalCount
        slot: int = encoding % self.totalCount
        symbolIndex: int = findSymbolIndex(self.symbols, self.cumCounts, slot)
        prevState: int = blockId * \
            self.counts[symbolIndex] + slot - self.cumCounts[symbolIndex]

        return self.symbols[symbolIndex], prevState
