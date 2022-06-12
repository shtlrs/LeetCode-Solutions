class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        distinct_elements = set(nums)
        result = [element for element in distinct_elements if nums.count(element) > n/3]
        return result