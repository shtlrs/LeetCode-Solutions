class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_distinct_nums = sorted(list(set(nums)))
        print(sorted_distinct_nums)
        if len(sorted_distinct_nums)>=3:
            return sorted_distinct_nums[-3]
        return sorted_distinct_nums[-1]