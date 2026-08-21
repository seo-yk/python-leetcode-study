class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []

        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        r, c, i = 0, 0, 0

        for _ in range(m*n):
            ans.append(matrix[r][c])
            matrix[r][c] = '#'

            nr = r + dr[i]
            nc = c + dc[i]

            if not (0 <= nr < m and 0 <= nc < n and matrix[nr][nc] != '#'):
                i = (i+1) % 4
                nr = r+dr[i]
                nc = c+dc[i]

            r, c = nr, nc

        return ans