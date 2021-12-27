from problems.n_puzzle import NPuzzleState
from problems.n_puzzle.heuristics.n_puzzle_abstract_heuristic import NPuzzleAbstractHeuristic



class NPuzzleTilesOutOfPlaceHeuristic(NPuzzleAbstractHeuristic):

    def __call__(self, state: NPuzzleState) -> float:
        # Calculate how many tiles are not on their expected positions
        # tip 1.'state' is the current state, 
        # tip 2. you can use self.positions function to get from it a dictionary:
        #   { tile_number : (x_coordinate, y_coordinate) }
        # tip 3. self.goal_coords contains such a dictionary for the goal state
        positions = self.positions(state)
        sum = 0
        for tile in positions:
            pos_x, pos_y = positions[tile]
            goal_x, goal_y = self.goal_coords[tile]
            if pos_x != goal_x or pos_y != goal_y:
                sum += 1
        return sum
