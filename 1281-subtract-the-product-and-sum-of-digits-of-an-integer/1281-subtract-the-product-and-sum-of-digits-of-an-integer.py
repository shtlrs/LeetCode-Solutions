class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        numbers = [int(char) for char in str(n)]
        product = 1
        summ = 0
        for number in numbers:
            product *= number
            summ += number
        
        return product - summ