from typing import List, Dict, Tuple
import re

from src.WordFrequency import WordFrequency


class WordFrequencyAnalyzer:
    '''
    This class analyses the given text and performs word frequency calculations 
    '''

    def calculate_highest_frequency(self, text: str) -> int:
        '''
        This method calculates the highest word frequency 
        and returns the count of the highest frequency from the given text

        Args:
            text (str): Text that needs to be analysed

        Returns:
            highest_frequency (int): count of the highest frequency
        '''

        word_list = self._constructWordList(text)

        if (not word_list):
            return 0

        word_count = self._constructWordCountDict(word_list)

        return max(word_count.values())

    def calculate_frequency_for_word(self, text: str, word: str) -> int:
        '''
        This method calculates the frequency of the given word in the given text

        Args:
            text (str): Text that needs to be analysed
            word (str): Word whose frequency needs to be counted

        Returns:
            frequency_count (int): count of the given word's frequency
        '''

        word_list = self._constructWordList(text)

        if (not word_list):
            return 0

        word_count = self._constructWordCountDict(word_list)

        if word.lower() not in word_count:
            return 0
        else:
            return word_count[word.lower()]

    def calculate_most_frequent_n_words(self, text: str, number: str) -> List[WordFrequency]:
        '''
        This method calculates the most frequent n number of words

        Args:
            text (str): Text that needs to be analysed
            number (int): Number of frequenct words that needs to be returned

        Returns:
            most_frequent_n_words (List[WordFrequency]): List of most frequent words with length 'n'
        '''

        word_list = self._constructWordList(text)

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

    def _constructWordList(self, text: str) -> List[str]:
        '''
        This method splits the given text into words.

        Defintion of word - a word is represented by a sequence of one or more
        characters between 'a' and 'z' or between 'A and 'Z'). 
        For example “agdfBh”. 

        Args:
            text (str): Text that needs to be processed

        Returns:
            list_of_words (List[str]): List of words that are split from the given text
        '''

        word_list = re.findall(
            r'(?<![A-Za-z])[A-Za-z]+(?![A-Za-z])', text.lower())

        return word_list

    def _constructWordCountDict(self, word_list: list) -> Dict[str, int]:
        '''
        This method builds a dictionary of words and their respective count from the given list of words.

        Args:
            word_list (List[str]): List of words that needs to be converted to dict

        Returns:
            word_count_dict (Dict[str, int]): Dictionary of words with their respective count
        '''

        word_count = {}
        for word in word_list:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        return word_count

    def _sort_dict_by_value_then_key(self, item: list) -> Tuple:
        return (-item[1], item[0])
