from queue import Queue
from copy import deepcopy

'''
Node类，为了方便对puzzle进行堆栈、队列操作，记录移动路径。

IDS算法需要维护深度信息；A*算法需要计算初始状态到当前状态的距离，可以用深度来表示。
'''

class Node:
    def __init__(self, puzzle, parent=None, actions=''):
        self.state = puzzle
        self.parent = parent
        self.depth = 0
        if parent is None:
            self.depth = 0
            self.actions = actions
        else:
            self.depth = parent.depth + 1
            self.actions = parent.actions + actions

    def isGoal(self):
        return self.state.isGoal()

    def neighbors(self):
        neighbors = []
        for direction in self.state.directions:
            tmp = deepcopy(self.state)
            tmp.move(direction)
            if tmp.zero is not self.state.zero:
                neighbors.append(Node(tmp, self, direction))
        return neighbors

    def cost(self, heuristic_mode):
        return self.placeWrong() if heuristic_mode == 0 else self.distance_manhattan()

    def placeWrong(self):
        errors = 0
        count = 1
        all = self.state.order ** 2
        for i in range(self.state.order):
            for j in range(self.state.order):
                if self.state.puzzle[i][j] != count % all:
                    errors += 1
                count += 1
        return errors

    def distance_manhattan(self):
        res = 0
        for i in range(self.state.order):
            for j in range(self.state.order):
                index = self.state.puzzle[i][j] - 1
                dis = 0 if index == -1 else abs(i - int(index/self.state.order)) + abs(j - int(index % self.state.order))
                res += dis
        return res

    def __str__(self):
        return str(self.actions)

    def __lt__(self, other):
        return True




