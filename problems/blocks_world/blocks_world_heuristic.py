


from typing import Dict, List
from base.heuristic import Heuristic
from problems.blocks_world.blocks_world_problem import BlocksWorldProblem, BlocksWorldState

class BlocksWorldNaiveHeuristic(Heuristic):

    def __init__(self, problem: BlocksWorldProblem) -> None:
        super().__init__(problem)
        self.expected_columns = self._calculate_expected_columns(problem.goal)
        self.expected_fundaments = self._calculate_expected_fundaments(problem.goal)

    def _calculate_expected_columns(self, goal: BlocksWorldState) -> Dict[str, int]:
        # return a dict of form:
        # { <block name> : <index of column in the goal state> }
        expected_columns = {}
        for i, col in enumerate(goal.columns):
            for block in col:
                expected_columns[block] = i
        return expected_columns

    def _calculate_expected_fundaments(self, goal: BlocksWorldState) -> Dict[str, List[str]]:
        # return a dict of form:
        # { <block name> : <list of the blocks below it in the goal state> }
        excepted_fundaments = {}
        for i, col in enumerate(goal.columns):
            for b, block in enumerate(col):
                excepted_fundaments[block] = []
                for j in range(b):
                    excepted_fundaments[block].append(col[j])
        return excepted_fundaments

    def __call__(self, state: BlocksWorldState) -> int:
        # - calculate how many blocks are in the incorrect columns
        # - calculate how many blocks have incorrect block below
        # - return number of incorrect columns plus twice the number of incorrect blocks below
        # tip. use self.expected_columns and self.expected_fundaments
        incorrect_columns = 0
        incorrect_fundaments = 0
        for i, col in enumerate(state.columns):
            if col != self.expected_columns[i]:
                incorrect_columns += 1

        for i, col in enumerate(state.columns):
            for block in col:
                if block in self.expected_fundaments[block]:
                    if self.expected_fundaments[block][self.expected_fundaments[block].index(block)] != col[col.index(block)]:
                        incorrect_fundaments += 1
                        
        return incorrect_columns + (2 * incorrect_fundaments)
