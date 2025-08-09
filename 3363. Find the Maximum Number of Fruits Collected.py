class Solution:
    def maxCollectedFruits(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = 0
        for i in range(n):
            res += grid[i][i]
        for pass_ in range(2):
            if pass_ == 1:
                for i in range(n):
                    for j in range(i + 1, n):
                        grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
            prev = [-1] * n
            prev[n - 1] = grid[0][n - 1]
            for row in range(1, n - 1):
                curr = [-1] * n
                for col in range(n):
                    if prev[col] < 0:
                        continue
                    if col > 0:
                        curr[col - 1] = max(curr[col - 1], prev[col] + grid[row][col - 1])
                    if col < n - 1:
                        curr[col + 1] = max(curr[col + 1], prev[col] + grid[row][col + 1])
                    curr[col] = max(curr[col], prev[col] + grid[row][col])
                prev = curr
            res += prev[n - 1]
        return res
