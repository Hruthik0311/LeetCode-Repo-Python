class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diag_map = {}
        for i in range(n):
            for j in range(n):
                key = i - j
                if key not in diag_map:
                    diag_map[key] = []
                diag_map[key].append(grid[i][j])
        for key, arr in diag_map.items():
            if key >= 0:
                arr.sort(reverse=True)
            else: 
                arr.sort() 
            diag_map[key] = arr
        for i in range(n):
            for j in range(n):
                key = i - j
                grid[i][j] = diag_map[key].pop(0)
        return grid
