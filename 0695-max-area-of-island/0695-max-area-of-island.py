class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if 0 > i or i >= len(grid) or 0 > j or j >= len(grid[0]) or grid[i][j] != 1:
                return 0

            grid[i][j] = 2

            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)

        if not grid:
            return 0

        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area