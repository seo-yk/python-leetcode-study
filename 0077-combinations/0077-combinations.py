class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        answer = []

        def combination(start, path):
            if len(path) == k:
                answer.append(path[:])
                return

            for i in range(start, n+1):
                path.append(i)
                combination(i+1, path)
                path.pop()

        combination(1, [])
        return answer