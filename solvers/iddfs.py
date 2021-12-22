from typing import Tuple, Optional
from base.solver import P, Solver
from solvers.utils import PriorityQueue, Queue
from solvers.utils import LIFO
from tree import Node, Tree, node


class IDDFS(Solver):
    def __init__(self, problem: P):
        self.problem = problem
        self.start = problem.initial
        self.root = Node(self.start)
        self.tree = Tree(self.root)


    def solve(self) -> Optional[Node]:
        # - if the root node is a goal, just return it
        #   tip. use 'is_goal' method from Problem
        if self.problem.is_goal(self.root.state):
            return self.root
        # - set depth to 1
        depth = 1
        while True:
        # - run self._depth_limited search
            node, left = self._depth_limited_search(self.root, depth)
        #   * if it returned a node, return it!
            if node is not None:
                return node
        #   * if there is no nodes left, return None
            if not left:
                return None
        #   * otherwise increment depth and repeat the limited search
            depth += 1
    

    def _depth_limited_search(self, root: Node, max_depth: int) -> Tuple[Optional[Node], bool]:
        frontier = Queue
        visited = {self.start}
        frontier.push((self.root, False))
        for i in range(1, max_depth):
            node, left = frontier.pop()
            if self.problem.is_goal(node.state):
                return (node, left)
            elif i == max_depth:
                return (node, True)
            else:
                for child in self.tree.expand(self.problem, node):
                    if child not in visited:
                        visited.add(child.state)
                        frontier.push((child, i == max_depth))
        # - do a DFS with depth limited by a given depth
        #   tip. base in on the Uninformed search you have already done by now
        # differences:
        # - you should store in the frontier a tuple (node, depth), so later you could easily access current depth
        # - if depth of child is bigger than the max_depth, do not expand this child and store info there are still nodes left
        # - this method return a tuple:
        #   * first element is the node if the method finds a goal state, otherwise it should be None
        #   * second element is a boolean telling whether there are any nodes left to be expanded
        return None


    def search_tree(self) -> Tree:
        return self.tree
        