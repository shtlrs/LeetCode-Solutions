class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_count = {}
        for num in nums:
            existing = num_count.get(num, None)
            if not existing:
                num_count[num] = 1
                continue
            return True
        return False