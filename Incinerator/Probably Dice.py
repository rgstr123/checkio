from math import factorial
from itertools import combinations_with_replacement, groupby
from functools import reduce

def probability(dice_number, sides, target):

    if dice_number * sides < target:
        return 0

    vsego_ishodov = sides ** dice_number
    koli4estvo_ishodov_target = 0

    for i in combinations_with_replacement(range(1, sides + 1), dice_number):
        if sum(i) == target:
            itemCount = [len([k for k in j]) for _, j in groupby(i)]
            koli4estvo_ishodov_target += factorial(len(i)) / reduce(lambda x, y: x * y, map(factorial, itemCount))

    return koli4estvo_ishodov_target/vsego_ishodov


if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
