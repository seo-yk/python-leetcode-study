class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(s, open_count, close_count):
            if len(s) == (n*2):
                ans.append(s)
                return

            if open_count < n:
                dfs(s+'(', open_count+1, close_count)
            if close_count < open_count:
                dfs(s+')', open_count, close_count+1)

        dfs("", 0, 0)
        return ans