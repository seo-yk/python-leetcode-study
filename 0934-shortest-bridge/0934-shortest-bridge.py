class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        queue = deque()

        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] != 1:
                return

            grid[r][c] = 2
            queue.append((r, c, 0))

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        found = False
        for r in range(R):
            for c in range(C):
                if found:
                    break
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if 0 <= nr < R and 0 <= nc < C:
                    if grid[nr][nc] == 1:
                        return dist

                    if grid[nr][nc] == 0:
                        grid[nr][nc] = -1
                        queue.append((nr, nc, dist+1))

        return 0