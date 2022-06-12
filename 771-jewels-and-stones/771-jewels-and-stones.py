class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        d = {}
        for jewel in jewels:
            d[jewel] = jewel
        count = 0
        for stone in stones:
            if d.get(stone, None):
                count += 1
                
        return count