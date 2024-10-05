import unittest
from farmer_problem import FarmerProblem

class TestFarmerProblem(unittest.TestCase):
    def setUp(self):
        self.problem = FarmerProblem()

    def test_initial_state(self):
        self.assertEqual(self.problem.initial, ('L', 'L', 'L', 'L'))

    def test_goal_state(self):
        self.assertEqual(self.problem.goal, ('R', 'R', 'R', 'R'))

    def test_actions(self):
        initial_state = ('L', 'L', 'L', 'L')
        actions = self.problem.actions(initial_state)
        self.assertIn(('farmer_goat', 'R'), actions)
        self.assertNotIn(('farmer_wolf', 'R'), actions)
        self.assertNotIn(('farmer_cabbage', 'R'), actions)

    def test_result(self):
        initial_state = ('L', 'L', 'L', 'L')
        action = ('farmer_goat', 'R')
        result = self.problem.result(initial_state, action)
        self.assertEqual(result, ('R', 'R', 'L', 'L'))

    def test_is_valid_action(self):
        valid_state = ('L', 'L', 'L', 'L')
        valid_action = ('farmer_goat', 'R')
        self.assertTrue(self.problem.is_valid_action(valid_state, valid_action))

        invalid_state = ('R', 'L', 'L', 'L')
        invalid_action = ('farmer_alone', 'L')
        self.assertFalse(self.problem.is_valid_action(invalid_state, invalid_action))

    def test_goal_test(self):
        self.assertTrue(self.problem.goal_test(('R', 'R', 'R', 'R')))
        self.assertFalse(self.problem.goal_test(('L', 'R', 'R', 'R')))

    def test_path_cost(self):
        state1 = ('L', 'L', 'L', 'L')
        state2 = ('R', 'L', 'L', 'L')
        action = ('farmer_alone', 'R')
        self.assertEqual(self.problem.path_cost(0, state1, action, state2), 1)

        state1 = ('L', 'L', 'L', 'L')
        state2 = ('R', 'R', 'L', 'L')
        action = ('farmer_goat', 'R')
        self.assertEqual(self.problem.path_cost(0, state1, action, state2), 3)

if __name__ == '__main__':
    unittest.main()
