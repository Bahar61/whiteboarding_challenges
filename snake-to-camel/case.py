"""Given a variable name in snake_case, return camelCase of name.

For example::

    >>> snake_to_camel("hi_balloonicorn")
    'hiBalloonicorn'

    >>> snake_to_camel("this_is_test")
    'thisIsTest'

"""


def snake_to_camel(variable_name):
    """Given a variable name in snake_case, return camelCase of name."""

    # START SOLUTION

    words = variable_name.split("_")

    for i in range(1, len(words)):
        words[i] = words[i].capitalize()

    return "".join(words)

# END SOLUTION


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
