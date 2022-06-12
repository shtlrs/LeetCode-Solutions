class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        n = len(nums)
        result = [0] * n
        parity = 0
        for element in nums:
            if element %2 == 0:
                result[parity]=element
                parity += 2
        parity = 1
        for element in nums:
            if element %2 != 0:
                result[parity] = element
                parity += 2
        return result