class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        
        for index, element in enumerate(nums):
            d[element] = index
        
        for index, element in enumerate(nums):
            remaining = target - element
            complement = d.get(remaining, None)
            if complement and complement != index:
                return [index, complement ]
        
        return None