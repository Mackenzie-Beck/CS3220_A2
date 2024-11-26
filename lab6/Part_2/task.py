


#1. Formulate the problem (presented above) as a CSP problem.
from utils import *


variables = [0,1,2,3,4,5] #list of variables, representing the seats around the table
dinnerproblemdomain = UniversalDict(list('ABCDE'))  #domain of each variable is the same, representing the people

dinnertable = "0: 1 5; 1: 2; 2: 3; 3: 4; 4: 5; 5:"





#2. Develop CSP implementation (based on CSP class)
from CSPS import Dinner_CSP
dinnerCSP = Dinner_CSP(dinnertable)
print(dinnerCSP.variables)
print(dinnerCSP.domains)
print(dinnerCSP.neighbors)
print(dinnerCSP.constraints)

print("\n")
print("--------------------------------")
print("\n")
#3. After running constraint propagation once without search, do any of the domains change? (Apply AC-3 for the answer)
from algorithms import AC3
AC3(dinnerCSP)
print(dinnerCSP.curr_domains)
print("\n")
print("--------------------------------")
print("\n")
#none of the domains change

#4. Apply a backtracking search algorithm to solve ths problem
from algorithms import backtracking_search
result = backtracking_search(dinnerCSP)
print(result)

