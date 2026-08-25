class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = bin(n)[2:]
        return answer.count("1")