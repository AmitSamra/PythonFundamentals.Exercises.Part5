def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """

	a = first_string.split()
	#print(a)
	b = second_string.split()
	#print(b)
	return a == b
	