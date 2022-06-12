from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        d = defaultdict(int)
        d[0] = 1
        prefix = 0
        for num in nums:
            prefix += num
            op = prefix - k
            if op in d:
                count += d[op]
            
            d[prefix] += 1
        
        return count