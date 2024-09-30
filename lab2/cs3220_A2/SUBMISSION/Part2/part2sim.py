import random
from CatFriendlyHouse import CatFriendlyHouse
from environmentClass import Environment
from agents import agent_cat
from sausage import Sausage
from milk import Milk



def simulate_cat_in_house(num_steps):
    # Create the environment (CatFriendlyHouse)
    house = CatFriendlyHouse()
 
    # Create the agent (AgentCat) and add it to house
    cat = agent_cat()
    house.agents.append(cat)
    cat.location = house.default_location(cat)

    # Add sausages and milk to the house
    house.add_thing(Sausage(20))
    house.add_thing(Milk(10))


    # Run the simulation for 10 steps
    house.run(num_steps)

# Run the simulation for 10 steps
if __name__ == "__main__":
    simulate_cat_in_house(10)
