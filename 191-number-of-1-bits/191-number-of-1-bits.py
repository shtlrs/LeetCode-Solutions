class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_string = bin(n)[2:]
        return binary_string.count("1")