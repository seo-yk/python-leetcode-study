class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        ans = []
        path = ""

        dd = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        def backtrack(depth, path):
            if depth == len(digits):
                ans.append(path)
                return

            for char in dd[digits[depth]]:
                backtrack(depth+1, path + char)

        backtrack(0, "")
        return ans   