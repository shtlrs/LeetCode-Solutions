class Solution:
    units = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }

    tens = {
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
    }

    wenties = {
        2: "Twenty",
        3: "Thirty",
        4: "Forty",
        5: "Fifty",
        6: "Sixty",
        7: "Seventy",
        8: "Eighty",
        9: "Ninety"
    }

    def decompose(self, num: int):
        h = num // 100
        t = num % 100

        result = ""
        if h:
            result += f"{self.units.get(h)} Hundred"
        if self.tens.get(t, None):
            result += f" {self.tens.get(t)}"
        else:
            t = num % 100 // 10
            if t:
                result += f" {self.wenties.get(t)}"
            u = num % 100 % 10
            if u:
                result += f" {self.units.get(u)}"

        return result

    def numberToWords(self, num: int) -> str:
        
        if num == 0:
            return "Zero"
        
        billions = num // 10 ** 9
        num = num % 10 ** 9
        millions = num // 10 ** 6
        num = num % 10 ** 6
        thousands = num // 10 ** 3
        num = num % 10 ** 3

        result = ""

        if billions:
            result += f"{self.decompose(billions)} Billion"

        if millions:
            result += f" {self.decompose(millions)} Million"

        if thousands:
            result += f" {self.decompose(thousands)} Thousand"

        if num:
            result += f" {self.decompose(num)}"

        return " ".join(result.split())