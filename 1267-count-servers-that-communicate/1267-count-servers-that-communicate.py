class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        if not grid:
            return 0

        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] != 1:
                return 0

            grid[r][c] = 2
            cnt = 1

            for i in range(C):
                if grid[r][i] == 1:
                    cnt += dfs(r, i)

            for i in range(R):
                if grid[i][c] == 1:
                    cnt += dfs(i, c)

            return cnt

        total = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    connected = dfs(r, c)
                    if connected > 1:
                        total += connected

        return total