# Checks if positions are within the grid, moves are valid, and cells are occupied
class Operator:
    @staticmethod
    def north(grid, row, col, occupied):
        if row - 1 > -1 and not grid[row - 1][col][occupied]:
            return True
        return False

    @staticmethod
    def south(grid, row, col, occupied):
        if row + 1 < 5 and not grid[row + 1][col][occupied]:
            return True
        return False

    @staticmethod
    def east(grid, row, col, occupied):
        if col + 1 < 5 and not grid[row][col + 1][occupied]:
            return True
        return False

    @staticmethod
    def west(grid, row, col, occupied):
        if col - 1 > -1 and not grid[row][col - 1][occupied]:
            return True
        return False

    @staticmethod
    def checkAgents(i, j, i_Prime, j_Prime):
        if i == i_Prime and j == j_Prime:
            return False
        return True
