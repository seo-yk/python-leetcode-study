class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
         문제 제약조건:
            시간 복잡도: O(N log N)
            공간 복잡도: O(N)
        """


        # Priority Queue / Heap
        """
        최대힙: 전부 넣기 -> K번째로 꺼내진 원소
            시간 복잡도: O(N log N)
            공간 복잡도: O(N)

        최소힙: 크기를 딱 K개로만 유지해서 탐색
            시간 복잡도: O(N log K)
            공간 복잡도: O(K)
        """

        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num) # 일단 넣고

            if k < len(min_heap):
                heapq.heappop(min_heap) # 최종 K 크기 유지

        return min_heap[0]

        # Quick Select O(N)
        """
            랜덤한 pivot 값 기준으로 좌, 우 나눠서 풀이
        """
        
        """
        pivot = nums[len(nums)//2]

        left = [num for num in nums if x > pivot]
        mid = [num for num in nums if x == pivot]
        right = [num for num in nums if x < pivot]

        if len(left) >= k:
            return self.findKthLargest(left, k)

        elif len(left) + len(mind) >= k:
            return pivot
        
        else:
            k = k - len(left) + len(mid)
            return self.findKthLargest(right, k)
        """
