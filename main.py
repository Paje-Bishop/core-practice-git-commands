import pytest

def silly_sum():
    """ reads numbers from the user
        summing as we go until either
        the user enters 0, or
        the sum reaches or exceeds 1000
    """
    num = int(input('Please enter a number => '))
    sum = 0

    while num != 0:
        sum += num
        if sum >= 1000:
            break

        num = int(input('Please enter a number => '))

    return sum
    
def always_returns_true():
    return True


def test_always_returns_true():
    assert always_returns_true()
