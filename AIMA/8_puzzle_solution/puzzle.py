import random
from misc import *

class Puzzle:
    def __init__(self, order=3):
        '''
        :param order: INT, 表示几阶方阵
        :attributes:
            puzzle:
            zero: 存储0点坐标
            directions: 方向
        '''
        self.order = order
        self.puzzle = []
        self.zero = (0, 0)
        self.directions = ['U', 'D', 'L', 'R']
        count = 1
        # 初始化
        for i in range(order):
            self.puzzle.append([])
            for j in range(order):
                self.puzzle[i].append(count)
                count += 1
        self.puzzle[order-1][order-1] = 0
        self.zero = (order - 1, order -1)

    def setPuzzle(self, state):
        for i in range(self.order):
            for j in range(self.order):
                self.puzzle[i][j] = state[i][j]
                if state[i][j] == 0:
                    self.zero = (i, j)

    def move(self, direction):
        if direction == 'U':
            self.up()
        if direction == 'D':
            self.down()
        if direction == 'L':
            self.left()
        if direction == 'R':
            self.right()

    def shuffle(self, numAct):
        for i in range(numAct):
            self.move(self.directions[random.randint(0, 3)])

    # 按指令移动
    def route(self, string):
        for m in string:
            self.move(m)

    # 问题是否可解
    def check(self):
        return isSolvable(self.puzzle)

    # GOAL 状态检测
    def isGoal(self):
        count = 1
        all = self.order ** 2
        for i in range(self.order):
            for j in range(self.order):
                if self.puzzle[i][j] != count % all:
                    return False
                count += 1
        return True

    # 移动数据交换、更新0的位置
    def up(self):
        if self.canUp():
            tmp = (self.zero[0] - 1, self.zero[1])
            self.swap(self.zero, tmp)
            self.zero = tmp

    def down(self):
        if self.canDown():
            tmp =  (self.zero[0] + 1, self.zero[1])
            self.swap(self.zero, tmp)
            self.zero = tmp

    def left(self):
        if self.canLeft():
            tmp = (self.zero[0], self.zero[1] - 1)
            self.swap(self.zero, tmp)
            self.zero = tmp

    def right(self):
        if self.canRight():
            tmp = (self.zero[0], self.zero[1] + 1)
            self.swap(self.zero, tmp)
            self.zero = tmp

    def swap(self, p1, p2):
        tmp = self.puzzle[p1[0]][p1[1]]
        self.puzzle[p1[0]][p1[1]] = self.puzzle[p2[0]][p2[1]]
        self.puzzle[p2[0]][p2[1]] = tmp

    # 移动边界判断
    def canUp(self):
        return self.zero[0] > 0

    def canDown(self):
        return self.zero[0] < self.order - 1

    def canLeft(self):
        return self.zero[1] > 0

    def canRight(self):
        return self.zero[1] < self.order - 1

    def toString(self):
        for i in range(self.order):
            print(' '.join(map(str,self.puzzle[i])))
