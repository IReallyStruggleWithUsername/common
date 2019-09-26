"""
This is a list of functions that should be completed.
"""

from typing import Any
from typing import List


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(first_value: Any, second_value: Any) -> bool:
    """
    If @first and @second has same value should return True
    In another case should return False
    """
    if first_value == second_value:
        return True
    else:
        return False


def is_two_objects_has_same_type(first_value: Any, second_value: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    if type(first_value) == type(second_value):
        return True
    else:
        return False


def is_two_objects_is_the_same_objects(first_value: Any, second_value: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    if first_value is second_value:
        return True
    else:
        return False


def multiple_ints(first_value: int, second_value: int) -> int:
    """
    Should calculate product of all args.
    if first_value or second_value is not int should raise ValueError

    Raises:
        ValueError

    Params:
        first_value: value for multiply
        second_value
    Returns:
        Product of elements
    """
    result = first_value*second_value

    if type(first_value) != int or type(second_value) != int:
        raise ValueError
    else:
        return result


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    """
    If possible to convert arguments to int value - convert and multiply them.
    If it is impossible raise ValueError

    Args:
        first_value: number for multiply
        second_value: number for multiply

    Raises:
        ValueError

    Returns: multiple of two numbers.

    Examples:
        multiple_ints_with_conversion(6, 6)
        >>> 36
        multiple_ints_with_conversion(2, 2.0)
        >>> 4
        multiple_ints_with_conversion("12", 1)
        >>> 12
        try:
            multiple_ints_with_conversion("Hello", 2)
        except ValueError:
            print("Not valid input data")
        >>> "Not valid input data"
    """
    try:
        result = int(first_value)*int(second_value)
        return result
    except ValueError:
        raise ValueError("Not valid input data!")
    except TypeError:
        raise TypeError("Not valid input data!")


def is_word_in_text(word: str, text: str) -> bool:
    """
    If text contain word return True
    In another case return False.

    Args:
        word: Searchable substring
        text: Text for searching

    Examples:
        is_word_in_text("Hello", "Hello word")
        >>> True
        is_word_in_text("Glad", "Nice to meet you ")
        >>> False

    """
    if word in text.split():
        return True
    else:
        return False


def some_loop_exercise() -> list:
    """
    Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """
    result = []
    for i in range(13):
        if i != 6 and i != 7:
            result.append(i)
    return result


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """
    data = [i for i in data if i >= 0]
    return data
    pass


def alphabet() -> dict:
    """
    Create dict which keys is alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """
    alph = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    info = []
    p = 1
    for i in alph:
        info.append((p, i))
        p += 1
    result = dict(info)
    return result
#   test asks for numbers as keys so i did that


def simple_sort(data: List[int]) -> List[list]:
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:

    """
    for i in range(len(data)):
        for x in range(i, len(data)):
            if data[i] > data[x]:
                data[i], data[x] = data[x], data[i]
    return data
