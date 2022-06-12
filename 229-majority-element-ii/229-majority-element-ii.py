class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        distinct_elements = set(nums)
        for distinct_element in distinct_elements:
            if nums.count(distinct_element) > n/3:
                result.append(distinct_element)
        return result