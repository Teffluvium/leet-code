from leet_code.length_of_longest_substring import length_of_longest_substring


def test_length_of_longest_substring_empty_string() -> None:
    assert length_of_longest_substring("") == 0


def test_length_of_longest_substring_single_character() -> None:
    assert length_of_longest_substring("a") == 1


def test_length_of_longest_substring_all_unique() -> None:
    assert length_of_longest_substring("abcdef") == 6


def test_length_of_longest_substring_repeating_characters() -> None:
    assert length_of_longest_substring("abcabcbb") == 3


def test_length_of_longest_substring_all_same_characters() -> None:
    assert length_of_longest_substring("aaaaaa") == 1


def test_length_of_longest_substring_mixed_characters() -> None:
    assert length_of_longest_substring("pwwkew") == 3


def test_length_of_longest_substring_with_spaces() -> None:
    assert length_of_longest_substring("a b c a b c") == 3


def test_length_of_longest_substring_with_special_characters() -> None:
    assert length_of_longest_substring("!@#$%^&*()") == 10


def test_length_of_longest_substring_with_numbers() -> None:
    assert length_of_longest_substring("123123456") == 6
