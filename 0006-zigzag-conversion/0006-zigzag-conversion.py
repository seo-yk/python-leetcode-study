class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        ans = [[] for _ in range(numRows)]

        currentRow = 0
        direction = -1

        for c in s:
            ans[currentRow].append(c)

            if currentRow == 0 or currentRow == numRows-1:
                direction *= -1

            currentRow += direction

        return "".join("".join(row) for row in ans)