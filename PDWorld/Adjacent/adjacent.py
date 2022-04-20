from PDWorld.Agent.agent import Agent
from PDWorld.Agent.operator import Operator


class Adjacent(Agent):
    def __init__(self, start):
        super().__init__(start[0], start[1], start[2], start[3], start[4])

    def adjacentToSouth(self, matrix, row, col, block, occupied):
        return Operator.south(matrix, row, col, occupied) and self.agentReward(matrix, row + 1, col,
                                                                               block)

    def adjacentToNorth(self, matrix, row, col, block, occupied):
        return Operator.north(matrix, row, col, occupied) and self.agentReward(matrix, row - 1, col,
                                                                               block)

    def adjacentToEast(self, matrix, row, col, block, occupied):
        return Operator.east(matrix, row, col, occupied) and self.agentReward(matrix, row, col + 1,
                                                                              block)

    def adjacentToWest(self, matrix, row, col, block, occupied):
        return Operator.west(matrix, row, col, occupied) and self.agentReward(matrix, row, col - 1,
                                                                              block)

    def adjacentDropOff(self, matrix, row, col, block, occupied):
        # DropOff Location: 0, 0
        if row == 0 and col - 1 == 0 and self.adjacentToWest(matrix, row, col, block, occupied):
            self.agentMovesInXAxis(matrix, row, col - 1, occupied, -1)
            return True

        if row - 1 == 0 and col == 0 and self.adjacentToNorth(matrix, row, col, block, occupied):
            self.agentMovesInYAxis(matrix, row - 1, col, occupied, -1)
            return True

        # DropOff Location: 0, 4
        if row == 0 and col + 1 == 4 and self.adjacentToEast(matrix, row, col, block, occupied):
            self.agentMovesInXAxis(matrix, row, col + 1, occupied, 1)
            return True

        if row - 1 == 0 and col == 4 and self.adjacentToNorth(matrix, row, col, block, occupied):
            self.agentMovesInYAxis(matrix, row - 1, col, occupied, -1)
            return True

        # DropOff Location: 4, 4
        if row == 4 and col + 1 == 4 and self.adjacentToEast(matrix, row, col, block, occupied):
            self.agentMovesInXAxis(matrix, row, col + 1, occupied, 1)
            return True

        if row + 1 == 4 and col == 4 and self.adjacentToSouth(matrix, row, col, block, occupied):
            self.agentMovesInYAxis(matrix, row + 1, col, occupied, 1)
            return True

        # DropOff Location: 2, 2
        if row + 1 == 2 and col == 2 and self.adjacentToSouth(matrix, row, col, block, occupied):
            self.agentMovesInYAxis(matrix, row + 1, col, occupied, 1)
            return True

        if row - 1 == 2 and col == 2 and self.adjacentToNorth(matrix, row, col, block, occupied):
            self.agentMovesInYAxis(matrix, row - 1, col, occupied, -1)
            return True

        if row == 2 and col + 1 == 2 and self.adjacentToEast(matrix, row, col, block, occupied):
            self.agentMovesInXAxis(matrix, row, col + 1, occupied, 1)
            return True

        if row == 2 and col - 1 == 2 and self.adjacentToWest(matrix, row, col, block, occupied):
            self.agentMovesInXAxis(matrix, row, col - 1, occupied, -1)
            return True

        return False

    def adjacentPickUp(self, matrix, row, col, block, occupied):
        # PickUp Location: 2, 4
        if row + 1 == 2 and col == 4 and self.adjacentToSouth(matrix, row, col, block, occupied):
            self.agentMovesInYAxis(matrix, row + 1, col, occupied, 1)
            return True

        if row - 1 == 2 and col == 4 and self.adjacentToNorth(matrix, row, col, block, occupied):
            self.agentMovesInYAxis(matrix, row - 1, col, occupied, -1)
            return True

        # PickUp Location: 3, 1
        if row - 1 == 3 and col == 1 and self.adjacentToNorth(matrix, row, col, block, occupied):
            self.agentMovesInYAxis(matrix, row - 1, col, occupied, -1)
            return True

        if row == 3 and col + 1 == 1 and self.adjacentToEast(matrix, row, col, block, occupied):
            self.agentMovesInXAxis(matrix, row, col + 1, occupied, 1)
            return True

        if row + 1 == 3 and col == 1 and self.adjacentToSouth(matrix, row, col, block, occupied):
            self.agentMovesInYAxis(matrix, row + 1, col, occupied, 1)
            return True

        if row == 3 and col - 1 == 1 and self.adjacentToWest(matrix, row, col, block, occupied):
            self.agentMovesInXAxis(matrix, row, col - 1, occupied, -1)
            return True

        return False

    def checkAdjacent(self, matrix, row, col, block, occupied):
        if self.adjacentPickUp(matrix, row, col, block, occupied):
            return True
        if self.adjacentDropOff(matrix, row, col, block, occupied):
            return True
        return False
