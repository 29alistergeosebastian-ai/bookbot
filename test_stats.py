import pytest

from stats import (
    chars_dict_to_sorted_list,
    get_chars_dict,
    get_num_words,
)


def test_get_num_words():
    text = "I probably should've manegd my time better and done this last week but oh well"
    assert get_num_words(text) == 64
    assert get_num_words("") == 0


def test_get_chars_dict():
    text = "AaBb"
    result = get_chars_dict(text)

    assert result["a"] == 2
    assert result["b"] == 2



def test_sort_on():
    my_tuple = ("a", 42)
    assert sort_on(my_tuple) == 42



def test_chars_dict_to_sorted_list():
    my_dict = {"a": 1, "b": 10, "c": 5}
    result = chars_dict_to_sorted_list(my_dict)
    expected = [("b", 10), ("c", 5), ("a", 1)]
    assert result == expected
