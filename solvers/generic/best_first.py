from typing import Callable, Optional
from base.problem import Problem
from solvers.utils import PriorityQueue, Queue
from tree import Node, Tree


class BestFirstSearch():
    def __init__(self, problem: Problem, eval_fun: Callable[[Node], float]):
        self.problem = problem
        self.eval_fun = eval_fun
        self.start = problem.initial
        self.root = Node(self.start)
        self.frontier:PriorityQueue = PriorityQueue(eval_fun)
        self.visited = {self.start: self.root.cost}
        self.tree = Tree(self.root)
    

    def solve(self) -> Optional[Node]:
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
        #       - if child has not been visited (check self.visited dictionary)
        #         or its cost is better than the saved one
                    if child.state not in self.visited or self.visited[child.state] > child.cost + self.visited[node.state]:
        #         * update cost in visited
                        self.visited[child.state] = child.cost
        #         * push child onto frontier
                        self.frontier.push(child)
        # - return None if nothing happens
        return None
