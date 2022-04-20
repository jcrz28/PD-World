from PDWorld.Matrix.location import Location
from PDWorld.Agent.operator import Operator


class Agent:
    Operator = Operator()
    Location = Location()

    def __init__(self, agent, femalePos, malePos, hasCapacity, reward):
        # Differentiate Male and Female Agent
        self.agent = agent

        # Initial position of female agent
        self.i, self.j = femalePos[0], femalePos[1]

        # Initial position of male agent
        self.i_Prime, self.j_Prime = malePos[0], malePos[1]

        # Initial values of male and female agents block capacity
        self.x, self.x_Prime = hasCapacity[0], hasCapacity[1]

        self.reward = reward

    def gainReward(self):
        self.reward += 13

    def loseReward(self):
        self.reward -= 1

    def updateMatrixAndReward(self, grid, row, col, block, increment):
        self.gainReward()
        grid[row][col][block] += increment

    def agentReward(self, grid, row, col, block):
        if self.Location.checkDropOffLocations(grid, row, col, block, self.getAgent()):
            self.updateMatrixAndReward(grid, row, col, block, 1)
            self.agentFree()
            return True

        if self.Location.checkPickUpLocation(grid, row, col, block, self.getAgent()):
            self.updateMatrixAndReward(grid, row, col, block, -1)
            self.agentNotFree()
            return True

        return False

    def getAgent(self):
        if self.agent:
            return self.x
        return self.x_Prime

    def agentMovesInYAxis(self, grid, row, col, occupied, increment):
        grid[row - increment][col][occupied] = False
        grid[row][col][occupied] = True

        if self.agent:
            self.i += increment
        else:
            self.i_Prime += increment

    def agentMovesInXAxis(self, grid, row, col, occupied, increment):
        grid[row][col - increment][occupied] = False
        grid[row][col][occupied] = True

        if self.agent:
            self.j += increment
        else:
            self.j_Prime += increment

    def getCurrentAgentPosition(self):
        if self.agent:
            return self.i, self.j
        return self.i_Prime, self.j_Prime

    def agentFree(self):
        if self.agent:
            self.x = 0
        else:
            self.x_Prime = 0

    def agentNotFree(self):
        if self.agent:
            self.x = 1
        else:
            self.x_Prime = 1

    def changeAgent(self):
        if self.agent:
            self.agent = False
        else:
            self.agent = True
