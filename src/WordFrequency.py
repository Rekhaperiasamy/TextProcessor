class WordFrequency:
    def __init__(self, word: str, frequency: str) -> None:
        self._word = word
        self._frequency = frequency

    def getWord(self) -> str:
        return self._word

    def getFrequency(self) -> int:
        return self._frequency
