class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        answer = []
        visited = [False for _ in range(len(nums))]

        def helper(path):
            if len(path) == len(nums):
                answer.append(path[:])
                return

            for i in range(len(nums)):
                if visited[i] == False:
                    visited[i] = True
                    path.append(nums[i])
                    helper(path)
                    path.pop()
                    visited[i] = False

        helper([])
        return answer