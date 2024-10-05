from problemClass import Problem

class FarmerProblem(Problem):
    def __init__(self):
        initial_state = ('L', 'L', 'L', 'L') # (farmer, goat, cabbage, wolf)
        goal_state = ('R', 'R', 'R', 'R')
        super().__init__(initial_state, goal_state)
        self.goal_state = goal_state

    def actions(self, state):
        possible_actions = [] 
        farmer_side = state[0] 
        opposite_side = 'R' if farmer_side == 'L' else 'L' # if farmer is on the left, the opposite side is the right, and vice versa

        # Farmer can always move alone
        possible_actions.append(('farmer_alone', opposite_side))

        # Check which items are on the same side as the farmer
        for i, item in enumerate(['goat', 'cabbage', 'wolf']): # enumerate gets both index and value from loop
            if state[i+1] == farmer_side:
                possible_actions.append((f'farmer_{item}', opposite_side))

        # Filter out invalid actions (wolf eats goat, goat eats cabbage)
        return [action for action in possible_actions if self.is_valid_action(state, action)]

    def is_valid_action(self, state, action):
        #check if given state is valid
        if state[1] == state[2] != state[0]: # goat and cabbage on the same side
            return False
        if state[1] == state[3] != state[0]: # wolf and goat on the same side
            return False
        

        # Implement the validation of an action in a state
        new_state = self.result(state, action)
        return not(
            (new_state[1] == new_state[2] != new_state[0]) or # goat and cabbage on the same side
            (new_state[1] == new_state[3] != new_state[0]) # wolf and goat on the same side
        )

    def result(self, state, action):
        item, destination = action
        new_state = list(state)
        new_state[0] = destination  # Move farmer

        if item != 'farmer_alone':
            # split the item name and get the index of the item + 1 (to get the index of the item in the state tuple)
            item_index = ['goat', 'cabbage', 'wolf'].index(item.split('_')[1]) + 1 
            new_state[item_index] = destination

        return tuple(new_state)

    def goal_test(self, state):
        # Implement the goal test for the state
        return state == self.goal_state

    def path_cost(self, cost, state1, action, state2):
        # Implement the path cost function
        if action[0] == 'farmer_alone':
            return cost + 1
        else:
            return cost + 3 # farmer with item has to load, move, unload

