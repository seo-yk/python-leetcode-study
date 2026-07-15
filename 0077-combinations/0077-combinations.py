class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # n개의 숫자를 k개로 쪼개 조합하고 출력하기 (중복 X)
        
        ans = []
        path = []

        def backtrack(start):
            if len(path) == k:
                ans.append(path[:])
                return
            
            for i in range(start, n+1):
                path.append(i)
                backtrack(i + 1)
                path.pop()

        backtrack(1)
        return ans