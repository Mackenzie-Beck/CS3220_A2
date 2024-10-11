from p3worlddata import *
from visualizations import simple_visualization
from mapClass import *
from graphProblemClass import *
from agentsPrograms import *
from deliveryProblemSolvingAgentProClass import *







p3map = myMap(p3world, create_room_tuples())
simple_visualization(p3map)



initial_states = ['Room1_A', 'Room2_A']

import random

initial = random.choice(initial_states)

goal_rooms = get_random_rooms()
goal_rooms.append(initial)

p3problem = GraphProblem(initial, goal_rooms,p3map)

##print(p3problem.initial)
##print(p3problem.goal)
##print(p3problem.actions('Room1_A'))
bfs_program = BestFirstSearchAgentProgramForShow()



dps = deliveryProblemSolvingAgentPro(initial, p3map, goal_rooms, bfs_program)
dps.run()
