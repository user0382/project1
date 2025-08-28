def get_sum(a, b):
    """
    Return the sum of a and b.

    :param a: first number
    :type a: int or float
    :param b: second number
    :type b: int or float
    :return: sum of a and b
    :rtype: int or float

    >>> get_sum(2, 3)
    5
    """
    return a + b


def get_names_of_cities(n: int) -> list[str]:
    """
    Return a list of n cities, where n must be 10 or less.

    :param n: Number of cities to return
    :type n: int
    :return: List of cities
    :rtype: list[str]
    :raises ValueError: If n > 10


    >>> get_names_of_cities(3)
    ['tokyo', 'berlin', 'paris']
    >>> get_names_of_cities(11)
    Traceback (most recent call last):
    ...
    ValueError: n must be 10 or less
    """
    cities = [
        "tokyo", "berlin", "paris", "dehli", "london",
        "new york", "beijing", "cape town", "dubai", "moscow"
    ]
    if n <= 10:
        return cities[:n]
    else:
        raise ValueError("n must be 10 or less")
