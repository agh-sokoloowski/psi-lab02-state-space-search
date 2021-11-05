from typing import Optional
from base.solver import P, HeuristicSolver
from solvers.utils import PriorityQueue, Queue
from tree import Node, Tree


class UninformedSearch():
    def __init__(self, problem: P, queue: Queue):
        self.problem = problem
        self.start = problem.initial
        self.frontier = queue
        self.visited = {self.start}
        self.root = Node(self.start)
        self.tree = Tree(self.root)


    def solve(self):
        # TODO:
        # - push root node to the frontier
        # - pop nodes from the frontier as long as there any
        #   - if popped node is a goal, return it
        #     tip. use 'is_goal' method from Problem
        #   - otherwise go through all its children (expand method of Tree)
        #       - if child has not been visited (check self.visited set)
        #         * add child to visited
        #         * push child onto frontier
        # - return None if nothing happens
        raise NotImplementedError()
