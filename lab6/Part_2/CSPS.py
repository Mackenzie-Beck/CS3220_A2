from CSPclass import CSPBasic, CSP, DinnerCSP
from utils import *

def MapColoringCSP(colors, neighbors):
    """Make a CSP for the problem of coloring a map with different colors
    for any two adjacent regions. Arguments are a list of colors, and a
    dict of {region: [neighbor,...]} entries. This dict may also be
    specified as a string of the form defined by parse_neighbors."""
    if isinstance(neighbors, str):
        neighbors = parse_neighbors(neighbors)
    return CSP(list(neighbors.keys()), UniversalDict(colors), neighbors, different_values_constraint)


def Dinner_CSP(neighbors, people):
    """Make a CSP for the problem of seating guests at a dinner table, where specific people cannot sit next to each other
    as specified by the assignment"""
    if isinstance(neighbors, str):
        neighbors = parse_neighbors(neighbors)
    return DinnerCSP(list(neighbors.keys()), UniversalDict(people), neighbors, DinnerConstraint)