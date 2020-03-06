def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    a = ''
    for i in value:
        a += i.lower()
    b = a.split()
    c = ''.join(b)
    return c == c[::-1]

