class Solution:
    def reverseBits(self, n: int) -> int:
        binary_string = bin(n)[2:]
        if len(binary_string) < 32:
            binary_string = "".join(reversed('0'*(32-len(binary_string)) + binary_string))
        return int(binary_string, 2)