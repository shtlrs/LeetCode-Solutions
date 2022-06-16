from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # If empty return directly
        
        # Iterate over the list and save the count of each element
        
        # Iterate over the dictionary & return all elements whose count > k
    
        if not nums:
            return []
        
        d = defaultdict(int)
        result = []
        
        for num in nums:
            
            d[num] += 1
            
        d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
        keys = list(d.keys())
        n = len(keys)
        return keys[n-k:]
        
        