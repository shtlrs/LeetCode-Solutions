from collections import defaultdict
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        d = defaultdict(list)

        for index, num in enumerate(nums):
            d[num].append(index)

        for key in d:
            l = d[key]
            n = len(l)
            if n < 2:
                continue
            for i in range(0, n - 1):
                if abs(l[i] - l[i + 1]) <= k:
                    return True
                continue
        return False