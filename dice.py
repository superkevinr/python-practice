"""Functions that simulate dice rolls

A die is a function that takes no arguments and returns a number from 1 to n
(inclusive), where n is the number of sides on the die.

Types of dice:

    Dice can be fair, meaning that they produce each possible outcome with equal
    probability.  

    For testing functions that use dice, this file also defines a deterministic
    die, which always cycles among a fixed set of values when it is rolled.

All functions defined in this module are higher-order functions that return dice.  
"""

from random import randint

def make_fair_die(sides=6):
    """Return a die that returns an outcome from 1 to sides with equal chance.

    >>> die = make_fair_die(1)
    >>> die()
    1
    """
    assert type(sides) == int and sides >= 1, 'Illegal value for sides'
    def die():
        return randint(1,sides)
    return die

def make_test_die(*outcomes):
    """Return a die that cycles deterministically through outcomes.

    Note:  This function uses nonlocal variable assignment syntax and list
           structures that have not yet been covered in the course.  Follow this
           usage example, rather than trying to understand the implementation.

    >>> die = make_test_die(1, 2, 3)
    >>> die()
    1
    >>> die()
    2
    >>> die()
    3
    >>> die()
    1
    >>> die()
    2
    """
    assert len(outcomes) > 0, 'You must supply outcomes to make_test_die'
    for o in outcomes:
        assert type(o) == int and o >= 1, 'Outcome is not a positive integer'
    index = len(outcomes) - 1
    def die():
        nonlocal index
        index = (index + 1) % len(outcomes)
        return outcomes[index]
    return die
