from utils import *



# Define variables for each day with three slots each
variables = [
    'mon_1', 'mon_2', 'mon_3',
    'tue_1', 'tue_2', 'tue_3',
    'wed_1', 'wed_2', 'wed_3',
    'thu_1', 'thu_2', 'thu_3',
    'fri_1', 'fri_2', 'fri_3'
]  # Each day now has three slots

# 1 - Practical Programming Methodology
# 2 - Algorithms
# 3 - Operating Systems
# 4 - Intrpduction to File and Database Management
# L means lab, A and B are different sections of the course
domain = ['1_A','1_B', '1LA','1LB','2_A','2_B','2LA','2LB','3_A','3_B','3LA','3LB','4_A','4_B', '4LA','4LB','___','___', '___'] # domain of each variable, representing the sections of courses and labs

weekdays = """
mon_1: mon_2 mon_3 tue_1 tue_2 tue_3; 
mon_2: mon_1 mon_3 tue_1 tue_2 tue_3; 
mon_3: mon_1 mon_2 tue_1 tue_2 tue_3;
tue_1: tue_2 tue_3 mon_1 mon_2 mon_3 wed_1 wed_2 wed_3; 
tue_2: tue_1 tue_3 mon_1 mon_2 mon_3 wed_1 wed_2 wed_3; 
tue_3: tue_1 tue_2 mon_1 mon_2 mon_3 wed_1 wed_2 wed_3;
wed_1: wed_2 wed_3 tue_1 tue_2 tue_3 thu_1 thu_2 thu_3; 
wed_2: wed_1 wed_3 tue_1 tue_2 tue_3 thu_1 thu_2 thu_3; 
wed_3: wed_1 wed_2 tue_1 tue_2 tue_3 thu_1 thu_2 thu_3;
thu_1: thu_2 thu_3 wed_1 wed_2 wed_3 fri_1 fri_2 fri_3; 
thu_2: thu_1 thu_3 wed_1 wed_2 wed_3 fri_1 fri_2 fri_3; 
thu_3: thu_1 thu_2 wed_1 wed_2 wed_3 fri_1 fri_2 fri_3;
fri_1: fri_2 fri_3 thu_1 thu_2 thu_3; 
fri_2: fri_1 fri_3 thu_1 thu_2 thu_3; 
fri_3: fri_1 fri_2 thu_1 thu_2 thu_3
"""  


#2. Develop CSP implementation (based on CSP class)
from CSPS import Schedule_CSP

scheduleCSP = Schedule_CSP(domain, weekdays)

print(scheduleCSP.variables)
print(scheduleCSP.domains)
print(scheduleCSP.neighbors)
print(scheduleCSP.constraints)

print("\n")
print("--------------------------------")
print("\n")
#3. Apply min_conflicts to solve the problem

from algorithms import min_conflicts



min_conflicts(scheduleCSP)
print(scheduleCSP.current)
