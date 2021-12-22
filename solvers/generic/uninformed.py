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
        # - push root node to the frontier
        self.frontier.push(self.root)
        # - pop nodes from the frontier as long as there any
        while self.frontier:
            node = self.frontier.pop()
        #   - if popped node is a goal, return it
        #     tip. use 'is_goal' method from Problem
            if self.problem.is_goal(node.state):
                return node
        #   - otherwise go through all its children (expand method of Tree)
            else:
                for child in self.tree.expand(self.problem, node):
        #       - if child has not been visited (check self.visited set)
                    if child not in self.visited:
        #         * add child to visited
                        self.visited.add(child.state)
        #         * push child onto frontier
                        self.frontier.push(child)
        # - return None if nothing happens
        return None
