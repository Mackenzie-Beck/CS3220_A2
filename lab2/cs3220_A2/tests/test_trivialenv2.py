import unittest
from TrivialVacuumEnvironment2 import TrivialVacuumEnvironment2
from agentClass import Agent
from dirt import Dirt
from locations import loc_A, loc_B

class TestTrivialVacuumEnvironment2(unittest.TestCase):
    def setUp(self):
        self.env = TrivialVacuumEnvironment2()
        self.agent = Agent()
        self.dirt = Dirt()

    def test_initial_state(self):
        self.assertEqual(self.env.status, {loc_A: 'Clean', loc_B: 'Clean'})
        self.assertEqual(len(self.env.things), 0)

    def test_add_thing(self):
        self.env.add_thing(self.agent)
        self.assertEqual(len(self.env.things), 1)
        self.assertIn(self.agent, self.env.things)
        self.assertIn(self.agent.location, [loc_A, loc_B])

    def test_remove_thing(self):
        self.env.add_thing(self.agent)
        self.env.remove_thing(self.agent)
        self.assertEqual(len(self.env.things), 0)

    def test_percept_clean(self):
        self.env.add_thing(self.agent)
        percept = self.env.percept(self.agent)
        self.assertEqual(percept[1], 'Clean')

    def test_percept_dirty(self):
        self.env.add_thing(self.agent)
        self.env.add_thing(self.dirt)
        self.dirt.location = self.agent.location
        percept = self.env.percept(self.agent)
        self.assertEqual(percept[1], 'Dirty')

    def test_execute_action_move(self):
        self.env.add_thing(self.agent)
        initial_location = self.agent.location
        initial_performance = self.agent.performance
        
        if initial_location == loc_A:
            self.env.execute_action(self.agent, 'Right')
            self.assertEqual(self.agent.location, loc_B)
        else:
            self.env.execute_action(self.agent, 'Left')
            self.assertEqual(self.agent.location, loc_A)
        
        self.assertEqual(self.agent.performance, initial_performance - 1)

    def test_execute_action_suck(self):
        self.env.add_thing(self.agent)
        self.env.add_thing(self.dirt)
        self.dirt.location = self.agent.location
        initial_performance = self.agent.performance
        
        self.env.execute_action(self.agent, 'Suck')
        
        self.assertEqual(self.env.status[self.agent.location], 'Clean')
        self.assertEqual(self.agent.performance, initial_performance + 10)

    def test_is_agent_alive(self):
        self.env.add_thing(self.agent)
        self.assertTrue(self.env.is_agent_alive(self.agent))
        
        self.agent.performance = -1
        self.env.update_agent_alive(self.agent)
        self.assertFalse(self.env.is_agent_alive(self.agent))

if __name__ == '__main__':
    unittest.main()
