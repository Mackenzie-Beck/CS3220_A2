from collections import defaultdict, Counter


class UniversalDict:
    """A universal dict maps any key to the same value. 
    We use it here as the domains dict for CSPs 
    in which all variables have the same domain.
    >>> d = UniversalDict(list('RGB'))
    >>> d['SA']
    ['R','G','B']
    """

    def __init__(self, value): 
      self.value = value

    def __getitem__(self, key): 
      return self.value

    def __repr__(self): 
      return f'Any from {self.value}'


def different_values_constraint(A, a, B, b):
    """A constraint saying two neighboring variables must differ in value."""
    return a != b



def DinnerConstraint(A, a, B, b):
    """A constraint specifying the dinner problem, where specific people cannot sit next to each other"""
    if (a == "A" and b == "B") or (a == "B" and b == "A"):
        return False
    elif (a == "B" and b == "E") or (a == "E" and b == "B"):
        return False
    elif (a == "C" and b == "B") or (a == "B" and b == "C"):
        return False
    else:
        return True

def parse_neighbors(neighbors):
    """Convert a string of the form 'X: Y Z; Y: Z' into a dict mapping
    regions to neighbors. The syntax is a region name followed by a ':'
    followed by zero or more region names, followed by ';', repeated for
    each region name. If you say 'X: Y' you don't need 'Y: X'.
    >>> parse_neighbors('X: Y Z; Y: Z') == {'Y': ['X', 'Z'], 'X': ['Y', 'Z'], 'Z': ['X', 'Y']}
    True
    """
    dic = defaultdict(list)
    specs = [spec.split(':') for spec in neighbors.split(';')]
    for (A, Aneighbors) in specs:
        A = A.strip()
        for B in Aneighbors.split():
            # had to alter this so that it would not add duplicates
            if B not in dic[A]:  # Check if B is already a neighbor of A
                dic[A].append(B)
            if A not in dic[B]:  # Check if A is already a neighbor of B
                dic[B].append(A)
    return dic


def count(seq):
    """Count the number of items in sequence that are interpreted as true."""
    return sum(map(bool, seq))

def first(iterable, default=None):
    """Return the first element of an iterable; or default."""
    return next(iter(iterable), default)


