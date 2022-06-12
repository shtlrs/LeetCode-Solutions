import random
from collections import defaultdict

class Solution:

    def __init__(self, nums: List[int]):
        self.mapp = defaultdict(list)
        self.nums = nums
        for index, num in enumerate(nums):
            self.mapp[num].append(index)

    def pick(self, target: int) -> int:
        if not self.nums:
            return None
        indices = self.mapp.get(target)
        return random.choice(indices)