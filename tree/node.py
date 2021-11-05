from typing import Union, Set
from base.state import State


class Node:
    def __init__(self, state: State, parent: State = None, action: Union[str, int] = None, cost: int = 0):
        self.state = state
        self.parent = parent
        self.children : Set[Node] = set()
        self.action = action
        self.cost = cost

    
    def __lt__(self, other):
        return self.cost < other.cost

    
    def __str__(self) -> str:
        return str(self.state)


    def __repr__(self) -> str:
        return f"<{str(self.parent)} --{self.action}--> {str(self.state)}. cost: {self.cost}>"


    def path(self):
        node, path = self, []
        while node:
            path.append(node)
            node = node.parent
        return path[::-1]


    def add_child(self, child):
        self.children.add(child)
