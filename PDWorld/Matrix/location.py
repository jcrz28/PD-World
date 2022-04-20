class Location:
    @staticmethod
    def pickUpLocations(row, col):
        return (row == 2 and col == 4) or (row == 3 and col == 1)

    def pickUpIsValid(self, grid, row, col, block):
        return self.pickUpLocations(row, col) and grid[row][col][block] > 0

    def checkPickUpLocation(self, grid, row, col, block, capacity):
        return self.pickUpIsValid(grid, row, col, block) and capacity == 0

    # Drop off Functions
    @staticmethod
    def dropOffLocationsFull(grid, block):
        return grid[0][0][block] == 5 and grid[0][4][block] == 5 and grid[2][2][block] == 5 and grid[4][4][block] == 5

    @staticmethod
    def dropOffLocations(row, col):
        return (row == 0 and col == 0) or (row == 0 and col == 4) or (row == 2 and col == 2) or (row == 4 and col == 4)

    # Each drop off cell has 5 blocks capacity
    def dropOffIsValid(self, grid, row, col, block):
        return self.dropOffLocations(row, col) and grid[row][col][block] < 5

    def checkDropOffLocations(self, grid, row, col, block, capacity):
        return self.dropOffIsValid(grid, row, col, block) and capacity == 1
