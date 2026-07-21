class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        visited = [False] * len(nums)

        def dfs(start):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    path.append(nums[i])

                    dfs(start + 1)
                    path.pop()
                    visited[i] = False

        dfs(0)
        return ans