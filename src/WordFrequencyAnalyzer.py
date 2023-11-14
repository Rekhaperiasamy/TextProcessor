from typing import List
import re
from collections import Counter

from src.WordFrequency import WordFrequency


class WordFrequencyAnalyzer:
    def __init__(self) -> None:
        pass

    def calculate_highest_frequency(self, text: str):
        word_list = re.findall(
            r'(?<![A-Za-z])[A-Za-z]+(?![A-Za-z])', text.lower())

        if (not word_list):
            return 0

        word_count = self._constructWordCountDict(word_list)

        return max(word_count.values())

    def calculate_frequency_for_word(self, text: str, word: str):
        word_list = re.findall(
            r'(?<![A-Za-z])[A-Za-z]+(?![A-Za-z])', text.lower())

        if (not word_list):
            return 0

        word_count = self._constructWordCountDict(word_list)

        if word.lower() not in word_count:
            return 0
        else:
            return word_count[word.lower()]

    def calculate_most_frequent_n_words(self, text: str, number: str):
        word_list = re.findall(
            r'(?<![A-Za-z])[A-Za-z]+(?![A-Za-z])', text.lower())

        if (not word_list) or number == 0:
            return []

        word_count = self._constructWordCountDict(word_list)

        sorted_word_count = sorted(
            word_count.items(), key=self._sort_dict_by_value_then_key)

        result = []
        for i in range(number):
            result.append(WordFrequency(
                sorted_word_count[i][0], sorted_word_count[i][1])
            )

        return result

    def _constructWordCountDict(self, word_list: list):
        word_count = {}
        for word in word_list:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        return word_count

    def _sort_dict_by_value_then_key(self, item: list):
        return (-item[1], item[0])
