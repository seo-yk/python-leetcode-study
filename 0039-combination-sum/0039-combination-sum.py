class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(start, curr):
            if curr == target:
                ans.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if curr < target:
                    curr += candidates[i]
                    path.append(candidates[i])
                    
                    dfs(i, curr)
                    path.pop()
                    curr -= candidates[i]
            
        dfs(0, 0)
        return ans