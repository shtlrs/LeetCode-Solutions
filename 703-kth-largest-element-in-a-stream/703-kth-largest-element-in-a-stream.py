class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.array = nums
        self.k = k

    def add(self, val: int) -> int:
        self.array.append(val)
        self.array.sort()
        return self.array[len(self.array)-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)