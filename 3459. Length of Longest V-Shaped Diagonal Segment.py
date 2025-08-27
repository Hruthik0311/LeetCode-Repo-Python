class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [(1,1), (-1,-1), (1,-1), (-1,1)]
        clockwise = {0:2, 2:1, 1:3, 3:0}
        from functools import lru_cache
        @lru_cache(None)
        def dfs(i, j, d, turned, expected):
            best = 1
            di, dj = dirs[d]
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == expected:
                nxt_expected = 0 if expected == 2 else 2
                best = max(best, 1 + dfs(ni, nj, d, turned, nxt_expected))
            if not turned:
                nd = clockwise[d]
                di, dj = dirs[nd]
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == expected:
                    nxt_expected = 0 if expected == 2 else 2
                    best = max(best, 1 + dfs(ni, nj, nd, True, nxt_expected))
            return best
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for d in range(4):
                        ans = max(ans, dfs(i, j, d, False, 2))
        return ans
