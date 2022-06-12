class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        j = n - 1
        i = 0
        while i < j:
            current_sum = numbers[i] + numbers[j]
            if current_sum > target:
                j -= 1
                continue
            elif current_sum < target:
                i += 1
                continue
            else:
                return [i+1, j+1] 
        return []