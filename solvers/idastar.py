from typing import Tuple, Optional
from base.solver import H, P, HeuristicSolver
from solvers.utils import LIFO, PriorityQueue
from tree import Node, Tree


class IDAStar(HeuristicSolver):
    def __init__(self, problem: P, heuristic: H):
        super().__init__(problem, heuristic)
        self.start = problem.initial
        self.root = Node(self.start, cost=0)
        self.tree = Tree(self.root)

    
    def solve(self) -> Optional[Node]:
        # - if the root node is a goal, just return it
        #   tip. use 'is_goal' method from Problem
        if self.problem.is_goal(self.root.state):
            return self.root
        # - set bound to the heuristic of the start state
        bound = self.heuristic(self.start)
        # - run self._cost_limited search
        while True:
            node, cost = self._cost_limited_search(self.root, bound)
        #   * if it returned a node, return it!
            if node:
                return node
        #   * if returned cost equals bound, return None
            if cost == bound:
                return None
        #   * otherwise update bound to cost and repeat the limited search
            bound = cost

    
    def _cost_limited_search(self, root: Node, bound: float) -> Tuple[Optional[Node], float]:
        frontier = PriorityQueue(lambda node: node.cost + self.heuristic(node.state))
        visited = {self.start}

        frontier.push(root)
        while frontier:
            node = frontier.pop()
            if self.problem.is_goal(node.state):
                return node, node.cost
            if node.cost > bound:
                return None, node.cost
            for child in self.tree.expand(self.problem, node):
                if child not in self.visited:
                    visited.add(child.state)
                    frontier.push(child)
        # - do a DFS with depth limited by a given bound
        #   tip. base in on the BestFirstSearch you have already done by now
        # differences:
        # - sort children using A* fcost (cost + heuristic)
        # - if fcost of child is bigger than the bound, do not expand this child
        # - this method return a tuple:
        #   * first element is the node if the method finds a goal state, otherwise it should be None
        #   * second element is a new bound (the smallest fcost of a not expanded child)
                
    def search_tree(self) -> Tree:
        return self.tree
