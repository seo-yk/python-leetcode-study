class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # time complexity: 최대 O(N)
        
        # 기준 1개 -> 하나씩 더해보기 -> index는 뒤로만 -> 찾으면 배열 추가 -> return
        result = []

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result

        