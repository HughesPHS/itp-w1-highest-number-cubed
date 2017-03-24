"""This is the entry point of the program."""


def highest_number_cubed(limit):
    i = 1
    while (i ** 3) < limit:
        i += 1
    return i - 1
