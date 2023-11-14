import pytest
from src.WordFrequencyAnalyzer import WordFrequencyAnalyzer
from src.WordFrequency import WordFrequency


def test_calculate_highest_frequency():
    analyzer = WordFrequencyAnalyzer()

    # Test regular positive flow
    assert analyzer.calculate_highest_frequency(
        "The sun shines over the lake.") == 2

    # Test regular positive flow
    assert analyzer.calculate_highest_frequency(
        "The sun shines over the lake and the mountains.") == 3

    # Test regular positive flow
    assert analyzer.calculate_highest_frequency(
        "Sun sun & sun shines over the lake and the sun.") == 4

    # Test other delimeters
    assert analyzer.calculate_highest_frequency(
        "The-sun!shines@over#the$lake%and^the&mountains.") == 3

    # Test more delimeters
    assert analyzer.calculate_highest_frequency(
        "The1sun2shines3over4the*lake5and6the7mountains.") == 3

    # Test empty input text
    assert analyzer.calculate_highest_frequency("") == 0


def test_calculate_frequency_for_word():
    analyzer = WordFrequencyAnalyzer()

    # Test regular positive flow
    assert analyzer.calculate_frequency_for_word(
        "The sun shines over the lake.", "the") == 2

    # Test regular positive flow
    assert analyzer.calculate_frequency_for_word(
        "The sun shines over the lake.", "lake") == 1

    # Test non existing word
    assert analyzer.calculate_frequency_for_word(
        "The sun shines over the lake.", "mountain") == 0

    # Test other delimeters
    assert analyzer.calculate_frequency_for_word(
        "The-sun!shines@over#the$lake%and^the&mountains.", "the") == 3

    # Test more delimeters
    assert analyzer.calculate_frequency_for_word(
        "The1sun2shines3over4the*lake5and6the7mountains.", "mountains") == 1

    # Test empty input text
    assert analyzer.calculate_frequency_for_word(
        "", "mountains") == 0


def test_calculate_most_frequent_n_words():
    analyzer = WordFrequencyAnalyzer()

    # Test regular positive flow
    result = analyzer.calculate_most_frequent_n_words(
        "The sun shines over the lake.", 3)
    expected = [WordFrequency("the", 2), WordFrequency(
        "lake", 1), WordFrequency("over", 1)]

    for r, e in zip(result, expected):
        assert r.getWord() == e.getWord() and r.getFrequency() == e.getFrequency()

    # Test regular positive flow
    result = analyzer.calculate_most_frequent_n_words(
        "The sun shines over the lake and the mountains.", 2)
    expected = [WordFrequency("the", 3), WordFrequency("and", 1)]
    for r, e in zip(result, expected):
        assert r.getWord() == e.getWord() and r.getFrequency() == e.getFrequency()

    # Test empty input text
    assert analyzer.calculate_most_frequent_n_words("", 3) == []

    # Test zero n words
    assert analyzer.calculate_most_frequent_n_words(
        "The sun shines over the lake and the mountains.", 0) == []
