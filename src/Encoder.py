from Coder import Coder


class Encoder(Coder):
    def encodeSequence(self, sequence: tuple[int, ...], verbose=False) -> int:
        state: int = 0
        if verbose:
            print("ENCODING")
        for symbol in sequence:
            state = self.encodingStep(state, symbol)
            if verbose:
                print("state:", state)
        return state

    def encodingStep(self, state: int, symbol: int) -> int:
        symbolIndex: int = self.symbols.index(symbol)
        assert symbolIndex >= 0
        blockId: int = state // self.counts[symbolIndex]
        slot: int = self.cumCounts[symbolIndex] + \
            state % self.counts[symbolIndex]
        newState = blockId * self.totalCount + slot
        return newState
