from part3EnvClass import part3Env
from agents import *  # Assuming you have a DeliveryAgent class


def test_environment():
    # Create the environment
    env = part3Env()

    # Create the agent
    agent = ReflexAgentP3()

    # Add the agent to the environment
    env.add_thing(agent)

    # Add other things to the environment (students, IT staff, office managers)
    # env.add_thing(Student(), location)
    # env.add_thing(ITStaff(), location)
    # env.add_thing(OfficeManager(), location)

    # Add 10 things to the environment in random locations
    from agents import Student, ITStaff, OfficeManager
    import random

    things_to_add = [
        Student(), Student(), Student(),
        ITStaff(), ITStaff(),
        OfficeManager(), OfficeManager(),
        Student(), ITStaff(), OfficeManager()
    ]

    for thing in things_to_add:
        location = env.default_location(thing)
        env.add_thing(thing, location)
        print(f"Added {type(thing).__name__} at location: {location}")










    # Run the environment for a certain number of steps
    for _ in range(100):  # Run for 100 steps
        env.step()
        if not agent.alive:
            break

    # Print final performance
    print(f"Agent's final performance: {agent.performance}")

if __name__ == "__main__":
    test_environment()