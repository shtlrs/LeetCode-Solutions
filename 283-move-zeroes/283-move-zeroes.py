class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        
        count = 0
        for element in nums:
            if element != 0:
                nums[count] = element
                count += 1
        
        for i in range(count, len(nums)):
            nums[i] = 0
            
        return nums