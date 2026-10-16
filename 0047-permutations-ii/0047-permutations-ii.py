class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        answer = []

        nums = sorted(nums)

        visited = [False for _ in range(len(nums))]
        
        def helper(path):
            if len(path) == len(nums):
                answer.append(path[:])
                return

            for i in range(len(nums)):
                if visited[i] == False :
                    if i>0 and nums[i-1] == nums[i] and visited[i-1] == False:
                        continue
                    else:
                        visited[i] = True
                        path.append(nums[i])
                        helper(path)
                        path.pop()
                        visited[i] = False

        helper([])
        return answer