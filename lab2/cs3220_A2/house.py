from environmentClass import Environment
from agentClass import Agent
from locations import *

import random

class House(Environment):
    def __init__(self):
        super().__init__()
        self.things = [] # Empty list of things in the environment.
    
    def percept(self, agent):
        #Returns a list of things that are in our agent's location.
        things = self.list_things_at(agent.location)
        return agent.location, things
    
    #POSSIBLE ISSUE IN THIS METHOD
    def execute_action(self, agent, action):
        #Check if agent alive, if so, execute action.
        if self.is_agent_alive(agent):
            percepted = self.list_things_at(agent.location)
            marked = []
            #Moving loses 1 performance.
            if action == 'MoveRight':
                self.moveToRight(agent)
                agent.performance -= 1
            elif action == 'MoveLeft':
                self.moveToLeft(agent)
                agent.performance -= 1
            #Drinking milk gains 5 performance and eliminates the milk from the environment.
            elif action == 'Drink':
                for thing in percepted:
                    if thing.name == 'Milk':
                        agent.performance += 5
                        marked.append(thing)
            #Eating a mouse gains 10 performance and eliminates the mouse from the environment. Only a strong cat can catch a mouse.
            elif action == 'Eat' and agent.performance >= 3:
                for thing in percepted:
                    if thing.name == 'Mouse':
                        agent.performance += 10
                        marked.append(thing)
            #Fighting a dog and winning (super strong cat) gains 20 performance and eliminates the dog from the environment.
            elif action == 'Fight' and agent.performance >= 10:
                for thing in percepted:
                    if thing.name == 'Dog':
                        agent.performance += 20
                        marked.append(thing)
            #Fighting a dog and losing (weak cat) loses 10 performance and the dog remains in the environment.
            elif action == 'Fight' and agent.performance < 10:
                for thing in percepted:
                    if thing.name == 'Dog':
                        agent.performance -= 10
            #Removal of marked things from the environment.
            for thing in marked:
                self.remove_thing(thing)
            self.update_agent_alive(agent)
    
    def default_location(self, thing):
        """Agents start in either location at random."""
        return random.choice([loc_A, loc_B, loc_C, loc_D, loc_E])
    
    #Returns true if all agents in the environment are dead.
    def is_done(self):
        return not any(self.is_agent_alive(agent) for agent in self.things if isinstance(agent, Agent))
    
    def step(self):
        #Run the environment for one time step.
        if not self.is_done():
            actions = []
            for agent in self.things:
                if isinstance(agent, Agent):
                    if agent.alive:
                        action=agent.program(self.percept(agent))
                        print("{} agent percepted {} at {}.".format(agent, self.percept(agent)[1], self.percept(agent)[0]))
                        print("Agent decided to {}.".format(action))
                        actions.append((agent, action))
                    else:
                        actions.append("")
            for (agent, action) in actions:
                self.execute_action(agent, action)
                print(agent.performance)
        else:
          print("There is no one here who could work...")

    #run() inherited from Environment

    #Adding the thing in a random location.
    def add_thing(self, thing):
        thing.location = self.default_location(thing)
        marked = []
        allow = True
        for thing2 in self.things:
            if thing.name == 'mouse':
                #If mouse and milk are in the same room, milk gets marked for removal.
                if (thing.location == thing2.location) and thing2.name == 'milk':
                    marked.append(thing2)
                #If mouse and dog are in the same room, mouse moves to an adjacent room.
                elif (thing.location == thing2.location) and thing2.name == 'dog':
                    moveDir = random.choice(['MoveRight', 'MoveLeft'])
                    if moveDir == 'MoveRight':
                        oldLocation = thing.location
                        self.moveToRight(thing)
                        if thing.location == oldLocation:
                            thing.location = loc_D
                    else:
                        oldLocation = thing.location
                        self.moveToLeft(thing)
                        if thing.location == oldLocation:
                            thing.location = loc_B
            elif thing.name == 'milk':
                #If milk and mouse are in the same room, milk gets set to not be added.
                if (thing.location == thing2.location) and thing2.name == 'mouse':
                    allow = False
            elif thing.name == 'dog':
                #If dog and mouse are in the same room, mouse moves to an adjacent room.
                if (thing.location == thing2.location) and thing2.name == 'mouse':
                    moveDir = random.choice(['MoveRight', 'MoveLeft'])
                    if moveDir == 'MoveRight':
                        oldLocation = thing2.location
                        self.moveToRight(thing2)
                        if thing2.location == oldLocation:
                            thing2.location = loc_D
                    elif moveDir == 'MoveLeft':
                        oldLocation = thing2.location
                        self.moveToLeft(thing2)
                        if thing2.location == oldLocation:
                            thing2.location = loc_B
        #Removes the things from the house marked for removal.
        for thing2 in marked:
            self.remove_thing(thing2)
        #Adds the thing to the house (if applicable).
        if allow == True:
            self.things.append(thing)

    def moveToRight(self, thing):
        if thing.location != loc_E:
            if thing.location == loc_A:
                thing.location = loc_B
            elif thing.location == loc_B:
                thing.location = loc_C
            elif thing.location == loc_C:
                thing.location = loc_D
            else:
                thing.location = loc_E
    
    def moveToLeft(self, thing):
        if thing.location != loc_A:
            if thing.location == loc_B:
                thing.location = loc_A
            elif thing.location == loc_C:
                thing.location = loc_B
            elif thing.location == loc_D:
                thing.location = loc_C
            else:
                thing.location = loc_D
        

    #Output the list of things with their locations
    def list_things_location(self):
        for thing in self.things:
            print(thing, thing.location)

    #Returns a list of things at the given location that is not an agent.
    def list_things_at(self, location):
        return [thing for thing in self.things if thing.location == location and not isinstance(thing, Agent)]

    #Removing the thing from the environment.
    def remove_thing(self, thing):
        self.things.remove(thing)

    #the status of the environment is unknown **

    def is_agent_alive(self, agent):
        return agent.alive

    def update_agent_alive(self, agent):
        if agent.performance <= 0:
            agent.alive = False
            print("Agent {} is dead.".format(agent))