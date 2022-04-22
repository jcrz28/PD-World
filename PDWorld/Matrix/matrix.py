import random
from copy import deepcopy

from PDWorld.Adjacent.adjacent import Adjacent
from PDWorld.Agent.operator import Operator
from PDWorld.Matrix.location import Location


class Matrix:
    Operator = Operator()
    Location = Location()

    def __init__(self, start, terminalStates):
        self.Agent = Adjacent(start)
        self.matrix, self.cell, self.terminalStates = [], {'block': 0, 'occupied': False}, terminalStates

    def getBlockKey(self):
        return list(self.cell.keys())[0]

    def getOccupiedKey(self):
        return list(self.cell.keys())[1]

    # No operators are valid going to a pickup or drop off locations.
    # Therefore, the agents will lose reward.
    def checkValidMoves(self, row, col, randomNumber, occupied):
        if randomNumber == 0 and Operator.north(self.matrix, row, col, occupied):
            self.Agent.agentMovesInYAxis(self.matrix, row - 1, col, occupied, -1)
            self.Agent.loseReward()
            return True

        if randomNumber == 1 and Operator.south(self.matrix, row, col, occupied):
            self.Agent.agentMovesInYAxis(self.matrix, row + 1, col, occupied, 1)
            self.Agent.loseReward()
            return True

        if randomNumber == 2 and Operator.east(self.matrix, row, col, occupied):
            self.Agent.agentMovesInXAxis(self.matrix, row, col + 1, occupied, 1)
            self.Agent.loseReward()
            return True

        if randomNumber == 3 and Operator.west(self.matrix, row, col, occupied):
            self.Agent.agentMovesInXAxis(self.matrix, row, col - 1, occupied, -1)
            self.Agent.loseReward()
            return True

        return False

    def moveAgent(self, block, occupied):
        row, col = self.Agent.getCurrentAgentPosition()
        move = False
        if Operator.checkAgents(self.Agent.i, self.Agent.j, self.Agent.i_Prime, self.Agent.j_Prime) and \
                self.Agent.checkAdjacent(self.matrix, row, col, block, occupied):
            return

        while not move:
            randomNumber = random.randint(0, 3)
            move = self.checkValidMoves(row, col, randomNumber, occupied)
        return

    def initializeMatrix(self, block, occupied):
        # Set Matrix Cells
        for row in range(5):
            row = []
            for col in range(5):
                row.append(deepcopy(self.cell))
            self.matrix.append(row)

        # Set PickUp Cells
        self.matrix[2][4][block] = 10
        self.matrix[3][1][block] = 10

        # Set DropOff Cells
        self.matrix[0][0][block] = 0
        self.matrix[0][4][block] = 0
        self.matrix[2][2][block] = 0
        self.matrix[4][4][block] = 0

        # Set Agents Starting Locations
        self.matrix[0][2][occupied] = True
        self.matrix[4][2][occupied] = True

    def printMatrix(self):
        for i in range(5):
            for j in range(5):
                print(i, j, ": ", self.matrix[i][j])
            print()

        print(f"Terminal states reached: {self.terminalStates}")
        print(self.Agent.reward)

    def start(self):
        random.seed(1)
        terminalStates, block, occupied = 0, self.getBlockKey(), self.getOccupiedKey()
        self.initializeMatrix(block, occupied)

        for i in range(8000):
            if Location.dropOffLocationsFull(self.matrix, block):
                self.terminalStates += 1
                self.__init__((True, (0, 2), (4, 2), (0, 0), self.Agent.reward), self.terminalStates)
                self.initializeMatrix(block, occupied)
            self.moveAgent(block, occupied)
            self.Agent.changeAgent()

        self.printMatrix()
