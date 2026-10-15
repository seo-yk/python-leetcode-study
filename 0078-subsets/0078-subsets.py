class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        answer = []

        def backtrack(start, path):
            answer.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
            
            return
        
        backtrack(0, [])
        return answer
