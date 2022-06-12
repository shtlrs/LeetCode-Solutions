class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        distinct_elements = set(nums)
        return [element for element in distinct_elements if nums.count(element) > n/3]
