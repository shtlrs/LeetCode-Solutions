class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if not nums:
            return []
        
        if len(nums) == 1:
            return [str(nums[0])]
        
        ranges = []
        result = []
        start, i = 0, 1
        n = len(nums)
        
        while i != n:

            if nums[i] - nums[i - 1] == 1:
                i += 1
                continue
            
            if nums[i - 1] == nums[start]:
                ranges.append(str(nums[start]))
            else:
                ranges.append([str(nums[start]), str(nums[i-1])])
            
            start = i
            i += 1
        
        
        if nums[start] == nums[i - 1]:
            ranges.append(str(nums[start]))
        else:
            ranges.append([str(nums[start]), str(nums[i - 1])])
                            
        for r in ranges:
            if type(r) == list:
                result.append("->".join(r))
            else:
                result.append(r)
        
        return result
            
        
        