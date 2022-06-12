class Solution:
    
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        if n == 2:
            return (max(nums[0], nums[1]))
        
        if n == 3:
            return(max(nums[0] + nums[2], nums[1]))
        
        result = [nums[0], nums[1], nums[0] + nums[2]]
        
        for i in range (3, n):
            result.append(nums[i] + max(result[i-2], result[i-3]))
        
        print(result)
        return max(result)
                    
