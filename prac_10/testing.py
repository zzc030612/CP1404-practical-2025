"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)  # 修复函数，使其通过测试


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length  # 修复函数，使其通过测试


def format_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a single full stop.
    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_sentence("this is a test")
    'This is a test.'
    """
    return phrase.capitalize().rstrip(".") + "."  # 实现格式化句子的功能


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"  # 测试通过

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # 测试 Car 类是否正确设置 fuel
    car_with_default_fuel = Car()  # 使用默认 fuel 值
    assert car_with_default_fuel.fuel == 0, "Car does not set default fuel correctly"

    car_with_custom_fuel = Car(fuel=10)  # 使用自定义 fuel 值
    assert car_with_custom_fuel.fuel == 10, "Car does not set custom fuel correctly"


run_tests()

# 运行所有 doctests
doctest.testmod()