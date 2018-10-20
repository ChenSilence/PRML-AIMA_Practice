from queue import LifoQueue
from queue import PriorityQueue
import node

class Solution:

    def __init__(self, puzzle):
        self.start = node.Node(puzzle)

    def IDS(self):
        depth = 0
        result = None
        while result == None:
            result = self.depthLimited(depth)
            depth += 1
        return result

    def depthLimited(self, depth):
        stack = LifoQueue()
        stack.put(self.start)
        while True:
            if stack.empty():
                return None
            top = stack.get()
            if top.isGoal():
                return top
            elif top.depth is not depth:
                for neighbor in top.neighbors():
                    stack.put(neighbor)

    def greedy(self, heuristic_mode):
        cur_node = self.start
        nodes = PriorityQueue()
        nodes.put((cur_node.cost(heuristic_mode), cur_node))
        visited = []
        while True:
            if nodes.empty():
                return None
            cur_node = nodes.get()[1]
            if cur_node.isGoal():
                return cur_node
            elif cur_node.state.puzzle not in visited:
                visited.append(cur_node.state.puzzle)
                for neighbor in cur_node.neighbors():
                    nodes.put((neighbor.cost(heuristic_mode), neighbor))

    def aStar(self, heuristic_mode):
        cur_node = self.start
        nodes = PriorityQueue()
        nodes.put((cur_node.cost(heuristic_mode), cur_node))
        visited = []
        while True:
            if nodes.empty():
                return None
            cur_node = nodes.get()[1]
            if cur_node.isGoal():
                return cur_node
            elif cur_node.state.puzzle not in visited:
                visited.append(cur_node.state.puzzle)
                for neighbor in cur_node.neighbors():
                    nodes.put((neighbor.cost(heuristic_mode) + neighbor.depth, neighbor))




