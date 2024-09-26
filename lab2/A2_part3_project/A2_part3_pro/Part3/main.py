from agents import ReflexAgentP3
from rules import *
from agentPrograms import *
from part3EnvClass import part3Env

env = part3Env()


agent = ReflexAgentP3()

people = []
import random
from agents import *
from locationsP3 import Room1_A, Room1_B, Room1_C, Room2_A, Room2_B, Room2_C

person_types = [OfficeManager, ITStaff, Student]


for _ in range(10):
    person_type = random.choice(person_types)
    people.append(person_type())



for person in people:
    env.add_thing(person, env.default_location(person))

for location in env.locations:
    print(location)
    for thing in env.list_things_at(location): 
        print(thing.name)