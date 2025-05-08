class Solution:
    def deleteGreatestValue(self, grid):
        for row in grid:
            row.sort()
        total = 0
        for col in zip(*grid):
            total += max(col)
        return total
