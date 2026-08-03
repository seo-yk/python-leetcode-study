class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(r, c, index):

            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[index]:
                return False

            if index == len(word)-1:
                return True

            temp = board[r][c]
            board[r][c] = '#'
            found = (
                dfs(r-1, c, index+1) or
                dfs(r+1, c, index+1) or
                dfs(r, c-1, index+1) or
                dfs(r, c+1, index+1)
            )
            board[r][c] = temp
            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False