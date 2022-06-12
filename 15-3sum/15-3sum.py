from collections import defaultdict


class Solution:
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        j = n - 1
        i = 0
        result = []
        while i < j:
            current_sum = numbers[i] + numbers[j]
            if current_sum > target:
                j -= 1
                continue
            elif current_sum < target:
                i += 1
                continue
            else:
                result.append([numbers[i], numbers[j]])
                i += 1
        return result
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(0, n-2):
            if i > 1 and nums[i] == nums[i-1]:
                continue
            solutions = self.twoSum(nums[i+1:], -nums[i])
            for solution in solutions:
                sol = [nums[i], solution[0], solution[1]]
                if sol not in result:
                    result.append(sol)
        
        return result
            
        
        
        