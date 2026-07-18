class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # target이 들어갈 인덱스 찾기

        # 시간 복잡도: O(log n) --> 이분 탐색
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                right = mid-1 
            
            else:
                left = mid+1
                
        return left