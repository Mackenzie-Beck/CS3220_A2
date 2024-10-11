from p3worlddata import *
from visualizations import simple_visualization
from mapClass import *
from graphProblemClass import *
from agentsPrograms import *
from deliveryProblemSolvingAgentProClass import *







p3map = myMap(p3world, create_room_tuples())
simple_visualization(p3map)



initial_states = ['Room1_A', 'Room1_B']

import random

initial = random.choice(initial_states)

packages_rooms = get_random_rooms()

p3problem = GraphProblem(initial, 'Room2_C',p3map)

##print(p3problem.initial)
##print(p3problem.goal)
##print(p3problem.actions('Room1_A'))
bfs_program = BestFirstSearchAgentProgramForShow()



dps = deliveryProblemSolvingAgentPro(initial, p3map, packages_rooms, bfs_program)
dps.run()